#!/usr/bin/env python3
"""Check the tree cross section by integrating the three-channel amplitude.

Uses only the Python standard library. Units m=g=1 remove an overall g^4/m^6.
The quadrature receives the amplitude, independently of its integrated formula.
"""
import json
import math
from pathlib import Path


def integrate(f, a, b, tol=1e-11):
    def rec(a, b, fa, fc, fb, whole, eps, depth):
        c = (a + b) / 2
        d, e = (a + c) / 2, (c + b) / 2
        fd, fe = f(d), f(e)
        left = (c-a)*(fa+4*fd+fc)/6
        right = (b-c)*(fc+4*fe+fb)/6
        delta = left+right-whole
        if abs(delta) <= 15*eps:
            return left+right+delta/15
        if depth == 0:
            raise RuntimeError('Quadrature did not converge')
        return rec(a,c,fa,fd,fc,left,eps/2,depth-1)+rec(c,b,fc,fe,fb,right,eps/2,depth-1)
    fa, fc, fb = f(a), f((a+b)/2), f(b)
    return rec(a,b,fa,fc,fb,(b-a)*(fa+4*fc+fb)/6,tol,45)


def closed(s):
    d = s-4
    bracket = 2*d/(s-3)+d/(s-1)**2+4*math.log1p(d)/((s-1)*(s-2))
    return bracket/(32*math.pi*s*d)


def quadrature(s):
    # Symmetry around z=(s-2)/2 avoids a second narrow endpoint layer.
    def f(w):
        z=math.exp(w)
        amplitude = 1/(1-s)+1/z+1/(s-2-z)
        return z*amplitude**2
    return 2*integrate(f,0,math.log((s-2)/2))/(32*math.pi*s*(s-4))


rows=[]
for s in (4.0001,4.01,5,10,100,1000,1e6):
    numeric, formula = quadrature(s), closed(s)
    error=abs(numeric/formula-1)
    assert error < 1e-8, (s,error)
    rows.append({'s_over_m2':s,'quadrature':numeric,'closed_form':formula,'relative_error':error})
nr_limit=25/(1152*math.pi)
d=1e-5
nr_coefficient=(1-closed(4+d)/nr_limit)/d
s=1e7
ur_coefficient=(closed(s)*16*math.pi*s*s-1)*s
assert abs(nr_coefficient-79/60)<3e-5
assert abs(ur_coefficient-3.5)<1e-4
result={'scope':'Scalar tree amplitude angular integral, identical final-state factor 1/2, and first low/high-energy corrections','passed':True,'cases':rows,'nr_first_coefficient':nr_coefficient,'ur_first_coefficient':ur_coefficient}
Path('checks/srednicki/cross-section11-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
