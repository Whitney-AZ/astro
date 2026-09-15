#!/usr/bin/env python3
"""Independent quadrature of the parameter and spectral integrals (m=alpha=1)."""
import json
import math
from pathlib import Path


def simpson(f,a=0.0,b=1.0,n=20000):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))+2*sum(f(a+i*h) for i in range(2,n,2)))


def parameter(u):
    def f(x):
        a=x*(1-x);d=1+u*a;d0=1-a
        logpart=0 if abs(d)<1e-15 else d*(complex(math.log(abs(d)/d0),-math.pi if d<0 else 0))
        return (logpart-a*(u+1))/2
    points=[0.0,1.0]
    if u < -4:
        beta=math.sqrt(1+4/u);points=[0,(1-beta)/2,(1+beta)/2,1]
    return sum(simpson(f,a,b) for a,b in zip(points,points[1:]))


def closed(u):
    if u==0:
        return complex(11/12-math.pi*math.sqrt(3)/6)
    if u>0:
        r=math.sqrt(1+4/u);f=r**3*math.atanh(1/r)
    elif u>-4:
        h=math.sqrt(-1-4/u);f=-h**3*math.atan(1/h)
    elif u==-4:
        f=0
    else:
        r=math.sqrt(1+4/u);f=r**3*complex(math.atanh(r),-math.pi/2)
    return ((3-math.pi*math.sqrt(3))*u+(3-2*math.pi*math.sqrt(3))+2*u*f)/12


rows=[]
for u in (-100,-10,-4.1,-4,-3.9,-3,-1,-0.1,0,1,10,100):
    quad,formula=parameter(u),closed(u)
    error=abs(quad-formula)/max(1,abs(formula))
    assert error<2e-8,(u,error)
    row={'u':u,'parameter_integral':[quad.real,quad.imag],'closed':[formula.real,formula.imag],'scaled_error':error}
    if u>-4:
        spectral=simpson(lambda v:8*v**4/(3*(3+v*v)**2*(4+u*(1-v*v))))
        target=quad.real/(u+1)**2 if u!=-1 else simpson(lambda x:(x*(1-x))**2/(1-x*(1-x)))/4
        assert abs(spectral-target)<1e-10,(u,spectral,target)
        row['spectral_integral']=spectral
        row['spectral_error']=abs(spectral-target)
    rows.append(row)
step=1e-4
shell_derivative=(parameter(-1+step)-parameter(-1-step))/(2*step)
assert abs(parameter(-1))<1e-12 and abs(shell_derivative)<1e-9
result={'onshell_derivative_finite_difference':[shell_derivative.real,shell_derivative.imag],'passed':True,'scope':'One-loop self energy: parameter integral, all three real-axis branches, two on-shell zeros, and reconstructed spectral integral','cases':rows}
Path('checks/srednicki/self-energy14-15-check.json').write_text(json.dumps(result,indent=2)+'\n')
print('Passed 12 self-energy points and 8 spectral integral comparisons.')
