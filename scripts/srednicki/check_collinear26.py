# Reproduces the numerical comparison explicitly quoted in section 26.
# Source: Srednicki-QFT-Trans/checks/check_s26_collinear.py; original left unchanged.
import json,math,sys,platform,warnings,hashlib
import numpy as np
import scipy
from scipy.integrate import quad, IntegrationWarning

K=1.0
g=0.6
alpha=g*g/(4*math.pi)**3
Omega4=2*math.pi**2
prefactor=g*g*Omega4/(4*(2*math.pi)**5)
c=4/3-math.sqrt(3)*math.pi
calls={"outer":0,"inner":0}
errors={"outer_max":0.0,"inner_max":0.0}
def quadrature(fun,a,b,kind):
    out=quad(fun,a,b,epsabs=2e-10,epsrel=3e-8,limit=160,full_output=1)
    if len(out)!=3:
        raise RuntimeError({"kind":kind,"interval":[a,b],"quad_output":str(out)})
    val,err,info=out
    calls[kind]+=info["neval"]
    errors[kind+"_max"]=max(errors[kind+"_max"],err)
    return val

def sinc(t):
    if abs(t)<1e-5:
        return 1-t*t/6+t**4/120
    return math.sin(t)/t

def f(x):
    return (1-x+x*x)/(x*x*(1-x)**2)

def angular_approx(x,m,delta):
    if x<=0 or x>=1:
        return 0.0
    r=delta*delta/((m/K)**2*f(x))
    if r<1e-5:
        a=r*r/2-2*r**3/3+3*r**4/4
    else:
        a=math.log1p(r)-r/(1+r)
    return x*(1-x)*a/2

def exact_angle(x,m,delta):
    if x<=0 or x>=1:
        return 0.0
    a=(m/K)**2*f(x)
    umax=math.log1p(delta*delta/a)
    omega=math.hypot(K,m)
    def integrand(u):
        if u==0:
            return 0.0
        theta=math.sqrt(a*math.expm1(u))
        r1=K*(1-x)*sinc((1-x)*theta)/sinc(theta)
        r2=K*x*sinc(x*theta)/sinc(theta)
        omega1=math.hypot(r1,m)
        omega2=math.hypot(r2,m)
        jac=K*x*sinc(x*theta)/(sinc(theta)**2)
        energy_difference=(m*m*(r1*r1+r2*r2)+m**4)/(omega1*omega2+r1*r2)
        den=-m*m-2*energy_difference-4*r1*r2*math.sin(theta/2)**2
        dtheta_du=a*math.exp(u)/(2*theta)
        return (omega*r1**4*math.sin(x*theta)**3*jac
                /(omega1*omega2*den*den))*dtheta_du
    return quadrature(integrand,0,umax,"inner")

rows=[]
captured=[]
with warnings.catch_warnings(record=True) as ws:
    warnings.simplefilter("always")
    for delta,rho in [(0.1,1e-3),(0.03,1e-3),(0.03,1e-4)]:
        m=K*delta*rho
        cuts=sorted(set([0.0,rho,0.01,0.1,0.5]))
        approximate=2*sum(quadrature(lambda x:angular_approx(x,m,delta),a,b,"outer")
                          for a,b in zip(cuts,cuts[1:]))
        exact=2*sum(quadrature(lambda x:exact_angle(x,m,delta),a,b,"outer")
                    for a,b in zip(cuts,cuts[1:]))
        leading=(math.log((delta*K/m)**2)+c)/12
        ceff=12*approximate-math.log((delta*K/m)**2)
        tolerance=2*delta*delta+5e-7
        assert abs(exact-approximate)<tolerance
        assert abs(ceff-c)<0.003
        assert abs(2*approximate-exact)>20*tolerance
        assert abs((approximate+1/12)-exact)>3*tolerance
        rows.append({"K":K,"g":g,"delta":delta,"rho_m_over_Kdelta":rho,"m":m,
                     "exact_massive_geometric_integral":exact,
                     "leading_collinear_exact_angular_integral":approximate,
                     "mass_asymptotic_formula":leading,
                     "geometry_minus_collinear":exact-approximate,
                     "finite_mass_c_effective":ceff,
                     "c_exact":c,
                     "probability_exact_geometric":prefactor*exact,
                     "probability_leading_formula":alpha*leading,
                     "comparison_tolerance":tolerance})
    captured=[str(w.message) for w in ws]
assert not captured
print(json.dumps({"python":sys.version.split()[0],"platform":platform.platform(),
                  "numpy":np.__version__,"scipy":scipy.__version__,
                  "assumptions":"K=1, g=.6, all masses m; positive daughter energies; exact sine geometry and same spatial cluster K; factor1/2 for unordered daughters; angular cone theta<delta. Only local splitting phase weight checked, not exact full event energy delta or incoming preparation.",
                  "integration":"u=ln(1+theta^2/a(x)), a=(m/K)^2 f(x); x symmetry and cuts 0,rho,.01,.1,.5. quad epsabs=2e-10 epsrel=3e-8 limit=160.",
                  "prefactor":prefactor,"alpha":alpha,"cases":rows,
                  "quadrature_neval":calls,"largest_reported_local_errors":errors,
                  "warnings":captured,"tests":"all assertions passed; missing identical1/2 and missing angular -1/2 finite term detected at all three points"},ensure_ascii=False,indent=2))
