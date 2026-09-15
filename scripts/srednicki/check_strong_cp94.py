"""Ordered mass operators, on-shell EDM spinors, radial logs and axion mixing."""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
import json
import numpy as np
from check_helicity60 import GAMMA, PAULI, slash

ROOT = Path(__file__).resolve().parents[2]
rng = np.random.default_rng(940915)
g5 = np.diag([-1., -1., 1., 1.])
I4, I2 = np.eye(4), np.eye(2)
PL, PR = (I4-g5)/2, (I4+g5)/2
metric = np.array([-1., 1., 1., 1.])
e4 = np.zeros((4, 4, 4, 4))
for p in permutations(range(4)):
    e4[p] = (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))
S = np.array([[.25j*(a@b-b@a) for b in GAMMA] for a in GAMMA])
records = []


def check(name, actual, expected, tol=5e-11):
    err = float(np.max(np.abs(np.asarray(actual)-expected)))
    scale = max(1., float(np.max(np.abs(expected))))
    records.append(dict(name=name, scaled_residual=err/scale, tolerance=tol, passed=err < tol*scale))


def su2(v):
    r = np.linalg.norm(v)
    return np.cos(r)*I2+1j*np.sinc(r/np.pi)*np.einsum('a,aij->ij', v, PAULI)


def block(L, R):
    return np.kron(L, PL)+np.kron(R, PR)


def aligned(theta, masses):
    mu, md = masses
    angle = np.arctan2((mu-md)*np.sin(theta/2), (mu+md)*np.cos(theta/2))
    u0 = np.diag(np.exp(.5j*angle*np.array([1., -1.])))
    M = np.diag(masses)*np.exp(-.5j*theta)
    return M, u0


def mass_operators(theta, masses, u, coeff):
    M, u0 = aligned(theta, masses)
    U = u0@u@u@u0
    B = block(u0@u, u0.conj().T@u.conj().T)
    gb = np.kron(I2, GAMMA[0])
    Bb = gb@B.conj().T@gb
    plus, minus = block(U.conj().T, U), block(U.conj().T, -U)
    trp = np.trace(M@U+M.conj().T@U.conj().T)
    trm = np.trace(M@U-M.conj().T@U.conj().T)
    original = [-block(M, M.conj().T),
                -block(U.conj().T@M.conj().T@U.conj().T, U@M@U),
                -trp*plus, -trm*minus]
    transformed = [Bb@a@B for a in original]
    Q = M@u0@u0
    C = u@Q@u
    direct = [-block(C, C.conj().T), -block(C.conj().T, C),
              -trp*np.eye(8), trm*np.kron(I2, g5)]
    return transformed, direct, Bb@plus@B, sum(c*a for c, a in zip(coeff, transformed))


for sample in range(8):
    masses = .3+rng.random(2)
    theta = rng.uniform(-5, 5)
    M, u0 = aligned(theta, masses)
    U0 = u0@u0
    R = np.sqrt(masses@masses+2*np.prod(masses)*np.cos(theta))
    check(f'exact vacuum trace {sample}', np.trace(M@U0).real, R)
    # Unit quaternions independently sample the full group, including off-diagonal U.
    trials = np.array([su2(rng.normal(size=3)*3) for _ in range(30)])
    max_trial = max(np.trace(M@U).real for U in trials)
    check(f'vacuum dominates full group samples {sample}', float(max_trial <= R+1e-12), 1.)
    u = su2(rng.normal(size=3))
    coeff = rng.normal(size=4)
    transformed, direct, unitmass, _ = mass_operators(theta, masses, u, coeff)
    check(f'four raw ordered mass operators {sample}', transformed, np.array(direct))
    check(f'raw chiral-limit mass cancellation {sample}', unitmass, np.eye(8))
    step = 2e-5
    pos = mass_operators(step, masses, u, coeff)[3]
    neg = mass_operators(-step, masses, u, coeff)[3]
    Ut = u@u
    c1, c2, c3, c4 = coeff
    mt = np.prod(masses)/sum(masses)
    expected = -1j*mt*(-(c1+c2)/2*np.kron(Ut-Ut.conj().T, I4)
                      +(c1-c2)/2*np.kron(Ut+Ut.conj().T, g5)
                      +c4*np.trace(Ut+Ut.conj().T)*np.kron(I2, g5))
    check(f'CP derivative of original action {sample}', (pos-neg)/(2*step), expected, 3e-9)
    mass, delta = 1.4, rng.normal()
    alpha = .5*np.arctan2(delta, mass)
    rot = np.diag(np.exp(-1j*alpha*np.diag(g5)))
    check(f'exact pseudoscalar mass removal {sample}',
          rot@(mass*I4+1j*delta*g5)@rot, np.sqrt(mass*mass+delta*delta)*I4)
    check(f'vector and axial rotations {sample}',
          [rot@G@rot for G in list(GAMMA)+[G@g5 for G in GAMMA]],
          np.array(list(GAMMA)+[G@g5 for G in GAMMA]))

lowerS = S*metric[:, None, None, None]*metric[None, :, None, None]
check('all six dual-spin identities', np.einsum('mnij,jk->mnik', S, 1j*g5),
      -.5*np.einsum('mnrs,rsij->mnij', e4, lowerS))


def spinors(p, mass):
    values, vectors = np.linalg.eigh((-slash(p)+mass*I4)@GAMMA[0])
    keep = values > 1e-9
    return vectors[:, keep]*np.sqrt(values[keep])


for sample in range(6):
    mass = .7+.2*sample
    pv, ppv = rng.normal(size=(2, 3))
    p = np.r_[np.sqrt(mass*mass+pv@pv), pv]
    pp = np.r_[np.sqrt(mass*mass+ppv@ppv), ppv]
    q, pb = pp-p, (p+pp)/2
    u, up = spinors(p, mass), spinors(pp, mass)
    Bu = up.conj().T@GAMMA[0]
    pseudoscalar = Bu@g5@u
    check(f'complete spin basis axial divergence {sample}',
          Bu@slash(q)@g5@u, -2*mass*pseudoscalar)
    dipole = np.einsum('mnij,n,jk->mik', S, metric*q, 1j*g5)
    check(f'complete spin basis exact Gordon {sample}',
          [Bu@d@u for d in dipole], pb[:, None, None]*pseudoscalar)
    P = rng.normal(size=4)
    propagator = -slash(P)+mass*I4
    check(f'two open loop chains {sample}', propagator@g5+g5@propagator, 2*mass*g5)
    check(f'derivative-contact identity {sample}', slash(P-p)@g5,
          (slash(P)+mass*I4)@g5+g5@(slash(p)+mass*I4)-2*mass*g5)
    check(f'off-shell inverse propagator {sample}', propagator@(slash(P)+mass*I4),
          (P@(metric*P)+mass*mass)*I4)

nodes, weights = np.polynomial.legendre.leggauss(400)
y, w = (nodes+1)/2, weights/2
for ratio in [.3, 1., 8., 40.]:
    L = ratio*y
    raw = 2*np.dot(ratio*w, L**3/(L*L+1)**2)
    check(f'original radial cutoff integral ratio={ratio}', raw,
          np.log1p(ratio*ratio)+1/(ratio*ratio+1)-1)

# Full relativistic two-pseudoscalar-vertex graphs at q=0 give
# 2 M^2 int_0^1 x(1-x)/[M^2 x^2+(1-x)m_pi^2] dx after Feynman parametrization.
# Verify their log coefficient independently of the heavy-nucleon approximation.
for ratio in [1e-3, 1e-4, 1e-5, 1e-6]:
    cutoff = -np.log(ratio)+30
    x = np.exp(-cutoff*y)
    full = 2*np.dot(cutoff*w, x*x*(1-x)/(x*x+(1-x)*ratio**2))
    remainder = full+2*np.log(ratio)+2
    check(f'relativistic two-graph logarithm ratio={ratio}', remainder, 0., 15*ratio)

for mu, md in [(.4, .9), (1., 1.), (0., 1.), (1., 0.)]:
    v3, fp = 1.3, .8
    s, d = mu+md, mu-md
    for f in [2., 10., 100.]:
        H = v3*np.array([[s/(2*f*f), d/(f*fp)], [d/(f*fp), 2*s/(fp*fp)]])
        # Build the Hessian directly as sum of the two cosine quadratic forms.
        cu = np.array([1/(2*f), 1/fp])
        cd = np.array([1/(2*f), -1/fp])
        direct = 2*v3*(mu*np.outer(cu, cu)+md*np.outer(cd, cd))
        check(f'original two-cosine Hessian {mu,md,f}', H, direct)
        ev = np.linalg.eigvalsh(H)
        A, B, C = H[0, 0], H[0, 1], H[1, 1]
        heavy = .5*(A+C+np.sqrt((C-A)**2+4*B*B))
        light = (A*C-B*B)/heavy  # stable evaluation of the exact small root
        check(f'physical two-field masses {mu,md,f}', ev, [light, heavy])
        schur = A-B*B/C
        check(f'aligned potential curvature {mu,md,f}', schur, 2*v3*mu*md/(s*f*f))
        if mu*md == 0:
            check(f'massless flavor exact zero {mu,md,f}', ev[0], 0.)

coefficient = 1.27*1.7*.0012/(8*np.pi**2*.0924**2)*4.2
check('historical EDM rounding in GeV inverse', coefficient, .0161, 5e-5)
check('historical EDM rounding in cm', coefficient*1.97327e-14/1e-16, 3.2, .05/3.2)
result = dict(checks=len(records), all_passed=all(r["passed"] for r in records),
              max_scaled_residual=max(r["scaled_residual"] for r in records),
              max_algebraic_residual=max(r["scaled_residual"] for r in records if r["tolerance"] <= 3e-9),
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
              helper_sha256=sha256((Path(__file__).parent/"check_helicity60.py").read_bytes()).hexdigest(),
              records=records)
(ROOT/"checks/srednicki/strong-cp94-check.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k != "records"}, indent=2))
if not result["all_passed"]:
    print(json.dumps([r for r in records if not r["passed"]], indent=2))
    raise SystemExit(1)
