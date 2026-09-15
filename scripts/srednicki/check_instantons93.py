"""Cartesian BPST fields, winding traces, Wick signs, and action integrals."""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
rng = np.random.default_rng(930915)
records = []


def epsilon(n):
    e = np.zeros((n,) * n)
    for p in permutations(range(n)):
        e[p] = (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
    return e


e3, e4 = epsilon(3), epsilon(4)
sigma = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
eta = np.zeros((4, 4, 3))  # spacetime mu, nu, color a
eta[:3, :3] = np.moveaxis(e3, 0, 2)
eta[:3, 3] = np.eye(3)
eta[3, :3] = -np.eye(3)


def check(name, actual, expected, tol=5e-11):
    err = float(np.max(np.abs(np.asarray(actual) - expected)))
    scale = max(1., float(np.max(np.abs(expected))))
    records.append(dict(name=name, scaled_residual=err/scale, passed=err < tol*scale))


for sample in range(10):
    x = rng.normal(size=4)
    a, g = .2+rng.random(), .4+rng.random()
    r2 = x@x
    D = r2+a*a
    h = np.einsum('mna,n->ma', eta, x)
    A = 2*h/(g*D)
    # Derivatives of every Cartesian component of the potential.
    dA = np.array([[(2/g)*(eta[nu, mu]/D-2*x[mu]*h[nu]/D**2)
                    for nu in range(4)] for mu in range(4)])
    F = np.array([[dA[mu, nu]-dA[nu, mu]+g*np.cross(A[mu], A[nu])
                   for nu in range(4)] for mu in range(4)])
    check(f'full nonabelian Cartesian strength {sample}', F, -4*a*a*eta/(g*D**2))
    dual = .5*np.einsum('mnrs,rsa->mna', e4, F)
    check(f'self-duality all components {sample}', dual, F)
    # Ordinary derivative of the explicit curvature plus all connection terms.
    dF = 16*a*a*np.einsum('l,mna->lmna', x, eta)/(g*D**3)
    div = np.array([sum(dF[mu, mu, nu]+g*np.cross(A[mu], F[mu, nu])
                        for mu in range(4)) for nu in range(4)])
    check(f'Yang-Mills equation all components {sample}', div, np.zeros((4, 3)))
    check(f'original kinetic and topological densities {sample}',
          [np.sum(F*F)/4, g*g*np.sum(dual*F)/(32*np.pi**2)],
          [48*a**4/(g*g*D**4), 6*a**4/(np.pi**2*D**4)])
    P = np.diag([-1., 1., 1., 1.])
    Fa = np.einsum('rm,sn,rsa->mna', P, P, F)
    check(f'reflected anti-self-duality {sample}',
          .5*np.einsum('mnrs,rsa->mna', e4, Fa), -Fa)
    # Derive U dU^dagger directly from its quaternion expression.
    rho = np.sqrt(r2)
    U = (x[3]*np.eye(2)+1j*np.einsum('a,aij->ij', x[:3], sigma))/rho
    dU = [(1j*sigma[mu] if mu < 3 else np.eye(2))/rho-U*x[mu]/r2 for mu in range(4)]
    B = np.array([U@d.conj().T for d in dU])
    check(f'pure-gauge Maurer components {sample}', B,
          -1j*np.einsum('ma,aij->mij', h, sigma)/r2)

    # Arbitrary noncommuting matrix-valued Minkowski strengths; not just BPST.
    FM = rng.normal(size=(4, 4, 3))
    FM = np.einsum('mna,aij->mnij', FM-FM.swapaxes(0, 1), sigma/2)
    FE = np.zeros_like(FM)
    FE[:3, :3] = FM[1:, 1:]
    for i in range(3):
        FE[i, 3] = 1j*FM[0, i+1]
        FE[3, i] = -FE[i, 3]
    topM = .5*np.einsum('mnrs,mnij,rsji->', e4, FM, FM)
    topE = .5*np.einsum('mnrs,mnij,rsji->', e4, FE, FE)
    check(f'Wick topological trace sign {sample}', topE, 1j*topM)
    metric = np.diag([-1., 1., 1., 1.])
    raised = np.einsum('mr,ns,rsij->mnij', metric, metric, FM)
    check(f'Wick kinetic trace sign {sample}',
          np.einsum('mnij,mnji->', FE, FE), np.einsum('mnij,mnji->', raised, FM))


def angular_matrix(chi, psi, phi, N):
    """U^N and its three derivatives from explicit sine/cosine matrices."""
    n = np.array([np.sin(psi)*np.cos(phi), np.sin(psi)*np.sin(phi), np.cos(psi)])
    np_ = np.array([np.cos(psi)*np.cos(phi), np.cos(psi)*np.sin(phi), -np.sin(psi)])
    nf = np.array([-np.sin(psi)*np.sin(phi), np.sin(psi)*np.cos(phi), 0.])
    sn = np.einsum('a,aij->ij', n, sigma)
    c, s = np.cos(N*chi), np.sin(N*chi)
    U = c*np.eye(2)+1j*s*sn
    deriv = [-N*s*np.eye(2)+1j*N*c*sn,
             1j*s*np.einsum('a,aij->ij', np_, sigma),
             1j*s*np.einsum('a,aij->ij', nf, sigma)]
    B = np.array([U@d.conj().T for d in deriv])
    density = np.einsum('abc,aij,bjk,cki->', e3, B, B, B)
    return density


for N in [-4, -1, 0, 1, 3]:
    chi, psi, phi = .27+rng.random()*2, .3+rng.random()*2, rng.random()*6
    check(f'power-map direct triple trace N={N}', angular_matrix(chi, psi, phi, N),
          -12*N*np.sin(N*chi)**2*np.sin(psi))

nodes, weights = np.polynomial.legendre.leggauss(240)
y, w = (nodes+1)/2, weights/2
for N in [-4, -1, 0, 1, 3]:
    # Trace density is independent of phi and proportional to sin(psi).
    density = np.array([angular_matrix(t, np.pi/2, .71, N) for t in np.pi*y])
    degree = -np.dot(np.pi*w, density)*2*(2*np.pi)/(24*np.pi**2)
    check(f'integrated matrix winding N={N}', degree, N)

for a, g in [(.1, .7), (1., 1.2), (3., .4)]:
    # Independent quadrature on the full radial half-line r=a*y/(1-y).
    r = a*y/(1-y)
    jac = a/(1-y)**2
    density = 48*a**4/(g*g*(r*r+a*a)**4)
    action = np.dot(w, 2*np.pi**2*r**3*jac*density)
    check(f'full-line original action a,g={a,g}', action, 8*np.pi**2/g**2)
    for t in [1., 4., 40.]:
        r = a*t*y
        densityQ = 6*a**4/(np.pi**2*(r*r+a*a)**4)
        charge = np.dot(w, 2*np.pi**2*r**3*(a*t)*densityQ)
        check(f'finite-ball original charge a,t={a,t}', charge,
              1-3/(1+t*t)**2+2/(1+t*t)**3)

for m in [9, 13, 21]:
    h = {0: .8, 1: -.13, -1: -.13, 2: .04, -2: .04}
    H = np.array([[h.get((i-j+m//2) % m-m//2, 0) for j in range(m)] for i in range(m)])
    for k in [0, 1, m-1]:
        theta = 2*np.pi*k/m
        v = np.exp(-1j*np.arange(m)*theta)
        energy = sum(value*np.exp(1j*ell*theta) for ell, value in h.items())
        check(f'circulant Hamiltonian Fourier m,k={m,k}', H@v, energy*v)

result = dict(checks=len(records), all_passed=all(r["passed"] for r in records),
              max_scaled_residual=max(r["scaled_residual"] for r in records),
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(), records=records)
out = ROOT/"checks/srednicki/instantons93-check.json"
out.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k != "records"}, indent=2))
if not result["all_passed"]:
    print(json.dumps([r for r in records if not r["passed"]], indent=2))
    raise SystemExit(1)
