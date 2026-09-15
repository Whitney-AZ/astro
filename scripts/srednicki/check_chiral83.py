"""Finite field-algebra and flavor-matrix checks for section 83."""
from pathlib import Path
from hashlib import sha256
from itertools import product
from math import factorial
import json
import numpy as np
from check_background78 import Poly, METRIC, dot
from check_helicity60 import PAULI, GAMMA

ROOT=Path(__file__).resolve().parents[2]
records=[]


def check(name, actual, expected, tol=2e-10):
    residual=float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))
    scale=max(1.,float(np.max(np.abs(expected))))
    records.append(dict(name=name,residual=residual,scaled_residual=residual/scale,
                        passed=residual<tol*scale))


def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(2)), Poly())
             for j in range(2)] for i in range(2)]


def exponential(Pi, sign):
    power=[[Poly({0:complex(i==j)}) for j in range(2)] for i in range(2)]
    out=[[Poly(x) for x in row] for row in power]
    for n in range(1,5):
        power=mm(power,Pi)
        for i,j in product(range(2),repeat=2):
            out[i][j]+=(sign*2j)**n/factorial(n)*power[i][j]
    return out


def action_vertex(colors, k, mass2, f=2.):
    Pi=[[Poly() for j in range(2)] for i in range(2)]
    for tag,color in enumerate(colors):
        for i,j in product(range(2),repeat=2):
            Pi[i][j]+=Poly({1<<tag:complex(PAULI[color][i,j]/(2*f))})
    U=exponential(Pi,1)
    Ud=exponential(Pi,-1)
    def deriv(A,mu):
        return [[Poly({mask:-1j*METRIC[mu]*
                       sum(k[tag][mu] for tag in range(4) if mask&(1<<tag))*v
                       for mask,v in A[i][j].items()})
                 for j in range(2)] for i in range(2)]
    # m=1 and v^3=mass2*f^2/4 impose m_pi^2=4mv^3/f^2.
    density=mass2*f*f/4*sum((U[i][i]+Ud[i][i] for i in range(2)),Poly())
    for mu in range(4):
        term=mm(deriv(Ud,mu),deriv(U,mu))
        density+=(-f*f/4*METRIC[mu])*sum((term[i][i] for i in range(2)),Poly())
    return 1j*density.get(15,0)


points=[
    ("massive",3., [(-5.,0.,0.,-4.),(-5.,0.,0.,4.),
                    (5.,2.4,3.2,0.),(5.,-2.4,-3.2,0.)]),
    ("massless",0., [(-5.,0.,0.,-5.),(-5.,0.,0.,5.),
                     (5.,3.,0.,4.),(5.,-3.,0.,-4.)]),
    ("off shell",2., [(3.,1.,2.,-1.),(-2.,-3.,0.,2.),
                      (1.,2.,-4.,1.),(-2.,0.,2.,-2.)]),
]
for name,m,k in points:
    check(name+" momentum",np.sum(k,axis=0),np.zeros(4))
    invariants=[-dot(np.add(k[0],k[j]),np.add(k[0],k[j])) for j in [1,2,3]]
    common=(sum(dot(q,q) for q in k)+m*m)/3
    for colors in product(range(3),repeat=4):
        a,b,c,d=colors
        pairing=[(a==b)*(c==d),(a==c)*(b==d),(a==d)*(b==c)]
        expected=1j/4*sum(delta*(channel+common)
                          for delta,channel in zip(pairing,invariants))
        check(name+" flavors "+str(colors),action_vertex(colors,k,m*m),expected)


def su2(vector):
    H=sum((v*s/2 for v,s in zip(vector,PAULI)),np.zeros((2,2),complex))
    vals,vecs=np.linalg.eigh(H)
    return (vecs*np.exp(1j*vals))@vecs.conj().T


I2=np.eye(2);I4=np.eye(4)
g5=np.diag([-1.,-1.,1.,1.])
PL=(I4-g5)/2;PR=(I4+g5)/2
gamma0=np.kron(I2,GAMMA[0])
def chiral(left,right):
    return np.kron(left,PL)+np.kron(right,PR)


for j in range(1,4):
    u=su2([.3*j,-.7,.2]);u0=su2([-.4,.1*j,.6])
    M=np.array([[1+.1j*j,.2-.3j],[.4+.2j,2-.2j*j]])
    for shifted in [False,True]:
        label=f"matrix {j} shifted={shifted}"
        if shifted:
            U=u0@u@u@u0
            B=chiral(u0@u,u0.conj().T@u.conj().T)
            C=u@u0@M@u0@u
        else:
            U=u@u
            B=chiral(u,u.conj().T)
            C=u@M@u
        Bbar=gamma0@B.conj().T@gamma0
        Md=M.conj().T;Ud=U.conj().T;Cd=C.conj().T
        check(label+" mass block 1",Bbar@chiral(M,Md)@B,chiral(C,Cd))
        check(label+" mass block 2",Bbar@chiral(Ud@Md@Ud,U@M@U)@B,chiral(Cd,C))
        check(label+" invariant mass",Bbar@chiral(Ud,U)@B,np.eye(8))
        check(label+" pseudoscalar block",Bbar@chiral(Ud,-U)@B,-np.kron(I2,g5))
        check(label+" trace",np.trace(M@U),np.trace(C))
        coeff=[.4,-.7,.2,.3]
        c1,c2,c3,c4=coeff
        original=(-c1*chiral(M,Md)-c2*chiral(Ud@Md@Ud,U@M@U)
                  -c3*np.trace(M@U+Md@Ud)*chiral(Ud,U)
                  -c4*np.trace(M@U-Md@Ud)*chiral(Ud,-U))
        new=(-(c1+c2)/2*np.kron(C+Cd,I4)
             +(c1-c2)/2*np.kron(C-Cd,g5)
             -c3*np.trace(C+Cd)*np.eye(8)
             +c4*np.trace(C-Cd)*np.kron(I2,g5))
        check(label+" full mass",Bbar@original@B,new)
        check(label+" Dirac hermiticity",gamma0@new.conj().T@gamma0,new)

# Independent diagonalization of the full neutral quadratic form.
for mu,md,ms in [(.0017,.0039,.076),(.002,.002,.09),(.003,.001,.05)]:
    B0=2.7;S=mu+md;delta=mu-md;Q=2*ms-S
    matrix=B0*np.array([[S,delta/np.sqrt(3)],[delta/np.sqrt(3),(S+4*ms)/3]])
    angle=.5*np.arctan(np.sqrt(3)*delta/Q)
    O=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
    roots=B0/3*np.array([2*(S+ms)-np.sqrt(Q*Q+3*delta*delta),
                        2*(S+ms)+np.sqrt(Q*Q+3*delta*delta)])
    check(f"neutral eigenvalues {mu,md,ms}",np.linalg.eigvalsh(matrix),roots)
    check(f"neutral rotation {mu,md,ms}",O@matrix@O.T,np.diag(roots))

P=.135**2;DEM=.140**2-P;Kp=.494**2-2*DEM;K0=.498**2
Bq=np.linalg.solve([[1,1,0],[1,0,1],[0,1,1]],[P,Kp,K0])
check("three flavor fit",Bq,[.0057535,.0124715,.2355325])
r=Bq[0]/Bq[1]; deltaN=.001293
fit=dict(B0mq=Bq.tolist(),mu_over_md=r,ms_over_md=Bq[2]/Bq[1],
         eta_mass=float(np.sqrt((P+4*Bq[2])/3)),
         cplus_mu_MeV=1000*deltaN*r/(1-r),
         cplus_md_MeV=1000*deltaN/(1-r),
         cplus_sum_MeV=1000*deltaN*(1+r)/(1-r),
         cplus_over_B0=deltaN/(K0-Kp))
result=dict(checks=len(records),passed=all(x['passed'] for x in records),
            max_scaled_residual=max(x['scaled_residual'] for x in records),
            records=records,fit=fit,
            script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'checks/srednicki/chiral83-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
print("Failures:",[x for x in records if not x['passed']])
raise SystemExit(0 if result['passed'] else 1)
