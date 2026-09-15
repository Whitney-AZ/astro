"""Realification, mixed-coupling mass bases, and direct scalar kinetic vertices."""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import numpy as np
from check_background78 import Poly

ROOT=Path(__file__).resolve().parents[2]
rng=np.random.default_rng(860915)
records=[]
metric=np.array([-1.,1.,1.,1.])


def check(name,actual,expected,tol=2e-11):
    err=float(np.max(np.abs(np.asarray(actual)-expected)))
    scale=max(1.,float(np.max(np.abs(expected))))
    records.append(dict(name=name,scaled_residual=err/scale,passed=err<tol*scale))


def realify(z):
    return np.block([[z.real,-z.imag],[z.imag,z.real]])


def generators(n):
    ts=[]
    for i in range(n):
        for j in range(i+1,n):
            t=np.zeros((n,n),complex);t[i,j]=t[j,i]=.5;ts.append(t)
            t=np.zeros((n,n),complex);t[i,j]=-.5j;t[j,i]=.5j;ts.append(t)
    for k in range(1,n):
        ts.append(np.diag([1.]*k+[-float(k)]+[0.]*(n-k-1))/np.sqrt(2*k*(k+1)))
    return np.array(ts+[np.eye(n)/2])


def kinetic_vertex(tau,v,legs):
    """Coefficient from -1/2 (d phi - A tau phi)^2, before expanding it."""
    ns=len(v);ng=len(tau)
    phi=[Poly({0:complex(x)}) for x in v]
    A=[[Poly() for mu in range(4)] for a in range(ng)]
    for tag,(kind,direction,p,eps) in enumerate(legs):
        for i,x in enumerate(direction):
            if kind=='s': phi[i]+=Poly({1<<tag:complex(x)})
            else:
                for mu in range(4): A[i][mu]+=Poly({1<<tag:complex(x*eps[mu]*metric[mu])})
    lag=Poly()
    for mu in range(4):
        for i in range(ns):
            d=Poly({mask:val*1j*metric[mu]*sum(leg[2][mu] for tag,leg in enumerate(legs) if mask&(1<<tag)) for mask,val in phi[i].items()})
            for a,j in product(range(ng),range(ns)):
                d+=(-float(tau[a,i,j]))*A[a][mu]*phi[j]
            lag+=(-.5*metric[mu])*d*d
    return 1j*lag.get((1<<len(legs))-1,0)


for n in [2,3,4]:
    ts=generators(n);ng=len(ts);ns=2*n
    couplings=np.array([.7]*(ng-1)+[.31])
    tau=np.array([-couplings[a]*realify(-1j*t) for a,t in enumerate(ts)])
    structure=np.zeros((ng,ng,ng))
    for a,b,c in product(range(ng-1),repeat=3):
        structure[a,b,c]=(-2j*np.trace((ts[a]@ts[b]-ts[b]@ts[a])@ts[c])).real
    h=couplings[:,None,None]*structure
    check(f'SU({n}) algebra',np.array([[tau[a]@tau[b]-tau[b]@tau[a] for b in range(ng)] for a in range(ng)]),-np.einsum('abc,cij->abij',h,tau))
    for sample in range(2):
        label=f'SU({n}) x U(1), sample {sample}'
        v=rng.normal(size=ns);chi=rng.normal(size=ns)*.2
        F=np.einsum('aij,j->ai',tau,v)
        S,sv,R=np.linalg.svd(F,full_matrices=True)
        rank=int(np.sum(sv>1e-10));Sigma=np.zeros_like(F)
        np.fill_diagonal(Sigma,sv)
        H=1.4*np.outer(v,v);Q=F.T@F
        tnew=np.einsum('ba,ij,bjk,kl->ail',S,R,tau,R.T)
        hnew=np.einsum('da,eb,fc,def->abc',S,S,S,h)
        check(label+' mass decomposition',S@Sigma@R,F)
        check(label+' scalar/vector ranks',rank,2*n-1)
        check(label+' Hessian kernel',H@F.T,np.zeros((ns,ng)))
        check(label+' commuting masses',H@Q,np.zeros((ns,ns)))
        check(label+' rotated algebra',np.array([[tnew[a]@tnew[b]-tnew[b]@tnew[a] for b in range(ng)] for a in range(ng)]),-np.einsum('abc,cij->abij',hnew,tnew))
        A=rng.normal(size=ng);dphi=rng.normal(size=ns)
        D=dphi-np.einsum('a,aij,j->i',A,tau,v+chi)
        Dnew=R@dphi-np.einsum('a,ai->i',S.T@A,Sigma)-np.einsum('a,aij,j->i',S.T@A,tnew,R@chi)
        check(label+' rotated derivative',Dnew,R@D)
        varphi=(v[:n]+chi[:n]+1j*(v[n:]+chi[n:]))/np.sqrt(2)
        dvarphi=(dphi[:n]+1j*dphi[n:])/np.sqrt(2)
        complexD=dvarphi-1j*np.einsum('a,a,aij,j->i',couplings,A,ts,varphi)
        check(label+' complex and real kinetic',np.vdot(complexD,complexD),.5*D@D)
        scalar_ghost=np.einsum('aj,bjk,k->ab',F,tau,chi)
        check(label+' rotated ghost scalar',S.T@scalar_ghost@S,np.einsum('aj,bjk,k->ab',Sigma,tnew,R@chi))
        for xi in [.4,2.7]:
            theta=rng.normal(size=ng);t=np.einsum('a,aij->ij',theta,tau)
            eig,U=np.linalg.eigh(1j*t)
            def rotate(eps): return (U@np.diag(np.exp(1j*eps*eig))@U.conj().T@(v+chi)).real-v
            step=1e-5
            variation=-xi*F@(rotate(step)-rotate(-step))/(2*step)
            check(label+f' finite FP xi={xi}',variation,xi*(F@F.T+scalar_ghost)@theta,tol=2e-8)
        for family in ['Ass','AAs','AAss']:
            p=rng.normal(size=4);q=rng.normal(size=4)
            u=rng.normal(size=4);w=rng.normal(size=4)
            a=rng.normal(size=ng);b=rng.normal(size=ng)
            x=rng.normal(size=ns);y=rng.normal(size=ns)
            ta=np.einsum('a,aij->ij',a,tau);tb=np.einsum('a,aij->ij',b,tau)
            if family=='Ass':
                legs=[('A',a,-p-q,u),('s',x,p,None),('s',y,q,None)]
                expected=x@ta@y*np.dot(metric*u,q-p)
            elif family=='AAs':
                legs=[('A',a,p,u),('A',b,q,w),('s',x,-p-q,None)]
                expected=-1j*np.dot(metric*u,w)*((ta@v)@tb@x+(tb@v)@ta@x)
            else:
                r=rng.normal(size=4)
                legs=[('A',a,p,u),('A',b,q,w),('s',x,r,None),('s',y,-p-q-r,None)]
                expected=1j*np.dot(metric*u,w)*(x@(ta@tb+tb@ta)@y)
            check(label+' direct kinetic '+family,kinetic_vertex(tau,v,legs),expected)

helper=Path(__file__).with_name('check_background78.py')
result=dict(checks=len(records),passed=all(r['passed'] for r in records),records=records,
            script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),helper_sha256=sha256(helper.read_bytes()).hexdigest())
(ROOT/'checks/srednicki/mass-basis86-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(checks=len(records),passed=result['passed'],max_scaled_residual=max(r['scaled_residual'] for r in records),failures=[r for r in records if not r['passed']]),indent=2))
raise SystemExit(0 if result['passed'] else 1)
