"""Explicit spinors and unsimplified traces for muon decay, plus massive phase space."""
from pathlib import Path
from hashlib import sha256
from itertools import product,permutations
from decimal import Decimal,localcontext
import json
import numpy as np
from check_helicity60 import GAMMA,slash,U

ROOT=Path(__file__).resolve().parents[2]
rng=np.random.default_rng(880915)
eta=np.diag([-1.,1.,1.,1.]);metric=np.diag(eta)
PL=np.diag([1.,1.,0.,0.]);PR=np.eye(4)-PL
C=np.block([[-U,np.zeros((2,2))],[np.zeros((2,2)),U]])
eps=np.zeros((4,4,4,4))
for p in permutations(range(4)):
    inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    eps[p]=(-1)**inversions
records=[]


def check(name,actual,expected,tol=3e-11):
    err=float(np.max(np.abs(np.asarray(actual)-expected)));scale=max(1.,float(np.max(np.abs(expected))))
    records.append(dict(name=name,scaled_residual=err/scale,passed=err<tol*scale))


def dot(a,b):return a@eta@b

def bar(u):return u.conj()@GAMMA[0]


def spinors(p,m,sign=1):
    density=(-slash(p)+sign*m*np.eye(4))@GAMMA[0]
    vals,vecs=np.linalg.eigh(density)
    return vecs[:,vals>1e-9]*np.sqrt(vals[vals>1e-9])


def trace_tensor(a,b):
    return np.array([[np.trace(slash(a)@GAMMA[mu]@slash(b)@GAMMA[nu]@PL) for nu in range(4)] for mu in range(4)])


for sample in range(5):
    a,b,c,d=rng.normal(size=(4,4))
    T=trace_tensor(a,b)
    sym=np.outer(a,b)+np.outer(b,a)-eta*dot(a,b)
    anti=np.einsum('mnrs,r,s->mn',eps,eta@a,eta@b)
    check(f'full chiral tensor {sample}',T,2*(sym-1j*anti))
    check(f'contracted chiral tensors {sample}',np.einsum('m,n,mn,mn',metric,metric,T,trace_tensor(c,d)),16*dot(a,c)*dot(b,d))

m=5.;GF=.3
for me in [0.,.4,3.5]:
    for sample in range(3):
        s=me*me+(m*m-me*me)*(.2+.25*sample)
        n=rng.normal(size=3);n/=np.linalg.norm(n)
        Eq=(m*m-s)/(2*m);q=np.r_[Eq,Eq*n];P=np.array([m,0.,0.,0.]);pair=P-q
        n2=rng.normal(size=3);n2/=np.linalg.norm(n2)
        Er=(s-me*me)/(2*np.sqrt(s));Ek=(s+me*me)/(2*np.sqrt(s))
        rest_r=np.r_[Er,Er*n2];rest_k=np.r_[Ek,-Er*n2]
        direction=pair[1:]/np.linalg.norm(pair[1:]);boost=np.eye(4)
        boost[0,0]=pair[0]/np.sqrt(s);boost[0,1:]=pair[1:]/np.sqrt(s);boost[1:,0]=pair[1:]/np.sqrt(s)
        boost[1:,1:]+=np.outer(direction,direction)*(pair[0]/np.sqrt(s)-1)
        r=boost@rest_r;k=boost@rest_k
        um=spinors(P,m);ue=spinors(k,me);un=spinors(r,0.);vn=spinors(q,0.,-1)
        total=0.
        for im,ie,inu,ia in product(range(2),repeat=4):
            a=um[:,im];b=ue[:,ie];c=un[:,inu];d=vn[:,ia]
            vector=sum(metric[mu]*(bar(b)@GAMMA[mu]@PL@d)*(bar(c)@GAMMA[mu]@PL@a) for mu in range(4))
            scalar=(a.T@C@PL@d)*(bar(b)@PR@C@bar(c).T)
            check(f'external Fierz {me,sample,im,ie,inu,ia}',vector,-2*scalar)
            v1=C@bar(a).T;v2=C@bar(c).T
            conjugate=(bar(d)@PR@v1)*(bar(v2)@PL@b)
            check(f'external conjugate {me,sample,im,ie,inu,ia}',conjugate,scalar.conjugate())
            total+=abs(2*np.sqrt(2)*GF*vector)**2/2
        expected=64*GF*GF*dot(P,q)*dot(r,k)
        check(f'explicit spin sum {me,sample}',total,expected)
        trace=0j
        for mu,nu in product(range(4),repeat=2):
            t1=np.trace((-slash(k)+me*np.eye(4))@GAMMA[mu]@PL@(-slash(q))@GAMMA[nu]@PL)
            t2=np.trace((-slash(r))@GAMMA[mu]@PL@(-slash(P)+m*np.eye(4))@GAMMA[nu]@PL)
            trace+=metric[mu]*metric[nu]*t1*t2
        check(f'unsimplified massive vector traces {me,sample}',4*GF*GF*trace,expected)

for rank in [1,2,3]:
    L0,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
    R0,_=np.linalg.qr(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
    y=L0@np.diag([.4,.7,1.1][:rank]+[0.]*(3-rank))@R0.conj().T
    left,d,rightH=np.linalg.svd(y);L=left.conj();E=rightH.conj().T
    check(f'two-left-field Yukawa rank {rank}',L.T@y@E,np.diag(d))
    check(f'charged current preserved rank {rank}',L.conj().T@L,np.eye(3))

nodes,weights=np.polynomial.legendre.leggauss(700)
y=(nodes+1)/2;weights=weights/2
phase=[]
for rho in [0.,(.511/105.7)**2,.01,.1,.5,.81]:
    # Map the actual massive pair invariant s to z=rho+(1-rho)y.
    z=rho+(1-rho)*y
    integral=float(np.dot(weights,(1-rho)*(1-z)**2*(z-rho)**2/z))
    with localcontext() as ctx:
        ctx.prec=50;r=Decimal(str(rho))
        f=float(1-8*r+8*r**3-r**4-12*r*r*r.ln()) if rho else 1.
    check(f'massive width integral rho={rho}',12*integral,f,tol=2e-11)
    phase.append(dict(rho=rho,quadrature_factor=12*integral,formula_factor=f))
helper=Path(__file__).with_name('check_helicity60.py')
result=dict(checks=len(records),passed=all(x['passed'] for x in records),records=records,phase=phase,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=sha256(helper.read_bytes()).hexdigest())
(ROOT/'checks/srednicki/leptons88-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(checks=len(records),passed=result['passed'],max_scaled_residual=max(x['scaled_residual'] for x in records),failures=[x for x in records if not x['passed']],phase=phase),indent=2))
raise SystemExit(0 if result['passed'] else 1)
