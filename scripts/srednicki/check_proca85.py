"""Finite Proca/Rxi kernels and gauge-invariant interpolators."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
metric=np.diag([-1.,1.,1.,1.])
records=[]


def check(name, actual, expected):
    residual=float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))
    scale=max(1.,float(np.max(np.abs(expected))))
    records.append(dict(name=name,residual=residual,passed=residual<3e-11*scale))


for M in [.7,2.1]:
    for k in [np.array([3.,1.,1.,0.]),np.array([1.,3.,0.,2.]),np.array([1.,0.,0.,1.])]:
        k2=k@metric@k;kk=np.outer(k,k)
        unitary=(metric+kk/(M*M))/(k2+M*M)
        for xi in [.25,1.,3.,100.]:
            K=(k2+M*M)*metric-(1-1/xi)*kk
            Delta=np.linalg.inv(K)
            # Inverse of the upper-index matrix is lower-index: raise twice.
            Delta=metric@Delta@metric
            formula=(metric+(xi-1)*kk/(k2+xi*M*M))/(k2+M*M)
            tag=f"M={M},k={k.tolist()},xi={xi}"
            check(tag+" inverse",Delta,formula)
            check(tag+" invariant pole",Delta+kk/(M*M*(k2+xi*M*M)),unitary)
    for p in [np.array([.3,.4,.7]),np.array([2.,-.5,1.])]:
        E=np.sqrt(p@p+M*M);n=p/np.linalg.norm(p)
        boost=np.eye(4);boost[0,0]=E/M
        boost[0,1:]=p/M;boost[1:,0]=p/M
        boost[1:,1:]+=np.outer(n,n)*(E/M-1)
        eps=boost[:,1:]
        k=np.r_[E,p]
        check(f"boosted completeness {M,p.tolist()}",eps@eps.T,metric+np.outer(k,k)/(M*M))
        check(f"boosted canonical {M,p.tolist()}",
              eps[1:,:]@(E*eps[1:,:]-np.outer(p,eps[0,:])).T,E*np.eye(3))

g=.6;v=1.3
for j in [1,2,3]:
    h=.1*j;b=-.2*j;dh=np.array([.2,-.3,.5,.1])*j
    db=np.array([-.1,.4,.3,-.2])*j;A=np.array([.3,.7,-.2,.5])
    phi=(v+h+1j*b)/np.sqrt(2)
    dphi=(dh+1j*db)/np.sqrt(2)
    def current(phi,dphi,A):
        D=dphi-1j*g*A*phi
        return 1j*(phi.conjugate()*D-D.conjugate()*phi)/(g*v*v)
    original=current(phi,dphi,A)
    expansion=(g*A*((v+h)**2+b*b)-(v+h)*db+b*dh)/(g*v*v)
    check(f"current expansion {j}",original,expansion)
    theta=.4*j;dtheta=np.array([.1,-.2,.4,.3])*j;phase=np.exp(-1j*g*theta)
    check(f"current finite local gauge {j}",
          current(phase*phi,phase*(dphi-1j*g*dtheta*phi),A-dtheta),original)

result=dict(checks=len(records),passed=all(x['passed'] for x in records),
            records=records,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'checks/srednicki/proca85-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(checks=len(records),passed=result['passed'],
                     max_residual=max(x['residual'] for x in records),
                     failures=[x for x in records if not x['passed']]),indent=2))
raise SystemExit(0 if result['passed'] else 1)
