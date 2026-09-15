"""Full one-generation anomaly matrices, exact beta counts, and CKM reconstruction."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from itertools import product
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
rng=np.random.default_rng(890915);records=[]


def check(name,actual,expected,tol=3e-11):
    err=float(np.max(np.abs(np.asarray(actual)-expected)));scale=max(1.,float(np.max(np.abs(expected))))
    records.append(dict(name=name,scaled_residual=err/scale,passed=err<tol*scale))


def unitary(n):return np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]


def su(n):
    out=[]
    for a in range(n):
        for b in range(a+1,n):
            T=np.zeros((n,n),complex);T[a,b]=T[b,a]=.5;out.append(T)
            T=np.zeros((n,n),complex);T[a,b]=-.5j;T[b,a]=.5j;out.append(T)
    for k in range(1,n):out.append(np.diag([1.]*k+[-float(k)]+[0.]*(n-k-1))/np.sqrt(2*k*(k+1)))
    return out


def blockdiag(xs):
    out=np.zeros((sum(len(x) for x in xs),)*2,complex);i=0
    for x in xs:out[i:i+len(x),i:i+len(x)]=x;i+=len(x)
    return out


# q(6), ubar(3), dbar(3), ell(2), ebar(1).
color=[blockdiag([np.kron(t,np.eye(2)),-t.T,-t.T,np.zeros((2,2)),np.zeros((1,1))]) for t in su(3)]
weak=[blockdiag([np.kron(np.eye(3),t),np.zeros((3,3)),np.zeros((3,3)),t,np.zeros((1,1))]) for t in su(2)]
Y=np.diag([1/6]*6+[-2/3]*3+[1/3]*3+[-1/2]*2+[1])
gen=color+weak+[Y]
anomalies=np.array([np.trace(A@(B@C+C@B))/2 for A,B,C in product(gen,repeat=3)])
check('all 1728 symmetric gauge traces',anomalies,np.zeros(12**3))
check('all 12 mixed gravity traces',[np.trace(t) for t in gen],np.zeros(12))
check('one-generation color indices',[np.trace(t@t) for t in color],np.full(8,2.))
check('one-generation weak indices',[np.trace(t@t) for t in weak],np.full(3,2.))
check('one-generation hypercharge index',np.trace(Y@Y),10/3)
# Separate exact arithmetic includes scalar and family multiplicities.
charges=[F(1,6),F(-2,3),F(1,3),F(-1,2),F(1)]
multiplicities=[6,3,3,2,1]
assert sum(n*y**3 for n,y in zip(multiplicities,charges))==0
assert sum(n*y for n,y in zip(multiplicities,charges))==0
indices=[sum(n*y*y for n,y in zip(multiplicities,charges))*3,F(6),F(6)]
betas=[-F(11,3)*ca+F(2,3)*ferm+F(1,3)*scalar for ca,ferm,scalar in zip([0,2,3],indices,[F(1,2),F(1,2),0])]
assert betas==[F(41,6),F(-19,6),F(-7)]
check('exact one-loop beta rational coefficients',[float(x) for x in betas],[41/6,-19/6,-7])


def km(c1,s1,c2,s2,c3,s3,phase):
    return np.array([[c1,s1*c3,s1*s3],[-s1*c2,c1*c2*c3-s2*s3*phase,c1*c2*s3+s2*c3*phase],[-s1*s2,c1*s2*c3+c2*s3*phase,c1*s2*s3-c2*c3*phase]])


def J(V):return (V[0,0]*V[1,1]*V[0,1].conjugate()*V[1,0].conjugate()).imag


for sample in range(7):
    Xd,Yd,Xu,Yu=(unitary(3) for _ in range(4))
    dd=np.array([.2,.5,1.]);du=np.array([.1,.7,1.4])
    yd=Xd@np.diag(dd)@Yd.conj().T;yu=Xu@np.diag(du)@Yu.conj().T
    D=Xd.conj();U=Xu.conj();V=U.conj().T@D
    check(f'down two-left Yukawa {sample}',D.T@yd@Yd,np.diag(dd))
    check(f'up two-left Yukawa {sample}',U.T@yu@Yu,np.diag(du))
    check(f'down left mass squared {sample}',D.conj().T@(yd.conj()@yd.T)@D,np.diag(dd*dd))
    check(f'up left mass squared {sample}',U.conj().T@(yu.conj()@yu.T)@U,np.diag(du*du))
    check(f'CKM unitary {sample}',V.conj().T@V,np.eye(3))
    alpha,beta=rng.normal(size=(2,3))
    W=np.exp(-1j*beta)[:,None]*V*np.exp(1j*alpha)[None,:]
    check(f'quartet rephasing {sample}',J(W),J(V))
    check(f'CP conjugate {sample}',J(V.conj()),-J(V))
    # Canonical first row positive, first column negative below first entry.
    alpha=-np.angle(V[0,:]);beta=alpha[0]+np.angle(V[:,0])
    real_edges=np.exp(-1j*beta)[:,None]*V*np.exp(1j*alpha)[None,:]
    real_edges[1:]*=-1
    c1=real_edges[0,0].real;s1=np.sqrt(1-c1*c1)
    a=-real_edges[1:,0].real/s1;b=real_edges[0,1:].real/s1
    ap=np.array([-a[1],a[0]]);bp=np.array([-b[1],b[0]])
    z=ap@real_edges[1:,1:]@bp
    rebuilt=km(c1,s1,*a,*b,-z)
    check(f'four-parameter reconstruction {sample}',rebuilt,real_edges)
    check(f'orthogonal block phase modulus {sample}',abs(z),1.)
    expected=c1*s1*s1*a[0]*a[1]*b[0]*b[1]*(-z).imag
    check(f'J formula {sample}',J(rebuilt),expected)

s1,s2,s3=.224,.041,.016;c1,c2,c3=np.sqrt(1-np.array([s1,s2,s3])**2)
V=km(c1,s1,c2,s2,c3,s3,np.exp(1j*np.deg2rad(40)))
example=dict(J=J(V),absolute_matrix=np.abs(V).tolist())
result=dict(checks=len(records),passed=all(x['passed'] for x in records),records=records,
            exact_beta_coefficients=[str(x) for x in betas],source_example=example,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'checks/srednicki/quarks89-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(checks=len(records),passed=result['passed'],max_scaled_residual=max(x['scaled_residual'] for x in records),failures=[x for x in records if not x['passed']],source_example=example),indent=2))
raise SystemExit(0 if result['passed'] else 1)
