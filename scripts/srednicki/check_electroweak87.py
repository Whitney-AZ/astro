"""Original SU(2) curvature vertices, real mass basis, and explicit H decay spins."""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import numpy as np
from check_background78 import Poly,eps

ROOT=Path(__file__).resolve().parents[2]
rng=np.random.default_rng(870915)
metric=np.array([-1.,1.,1.,1.]);eta=np.diag(metric)
records=[]


def check(name,actual,expected,tol=3e-11):
    residual=float(np.max(np.abs(np.asarray(actual)-expected)))
    scale=max(1.,float(np.max(np.abs(expected))))
    records.append(dict(name=name,scaled_residual=residual/scale,passed=residual<tol*scale))


def dot(u,v):return np.dot(metric*u,v)


def original_vertex(legs,g,sw,cw):
    fields=[[Poly() for mu in range(4)] for a in range(3)]
    directions={'+':[1/np.sqrt(2),1j/np.sqrt(2),0],'-':[1/np.sqrt(2),-1j/np.sqrt(2),0],'A':[0,0,sw],'Z':[0,0,cw]}
    for tag,(kind,p,u) in enumerate(legs):
        for a,mu in product(range(3),range(4)):
            fields[a][mu]+=Poly({1<<tag:complex(directions[kind][a]*metric[mu]*u[mu])})
    def derivative(field,mu):
        return Poly({mask:value*1j*metric[mu]*sum(leg[1][mu] for tag,leg in enumerate(legs) if mask&(1<<tag)) for mask,value in field.items()})
    lag=Poly()
    for a,mu,nu in product(range(3),range(4),range(4)):
        F=derivative(fields[a][nu],mu)+(-1)*derivative(fields[a][mu],nu)
        for b,c in product(range(3),repeat=2):F+=float(g*eps(a,b,c))*fields[b][mu]*fields[c][nu]
        lag+=(-.25*metric[mu]*metric[nu])*F*F
    return 1j*lag.get((1<<len(legs))-1,0)


for g1,g2 in [(.31,.7),(.9,.4)]:
    den=np.hypot(g1,g2);sw=g1/den;cw=g2/den
    charge={'A':g2*sw,'Z':g2*cw}
    for kinds in [('+','-','A'),('+','-','Z'),('+','-','A','A'),('+','-','A','Z'),('+','-','Z','Z'),('+','-','+','-')]:
        for sample in range(3):
            momenta=[rng.normal(size=4) for _ in range(len(kinds)-1)];momenta.append(-sum(momenta))
            u,v,w,z=rng.normal(size=(4,4))
            vectors=[u,v,w,z][:len(kinds)]
            legs=list(zip(kinds,momenta,vectors))
            if len(kinds)==3:
                p,q,k=momenta
                formula=1j*charge[kinds[2]]*(dot(p-q,w)*dot(u,v)+dot(q-k,u)*dot(v,w)+dot(k-p,v)*dot(w,u))
            elif kinds[2] in charge:
                formula=-1j*charge[kinds[2]]*charge[kinds[3]]*(2*dot(u,v)*dot(w,z)-dot(u,w)*dot(v,z)-dot(u,z)*dot(v,w))
            else:formula=1j*g2*g2*(2*dot(u,w)*dot(v,z)-dot(u,v)*dot(w,z)-dot(u,z)*dot(w,v))
            check(f'vertex {g1,g2,kinds,sample}',original_vertex(legs,g2,sw,cw),formula)
    v0=1.7
    ts=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]],-np.eye(2)],dtype=complex)/2
    realT=np.array([1j*np.block([[t.imag,t.real],[-t.real,t.imag]]) for t in ts])
    tau=1j*np.array([g2,g2,g2,g1])[:,None,None]*realT
    F=(tau@np.array([v0,0,0,0])).real
    target=v0/2*np.array([[0,0,0,g2],[0,-g2,0,0],[0,0,g2,0],[0,0,-g1,0]])
    check(f'orbit {g1,g2}',F,target)
    ST=np.eye(4);ST[2:,2:]=[[cw,-sw],[sw,cw]]
    R=np.array([[0,0,0,1],[0,-1,0,0],[0,0,1,0],[1,0,0,0]])
    MW=g2*v0/2;MZ=den*v0/2
    check(f'explicit SVD {g1,g2}',ST@F@R.T,np.diag([MW,MW,MZ,0]))
    for xi in [.3,2.]:
        H=np.diag([1.2*v0*v0/2,0,0,0])
        check(f'scalar mass {g1,g2,xi}',R@(H+xi*F.T@F)@R.T,np.diag([xi*MW*MW,xi*MW*MW,xi*MZ*MZ,1.2*v0*v0/2]))
    for sample in range(3):
        A=rng.normal(size=(3,4));dA=rng.normal(size=(3,4,4))
        B=rng.normal(size=4);dB=rng.normal(size=(4,4))
        Fs=dA-dA.transpose(0,2,1)
        for a,b,c in product(range(3),repeat=3):Fs[a]+=g2*eps(a,b,c)*np.outer(A[b],A[c])
        Bcurl=dB-dB.T
        original=-.25*np.einsum('m,n,amn,amn',metric,metric,Fs,Fs)-.25*np.einsum('m,n,mn,mn',metric,metric,Bcurl,Bcurl)
        W=(A[0]-1j*A[1])/np.sqrt(2);dW=(dA[0]-1j*dA[1])/np.sqrt(2)
        photon=sw*A[2]+cw*B;Z=cw*A[2]-sw*B
        Fphoton=sw*(dA[2]-dA[2].T)+cw*Bcurl
        FZ=cw*(dA[2]-dA[2].T)-sw*Bcurl
        D=dW-1j*np.outer(g2*A[2],W)
        chargeK=-np.einsum('m,n,mn,mn',metric,metric,D.conj(),D)+np.einsum('m,n,mn,nm',metric,metric,D.conj(),D)
        magnetic=1j*g2*np.einsum('m,n,mn,m,n',metric,metric,sw*Fphoton+cw*FZ,W,W.conj())
        quartic=-g2*g2/2*(dot(W,W.conj())**2-dot(W,W)*dot(W.conj(),W.conj()))
        final=-.25*np.einsum('m,n,mn,mn',metric,metric,Fphoton,Fphoton)-.25*np.einsum('m,n,mn,mn',metric,metric,FZ,FZ)+chargeK+magnetic+quartic
        check(f'full curvature density {g1,g2,sample}',final,original)


def pols(M,p):
    E=np.sqrt(M*M+p@p);direction=p/np.linalg.norm(p)
    B=np.eye(4);B[0,0]=E/M;B[0,1:]=p/M;B[1:,0]=p/M
    B[1:,1:]+=np.outer(direction,direction)*(E/M-1)
    return B[:,1:]


e=np.sqrt(4*np.pi/127.9);g2=e/np.sqrt(.231);g1=e/np.sqrt(.769);v0=160.8/g2
for M in [.8,80.4,91.2]:
    for ratio in [2.01,2.5,10.,100.]:
        mH=ratio*M;n=rng.normal(size=3);n/=np.linalg.norm(n)
        p=n*np.sqrt(mH*mH/4-M*M)
        E1=pols(M,p);E2=pols(M,-p)
        amplitudes=-2*M*M/v0*(E1.T@eta@E2)
        x=M*M/(mH*mH)
        check(f'decay nine polarizations {M,ratio}',np.sum(np.abs(amplitudes)**2),mH**4/v0**2*(1-4*x+12*x*x))
inputs=dict(e=e,g1=g1,g2=g2,v=v0,GF=1/(np.sqrt(2)*v0*v0),MZ_from_angle=80.4/np.sqrt(.769))
widths=[]
for M,S in [(80.4,1),(91.2,2)]:
    x=M*M/200**2
    widths.append(dict(M=M,x=x,beta=np.sqrt(1-4*x),polynomial=1-4*x+12*x*x,width=200**3/(16*np.pi*v0*v0*S)*np.sqrt(1-4*x)*(1-4*x+12*x*x)))
check('WW numerical table',widths[0]['width'],1.03832,tol=1e-5)
check('ZZ numerical table',widths[1]['width'],.368938,tol=1e-6)
helper=Path(__file__).with_name('check_background78.py')
result=dict(checks=len(records),passed=all(r['passed'] for r in records),records=records,inputs=inputs,widths=widths,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=sha256(helper.read_bytes()).hexdigest())
(ROOT/'checks/srednicki/electroweak87-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(checks=len(records),passed=result['passed'],max_scaled_residual=max(r['scaled_residual'] for r in records),failures=[r for r in records if not r['passed']],inputs=inputs,widths=widths),indent=2))
raise SystemExit(0 if result['passed'] else 1)
