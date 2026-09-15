"""Gauge mass spectra and constrained vacuum directions in section 84."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from itertools import product
import json
import numpy as np
from check_matrix80 import basis

ROOT=Path(__file__).resolve().parents[2]
records=[]


def check(name, actual, expected, tol=2e-10):
    residual=float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))
    scale=max(1.,float(np.max(np.abs(expected))))
    records.append(dict(name=name,residual=residual,passed=residual<tol*scale))


for n in range(2,7):
    t=basis(n)[:-1]/np.sqrt(2)
    v=np.zeros(n);v[-1]=1.
    vectors=t@v
    gram=(vectors.conj()@vectors.T).real
    expected=sorted([0.]*((n-1)**2-1)+[.25]*(2*n-2)+[(n-1)/(2*n)])
    check(f"SU{n} fundamental",np.linalg.eigvalsh(gram),expected)
    so=[]
    for i in range(n):
        for j in range(i+1,n):
            a=np.zeros((n,n),complex);a[i,j]=-1j;a[j,i]=1j;so.append(a)
    vectors=np.array(so)@v
    check(f"SO{n} fundamental",np.linalg.eigvalsh((vectors.conj()@vectors.T).real),
          [0.]*((n-1)*(n-2)//2)+[1.]*(n-1))

for eigs in [[-1.,1.],[-1.,0.,1.],[-1.,-1.,1.,1.],[-1/3]*3+[.5]*2]:
    n=len(eigs);t=basis(n)[:-1]/np.sqrt(2)
    # A non-diagonal conjugate of the proposed background.
    H=sum(((j+1)/len(t)*a for j,a in enumerate(t)),np.zeros((n,n),complex))
    w,q=np.linalg.eigh(H);rotation=(q*np.exp(1j*w))@q.conj().T
    V=rotation@np.diag(eigs)@rotation.conj().T
    comm=np.array([a@V-V@a for a in t])
    mass=-2*np.einsum('aij,bji->ab',comm,comm).real
    expected=sorted([0.]*(n-1)+[(eigs[i]-eigs[j])**2
                     for i in range(n) for j in range(i+1,n) for _ in range(2)])
    check(f"adjoint eigenvalues {eigs}",np.linalg.eigvalsh(mass),expected)
    # Projection on every canonically normalized real adjoint component.
    component=2*np.einsum('dij,aji->ad',t,comm)
    check(f"adjoint component Gram {eigs}",(component.conj()@component.T).real,mass)

# Exact rational comparison of all two-block multiplicities.
for n in range(2,11):
    values=[Fraction(n,k*(n-k))-Fraction(3,n) for k in range(1,n)]
    target=Fraction(1,n) if n%2==0 else Fraction(n*n+3,n*(n*n-1))
    check(f"two block minimum N={n}",float(min(values)),float(target),1e-14)

# Direct constrained curves through representative three-root stationary points.
seen=set();directions=[]
for n in range(4,9):
    for count_r in range(1,n-1):
        for count_s in range(1,n-count_r):
            count_t=n-count_r-count_s
            roots=np.array([count_t-count_s,count_r-count_t,count_s-count_r],float)
            if count_r==count_s==count_t: roots=np.array([-2.,-1.,3.])
            if len(set(roots))!=3:continue
            order=np.argsort(roots);mult=np.array([count_r,count_s,count_t])[order]
            roots=roots[order]/np.sqrt(np.dot([count_r,count_s,count_t],roots**2))
            key=(tuple(mult),tuple(np.round(roots,12)))
            if key in seen:continue
            seen.add(key)
            a,b,c=roots;r,s,t=mult
            x=np.repeat(roots,mult);z=np.zeros(n)
            if s>=2:
                z[r:r+2]=[1.,-1.]
            else:
                z[:r]=(c-b)/r;z[r]=-(c-a);z[r+1:]=(b-a)/t
            check(f"three root tangent {key}",[np.sum(z),np.dot(x,z)],[0.,0.])
            eta=1e-4
            plus=(x+eta*z)/np.sqrt(1+eta*eta*np.dot(z,z))
            minus=(x-eta*z)/np.sqrt(1+eta*eta*np.dot(z,z))
            descent=(np.sum(plus**4)+np.sum(minus**4))/2-np.sum(x**4)
            records.append(dict(name=f"three root descent {key}",passed=bool(descent<0),
                                energy_difference=float(descent)))
            directions.append(dict(N=n,multiplicities=mult.tolist(),
                                   roots=roots.tolist(),descent=float(descent)))
for angle in [.2,.7,1.1,2.3]:
    x=np.cos(angle)*np.array([-1.,0.,1.])/np.sqrt(2)
    x+=np.sin(angle)*np.array([1.,-2.,1.])/np.sqrt(6)
    check(f"N3 flat direction {angle}",np.sum(x**4),.5)

Y=np.array([-1/3]*3+[.5]*2)
for m2,l1,l2 in [(2.,.3,.7),(.1,1.,2.),(3.,2.,.2)]:
    v2=36*m2/(7*l1+30*l2);V=np.sqrt(v2)*Y
    potential=-m2*np.sum(V*V)/2+l1*np.sum(V**4)/4+l2*np.sum(V*V)**2/4
    check(f"SU5 potential {m2,l1,l2}",potential,-15*m2*m2/(2*(7*l1+30*l2)))
    grad=-m2*V+l1*V**3+l2*np.sum(V*V)*V
    check(f"SU5 traceless gradient {m2,l1,l2}",grad-grad.mean(),np.zeros(5))

result=dict(checks=len(records),passed=all(x['passed'] for x in records),
            records=records,three_root_directions=directions,
            script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
            helper_sha256=sha256((Path(__file__).parent/'check_matrix80.py').read_bytes()).hexdigest())
(ROOT/'checks/srednicki/higgs84-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(checks=len(records),passed=result['passed'],
                     three_root_samples=len(directions),
                     failures=[r for r in records if not r['passed']]),indent=2))
raise SystemExit(0 if result['passed'] else 1)
