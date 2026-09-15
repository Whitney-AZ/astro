"""Original Cartesian field strengths, radial energy squares and finite BPS integrals."""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
rng=np.random.default_rng(920915)
records=[]
eps=np.zeros((3,3,3))
for p in permutations(range(3)):
    eps[p]=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))


def check(name, actual, expected, tol=3e-11):
    err=float(np.max(np.abs(np.asarray(actual)-expected)))
    scale=max(1.,float(np.max(np.abs(expected))))
    records.append(dict(name=name,scaled_residual=err/scale,passed=err<tol*scale))


for sample in range(12):
    x=rng.normal(size=3);r=np.linalg.norm(x);n=x/r
    e,v=.7,1.3
    a,ar,f,fr=rng.normal(size=4)
    P=np.eye(3)-np.outer(n,n);Q=np.outer(n,n)
    A=a/(e*r)*np.einsum('aij,j->ia',eps,n)  # i,a
    dA=np.empty((3,3,3))  # derivative j, potential k, internal a
    for j in range(3):
        for k in range(3):
            for aa in range(3):
                dA[j,k,aa]=sum(eps[aa,k,l]*(ar*n[j]*x[l]/r**2+
                                    a*((j==l)/r**2-2*x[l]*x[j]/r**4))/e for l in range(3))
    F=np.array([[dA[j,k]-dA[k,j]+e*np.cross(A[j],A[k]) for k in range(3)] for j in range(3)])
    B=.5*np.einsum('ijk,jka->ia',eps,F)
    expectedB=-(ar*P/r+(2*a-a*a)*Q/r**2)/e
    check(f'Cartesian nonabelian B {sample}',B,expectedB)
    phi=v*f*n
    D=np.array([v*(fr*n[i]*n+f*P[i]/r)+e*np.cross(A[i],phi) for i in range(3)])
    expectedD=v*((1-a)*f*P/r+fr*Q)
    check(f'Cartesian covariant gradient {sample}',D,expectedD)
    density=np.sum(B*B)/2+np.sum(D*D)/2
    expected=(2*r*r*ar*ar+(2*a-a*a)**2)/(2*e*e*r**4)+v*v*(2*(1-a)**2*f*f+r*r*fr*fr)/(2*r*r)
    check(f'full Cartesian kinetic energy {sample}',density,expected)
    # General normalized-Higgs jets test the gauge-invariant electromagnetic tensor.
    dn=P@rng.normal(size=(3,2))
    A0,A1=rng.normal(size=(2,3));curl=rng.normal(size=3)
    full=n@(curl+e*np.cross(A0,A1))-n@np.cross(dn[:,0]+e*np.cross(A0,n),dn[:,1]+e*np.cross(A1,n))/e
    ordinary=n@curl+dn[:,0]@A1-dn[:,1]@A0-n@np.cross(dn[:,0],dn[:,1])/e
    check(f'electromagnetic tensor expansion {sample}',full,ordinary)
    rho=.3+abs(rng.normal());k=1+sample%3
    original=rho*(fr*fr+k*k*(1-a)**2*f*f/rho**2+
                   .5*(1-f*f)**2+k*k*ar*ar/(2*rho*rho))
    squares=rho*((fr-k*(1-a)*f/rho)**2+
                 k*k/(2*rho*rho)*(ar-rho*(1-f*f)/k)**2)
    boundary=k*(ar*(1-f*f)+2*(1-a)*f*fr)
    check(f'vortex radial Bogomolny identity {sample}',original,squares+boundary)

nodes,weights=np.polynomial.legendre.leggauss(400)
weights=weights/2;y=(nodes+1)/2
trial=[]
for beta2,c in [(1.5,np.sqrt(3)/4),(2.,.5),(5.,.9)]:
    # Integrate each term of the original rho energy after rho=sqrt(x/c).
    x=50*y;wx=50*weights;rho=np.sqrt(x/c);jac=1/(2*c*rho)
    f=np.sqrt(-np.expm1(-x));a=-np.expm1(-x)
    fp=c*rho*np.exp(-x)/f;ap=2*c*rho*np.exp(-x)
    terms=[rho*fp*fp,(1-a)**2*f*f/rho,ap*ap/(2*rho),
           beta2*rho*(1-f*f)**2/4]
    integrals=[float(np.dot(wx,jac*t)) for t in terms]
    expected=[.5*(np.pi**2/6-1),.5*np.log(1.5),c/2,beta2/(16*c)]
    check(f'four independent trial energy integrals {beta2,c}',integrals,expected)
    trial.append(dict(beta_squared=beta2,c=c,energy_over_2pi_v2=sum(integrals)))
check('strict trial counterexample',float(trial[0]['energy_over_2pi_v2']<47/48),1.)


def bps(rho):
    sh,ch=np.sinh(rho),np.cosh(rho)
    a=1-rho/sh;f=ch/sh-1/rho
    ap=rho*ch/sh**2-1/sh;fp=1/rho**2-1/sh**2
    app=2*ch/sh**2-rho/sh-2*rho/sh**3
    fpp=-2/rho**3+2*ch/sh**3
    return a,f,ap,fp,app,fpp


for rho in [.05,.2,.7,2.,7.,20.]:
    a,f,ap,fp,app,fpp=bps(rho)
    check(f'BPS first-order equations {rho}',[ap,fp],[(1-a)*f,(2*a-a*a)/rho**2])
    check(f'BPS second-order equations {rho}',[app,fpp+2*fp/rho],
          [(1-a)*((2*a-a*a)/rho**2-f*f),2*(1-a)**2*f/rho**2])
for R in [1.,4.,10.,40.]:
    r=R*y;a,f,ap,fp,_,_=bps(r)
    # Sum all four original energy terms, not the boundary derivative.
    integrand=ap**2+(2*a-a*a)**2/(2*r*r)+(1-a)**2*f*f+r*r*fp*fp/2
    integral=float(np.dot(R*weights,integrand))
    ae,fe,*_=bps(R)
    check(f'finite-radius BPS energy R={R}',integral,fe*(2*ae-ae*ae))

for speed in [0.,.3,-.7]:
    v,m=1.4,.8
    z=40*y-20;psi=v*np.tanh(m*z/2);dp=v*m/2/np.cosh(m*z/2)**2
    potential=m*m*(psi*psi-v*v)**2/(8*v*v)
    gamma=1/np.sqrt(1-speed*speed)
    energy=float(np.dot(40*weights,((gamma*speed*dp)**2+(gamma*dp)**2)/2+potential))/gamma
    momentum=float(np.dot(40*weights,gamma*speed*dp*dp))
    mass=2*m*v*v/3
    check(f'boosted kink energy and momentum {speed}',[energy,momentum],[gamma*mass,gamma*speed*mass],tol=1e-12)
for N in [-3,-1,0,1,4]:
    theta=np.pi*y
    integrand=N*np.sin(theta)
    degree=float(np.dot(np.pi*weights,integrand))/2
    check(f'oriented sphere degree {N}',degree,N)

result=dict(checks=len(records),passed=all(r['passed'] for r in records),records=records,trial=trial,
            script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'checks/srednicki/solitons92-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(checks=len(records),passed=result['passed'],trial=trial,
                     max_scaled_residual=max(r['scaled_residual'] for r in records),
                     failures=[r for r in records if not r['passed']]),indent=2))
raise SystemExit(0 if result['passed'] else 1)
