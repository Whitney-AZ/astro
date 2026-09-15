"""MSSM Higgs checks from the original two-doublet polynomial potential."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
rng = np.random.default_rng(960915)
records = []
sigma = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
g1, g2 = .36, .65
G, lam, kap = g1*g1+g2*g2, (g1*g1+g2*g2)/8, g2*g2/2


def check(name, actual, expected, tol=2e-9):
    err = float(np.max(np.abs(np.asarray(actual)-expected)))
    scale = max(1., float(np.max(np.abs(expected))))
    records.append(dict(name=name, scaled_residual=err/scale, passed=err < tol*scale))


def invariants(z):
    h, hb = z[:2], z[2:]
    return (np.vdot(h, h).real, np.vdot(hb, hb).real,
            np.vdot(h, hb), hb[0]*h[1]-hb[1]*h[0])


def potential(z, a, c, b):
    # Original moment maps; no use of the reduced quartic or target mass matrices.
    h, hb = z[:2], z[2:]
    J = np.array([np.vdot(h, s@h)+np.vdot(hb, s@hb) for s in sigma]).real
    Y = (-np.vdot(h, h)+np.vdot(hb, hb)).real/2
    I = hb[0]*h[1]-hb[1]*h[0]
    return (a*np.vdot(h, h).real+c*np.vdot(hb, hb).real
            +2*np.real(b*I)+g2*g2*np.dot(J, J)/8+g1*g1*Y*Y/2)


# Canonical real order h1,h2,a1,a2,c1,c2,d1,d2.
dirs = np.zeros((8, 4), complex)
for row, col, value in [(0, 0, 1), (1, 3, 1), (2, 0, 1j), (3, 3, 1j),
                         (4, 1, 1), (5, 2, 1), (6, 1, 1j), (7, 2, 1j)]:
    dirs[row, col] = value/np.sqrt(2)


def hessian(z, a, c, b, step):
    f = lambda q: potential(z+q, a, c, b)
    return np.array([[(f(step*(ei+ej))-f(step*(ei-ej))
                       -f(step*(-ei+ej))+f(-step*(ei+ej)))/(4*step*step)
                     for ej in dirs] for ei in dirs])


def gradient(z, a, c, b, step):
    return np.array([(potential(z+step*e, a, c, b)
                      -potential(z-step*e, a, c, b))/(2*step) for e in dirs])


def canonical(z):
    return np.sqrt(2)*np.array([z[0].real, z[3].real, z[0].imag, z[3].imag,
                                z[1].real, z[2].real, z[1].imag, z[2].imag])


generators = []
for s in sigma:
    t = np.zeros((4, 4), complex)
    t[:2, :2] = t[2:, 2:] = s/2
    generators.append(t)
generators.append(np.diag([-.5, -.5, .5, .5]))

for trial in range(12):
    z = rng.normal(size=4)+1j*rng.normal(size=4)
    a, c = rng.normal(size=2)
    b = rng.normal()+1j*rng.normal()
    x, y, inner, I = invariants(z)
    check(f'Gram determinant {trial}', abs(I)**2, x*y-abs(inner)**2)
    reduced = a*x+c*y+2*np.real(b*I)+lam*(x-y)**2+kap*abs(inner)**2
    check(f'Pauli quartic against raw moment maps {trial}', potential(z, a, c, b), reduced)
    direction = rng.normal(size=3)
    direction /= np.linalg.norm(direction)
    angle, phase = rng.normal(size=2)
    u = np.cos(angle)*np.eye(2)+1j*np.sin(angle)*np.einsum('a,aij->ij', direction, sigma)
    rotated = np.concatenate([np.exp(-.5j*phase)*u@z[:2], np.exp(.5j*phase)*u@z[2:]])
    check(f'Full finite SU2 and hypercharge invariance {trial}',
          potential(rotated, a, c, b), potential(z, a, c, b))
    # Complex symmetric Hessian of W_mu=mu*(H0*barH0-Hminus*barHplus).
    mu = .4+.7j
    W2 = np.zeros((4, 4), complex)
    W2[0, 3] = W2[3, 0] = mu
    W2[1, 2] = W2[2, 1] = -mu
    check(f'All four higgsino singular masses {trial}',
          np.linalg.svd(W2, compute_uv=False), np.full(4, abs(mu)))
    check(f'F potential from four holomorphic derivatives {trial}',
          np.linalg.norm(W2@z)**2, abs(mu)**2*(x+y))

vacua = [(A, beta, scale) for A in [.15, 1.7] for beta in [.25, .68, 1.15]
         for scale in [.8, 2.1]]
vacua += [(1.2, 0., 1.1), (.7, np.pi/2, 1.3)]
vacua += [(.6, np.pi/4, scale) for scale in [.8, 1.9]]
vacua += [(0., beta, scale) for beta in [0., .39, np.pi/4, 1.2] for scale in [1.1]]

for trial, (A, beta, scale) in enumerate(vacua):
    cb, sb = np.cos(beta), np.sin(beta)
    v, vb = scale*cb, scale*sb
    mz, mw = G*scale*scale/4, g2*g2*scale*scale/4
    b = A*sb*cb
    a, c = A*sb*sb-mz*(cb*cb-sb*sb)/2, A*cb*cb+mz*(cb*cb-sb*sb)/2
    z = np.array([v, 0, 0, vb], complex)/np.sqrt(2)
    full = (4*hessian(z, a, c, b, .015)-hessian(z, a, c, b, .03))/3
    grad = (4*gradient(z, a, c, b, .015)-gradient(z, a, c, b, .03))/3
    check(f'Original quartic full stationary point {trial}', grad, np.zeros(8))
    n = np.array([sb, cb])
    odd, charged = A*np.outer(n, n), (A+mw)*np.outer(n, n)
    even = A*np.array([[sb*sb, -sb*cb], [-sb*cb, cb*cb]])
    even += mz*np.array([[cb*cb, -sb*cb], [-sb*cb, sb*sb]])
    expected = np.zeros((8, 8))
    expected[:2, :2], expected[2:4, 2:4] = even, odd
    expected[4:6, 4:6] = charged
    expected[6:8, 6:8] = np.diag([1, -1])@charged@np.diag([1, -1])
    check(f'All 64 Hessian entries from original potential {trial}', full, expected)
    gap = np.sqrt((A+mz)**2-4*A*mz*np.cos(2*beta)**2)
    eigen = [0., 0., 0., A, A+mw, A+mw, (A+mz-gap)/2, (A+mz+gap)/2]
    check(f'Full eight scalar mass eigenvalues {trial}', np.linalg.eigvalsh(full), np.sort(eigen))
    gauge = np.array([canonical(1j*t@z) for t in generators])
    check(f'Gauge generators give Hessian null vectors {trial}', full@gauge.T, np.zeros((8, 4)))
    check(f'Exactly three broken gauge directions {trial}', np.linalg.matrix_rank(gauge, tol=1e-10), 3)
    tz = np.array([g*t@z for g, t in zip([g2, g2, g2, g1], generators)])
    vector_mass = 2*(tz.conj()@tz.T).real
    check(f'Gauge masses from full covariant kinetic term {trial}',
          np.linalg.eigvalsh(vector_mass), [0., mw, mw, mz])
    check(f'Rayleigh Higgs bound {trial}', np.array([cb, sb])@even@np.array([cb, sb]),
          mz*np.cos(2*beta)**2)
    # Independent global sampling supplements the analytic minimum proof in the article.
    samples = (rng.normal(size=(120, 4))+1j*rng.normal(size=(120, 4)))*scale
    energies = np.array([potential(t, a, c, b) for t in samples])
    check(f'Full complex field energy samples {trial}',
          float(np.min(energies) >= potential(z, a, c, b)-1e-10), 1.)

# At the origin the canonical spectrum consists of four copies of two roots.
for a, c, b in [(.4, 1.1, .3), (.4, .9, .6), (-.2, 1.3, .2), (.2, .4, .5)]:
    full = (4*hessian(np.zeros(4), a, c, b, .015)-hessian(np.zeros(4), a, c, b, .03))/3
    roots = [(a+c-np.sqrt((a-c)**2+4*b*b))/2, (a+c+np.sqrt((a-c)**2+4*b*b))/2]
    check(f'Origin spectrum {a,c,b}', np.linalg.eigvalsh(full), np.repeat(roots, 4))

# Bounded boundary with an unattained infimum: use full doublets along fixed Delta.
a, c, b = 1.2, .4, .8
delta = -(a-c)/(4*lam)
lower = -(a-c)**2/(16*lam)
previous = float('inf')
for total in [abs(delta)+1., 30., 90., 270.]:
    x, y = (total+delta)/2, (total-delta)/2
    z = np.array([np.sqrt(x), 0., 0., np.sqrt(y)])
    excess = potential(z, a, c, b)-lower
    check(f'Finite boundary excess Sigma={total}', excess,
          b*delta*delta/(total+np.sqrt(total*total-delta*delta)))
    check(f'Positive decreasing approach Sigma={total}', float(0 < excess < previous), 1.)
    previous = excess

for Y in [-.5, .5]:
    weak = np.trace((sigma[0]/2)@(sigma[0]/2)*(Y)).real
    cub = np.trace(np.linalg.matrix_power(Y*np.eye(2), 3))
    grav = np.trace(Y*np.eye(2))
    check(f'Explicit doublet anomaly traces Y={Y}', [weak, cub, grav], [Y/2, 2*Y**3, 2*Y])

result = dict(checks=len(records), all_passed=all(r["passed"] for r in records),
              max_scaled_residual=max(r["scaled_residual"] for r in records),
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(), records=records)
(ROOT/"checks/srednicki/mssm96-check.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k != "records"}, indent=2))
if not result["all_passed"]:
    print(json.dumps([r for r in records if not r["passed"]], indent=2))
    raise SystemExit(1)
