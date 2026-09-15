"""Finite massive triangle traces, polarized beta decay and phase-space integrals."""
from pathlib import Path
from hashlib import sha256
from itertools import permutations, product
from decimal import Decimal, localcontext
import json
import numpy as np
from check_helicity60 import GAMMA, PAULI, slash

ROOT = Path(__file__).resolve().parents[2]
rng = np.random.default_rng(900915)
eta = np.diag([-1., 1., 1., 1.])
metric = np.diag(eta)
g5 = np.diag([-1., -1., 1., 1.])
eye = np.eye(4)
eps = np.zeros((4, 4, 4, 4))
for p in permutations(range(4)):
    eps[p] = (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))
records = []


def check(name, actual, expected, tol=3e-11):
    err = float(np.max(np.abs(np.asarray(actual)-expected)))
    scale = max(1., float(np.max(np.abs(expected))))
    records.append(dict(name=name, scaled_residual=err/scale, passed=err < tol*scale))


def bar(u): return u.conj()@GAMMA[0]


def spinors(p, mass, sign=1):
    values, vectors = np.linalg.eigh((-slash(p)+sign*mass*eye)@GAMMA[0])
    keep = values > 1e-9
    return vectors[:, keep]*np.sqrt(values[keep])


for sample in range(7):
    p, q, ell = rng.normal(size=(3, 4))
    mass = .5+.3*sample
    a, b, c = ell-p, ell, ell+q
    N = lambda v: -slash(v)+mass*eye
    Q = lambda v: slash(v)+mass*eye
    expected = 4j*mass*np.einsum('mnab,a,b->mn', eps, eta@p, eta@q)
    raw = np.array([[np.trace(N(a)@GAMMA[mu]@N(b)@GAMMA[nu]@N(c)@g5)
                     for nu in range(4)] for mu in range(4)])
    check(f'full pseudoscalar numerator {sample}', raw, expected)
    check(f'massive axial vertex identity {sample}', slash(a-c)@g5,
          -Q(c)@g5-g5@Q(a)+2*mass*g5)
    check(f'first vector Ward numerator {sample}', (eta@p)@raw, np.zeros(4))
    check(f'second vector Ward numerator {sample}', raw@(eta@q), np.zeros(4))

mn, mp, me = 8., 7., .3
for sample in range(7):
    chi = rng.normal(size=2)+1j*rng.normal(size=2)
    chi /= np.linalg.norm(chi)
    S = np.array([np.vdot(chi, sigma@chi).real for sigma in PAULI])
    un = np.sqrt(mn)*np.r_[chi, chi]
    up = np.sqrt(mp)*np.vstack([np.eye(2), np.eye(2)])
    p3, q3 = rng.normal(size=(2, 3))
    p = np.r_[np.sqrt(me*me+p3@p3), p3]
    q = np.r_[np.linalg.norm(q3), q3]
    ue, vn = spinors(p, me), spinors(q, 0., -1)
    z = np.r_[0., S]
    check(f'pure polarized density {sample}', np.outer(un, bar(un)),
          .5*(eye-g5@slash(z))@(-slash(np.array([mn, 0., 0., 0.]))+mn*eye))
    for gA in [-1.27, 0., 1., 1.27]:
        total = 0.
        for ip, ie, inu in product(range(2), repeat=3):
            amplitude = sum(metric[mu]*(bar(up[:, ip])@GAMMA[mu]@(eye-gA*g5)@un)*
                            (bar(ue[:, ie])@GAMMA[mu]@(eye-g5)@vn[:, inu])
                            for mu in range(4))/np.sqrt(2)
            total += abs(amplitude)**2
        d = 1+3*gA*gA
        expected = 16*mn*mp*(d*p[0]*q[0]+(1-gA*gA)*(p3@q3)+
                             2*gA*(1-gA)*q[0]*(S@p3)+2*gA*(1+gA)*p[0]*(S@q3))
        check(f'explicit polarized beta spin sum {sample,gA}', total, expected)

nodes, weights = np.polynomial.legendre.leggauss(350)
x, weights = (nodes+1)/2, weights/2


def smooth_I(delta, m):
    Q = delta-m
    return 2*Q**3.5*float(np.dot(weights, (m+Q*x*x)*x*x*np.sqrt(2*m+Q*x*x)*(1-x*x)**2))


def decimal_I(delta, m):
    with localcontext() as ctx:
        ctx.prec = 70
        # Compare identical binary inputs; near threshold decimal re-rounding
        # would change Q itself by a relatively significant amount.
        d, mass = Decimal.from_float(delta), Decimal.from_float(m)
        if mass == 0: return float(d**5/30)
        p = (d*d-mass*mass).sqrt()
        return float(p*(2*d**4-9*d*d*mass*mass-8*mass**4)/60+
                     d*mass**4*((d+p)/mass).ln()/4)


for delta, m in [(1., 0.), (1., .2), (1., .9), (1., .999999),
                 (.001293, .000511), (.004594, .000511)]:
    exact = decimal_I(delta, m)
    check(f'phase integral relative {delta,m}', smooth_I(delta, m)/exact, 1.)

triangle = []
for tau in [0., .0001, .02, .2, .7, .99]:
    # Map y=(1-x)t, integrating the original Feynman triangle.
    y = (1-x[:, None])*x[None, :]
    F = float(np.einsum('i,j,ij->', weights, weights,
                        2*(1-x[:, None])/(1-4*tau*x[:, None]*y)))
    exact = np.arcsin(np.sqrt(tau))**2/tau if tau else 1.
    check(f'massive triangle parameter integral tau={tau}', F, exact)
    triangle.append(dict(tau=tau, integral=F, analytic=exact))

hbar = 6.62607015e-34/(2*np.pi*1.602176634e-10)
GF, c1, tau_n, rate_pi = 1.166e-5, .974, 886., .397
In, Ipi = smooth_I(.001293, .000511), smooth_I(.004594, .000511)
fit_c = np.sqrt(np.pi**3*hbar*rate_pi/(GF*GF*Ipi))
fit_g = np.sqrt((2*np.pi**3*hbar/(tau_n*GF*GF*c1*c1*In)-1)/3)
fit_joint = np.sqrt((2*Ipi/(tau_n*rate_pi*In)-1)/3)
width = (1/137.036)**2*.135**3/(64*np.pi**3*.0924**2)
for name, value, rounded in [('c1', fit_c, .963505), ('gA', fit_g, 1.326212),
                             ('joint gA', fit_joint, 1.343378),
                             ('neutral pion eV', width*1e9, 7.73319)]:
    check(f'printed rounding {name}', value, rounded, tol=1e-6)
for m in [.135, .7, 2.3]:
    k1, k2 = np.array([m/2, 0., 0., m/2]), np.array([m/2, 0., 0., -m/2])
    pol = [np.array([0., 1., 0., 0.]), np.array([0., 0., 1., 0.])]
    amp = lambda e1, e2: np.einsum('abcd,a,b,c,d', eps, eta@k1, eta@e1, eta@k2, eta@e2)
    check(f'photon polarization sum m={m}', sum(abs(amp(a,b))**2 for a in pol for b in pol), m**4/2)
    check(f'photon Ward m={m}', [amp(k1, b) for b in pol]+[amp(a, k2) for a in pol], np.zeros(4))

helper = Path(__file__).with_name('check_helicity60.py')
result = dict(checks=len(records), passed=all(r['passed'] for r in records), records=records,
              triangle=triangle, inputs=dict(hbar=hbar, In=In, Ipi=Ipi, c1=fit_c,
                                            gA=fit_g, joint_gA=fit_joint, neutral_width_eV=width*1e9),
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
              helper_sha256=sha256(helper.read_bytes()).hexdigest())
(ROOT/'checks/srednicki/hadrons90-check.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(dict(checks=len(records), passed=result['passed'], inputs=result['inputs'],
                      max_scaled_residual=max(r['scaled_residual'] for r in records),
                      failures=[r for r in records if not r['passed']]), indent=2))
raise SystemExit(0 if result['passed'] else 1)
