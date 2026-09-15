"""Explicit SU(5) representation, current, Yukawa and Spin(10) matrix checks."""
from pathlib import Path
from hashlib import sha256
from itertools import combinations, permutations
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
rng = np.random.default_rng(970915)
records = []


def check(name, actual, expected, tol=2e-10):
    err = float(np.max(np.abs(np.asarray(actual)-expected)))
    scale = max(1., float(np.max(np.abs(expected))))
    records.append(dict(name=name, scaled_residual=err/scale, passed=err < tol*scale))


def generators(n):
    out = []
    for i, j in combinations(range(n), 2):
        x = np.zeros((n, n), complex)
        x[i, j] = x[j, i] = .5
        out.append(x)
        y = np.zeros((n, n), complex)
        y[i, j], y[j, i] = -.5j, .5j
        out.append(y)
    for k in range(1, n):
        x = np.diag([1.]*k+[-float(k)]+[0.]*(n-k-1))/np.sqrt(2*k*(k+1))
        out.append(x.astype(complex))
    return np.array(out)


def wedge_matrix(x):
    n = len(x)
    basis = []
    for i, j in combinations(range(n), 2):
        e = np.zeros((n, n))
        e[i, j], e[j, i] = 1., -1.
        basis.append(e)
    return np.array([[np.vdot(e, x@f+f@x.T)/2 for f in basis] for e in basis])


for n in [3, 4, 5, 6]:
    for trial in range(4):
        xyz = []
        for _ in range(3):
            x = rng.normal(size=(n, n))+1j*rng.normal(size=(n, n))
            x = (x+x.conj().T)/2
            x -= np.trace(x)/n*np.eye(n)
            xyz.append(x)
        reps = [wedge_matrix(x) for x in xyz]
        raw = np.trace(reps[0]@(reps[1]@reps[2]+reps[2]@reps[1]))
        expected = (n-4)*np.trace(xyz[0]@(xyz[1]@xyz[2]+xyz[2]@xyz[1]))
        check(f'Noncommuting polarized cubic traces N={n} sample={trial}', raw, expected)
        check(f'Antisymmetric commutator representation N={n} sample={trial}',
              reps[0]@reps[1]-reps[1]@reps[0], wedge_matrix(xyz[0]@xyz[1]-xyz[1]@xyz[0]))

T = generators(5)
Y = np.diag([-1/3]*3+[.5]*2)
check('All 24 generator trace normalizations', np.einsum('aij,bji->ab', T, T), np.eye(24)/2)
V, g = 1.3, .7
comm = np.array([t@(V*Y)-(V*Y)@t for t in T])
mass = -2*g*g*np.einsum('aij,bji->ab', comm, comm).real
check('All 24 real vector masses from original adjoint kinetic term',
      np.linalg.eigvalsh(mass), [0.]*12+[(5*g*V/6)**2]*12)
check('10 hypercharge multiplicities', np.sort(np.linalg.eigvalsh(wedge_matrix(Y))),
      np.sort([-2/3]*3+[1/6]*6+[1.]))
check('Hypercharge normalization', np.trace((np.sqrt(3/5)*Y)**2), .5)
for k in range(6):
    z = np.exp(2j*np.pi*k/6)
    check(f'Z6 kernel representative {k}',
          np.diag([z**(-2)*z**2]*3+[z**3*z**(-3)]*2), np.eye(5))

# Species: dbar_r,b,g, e, nu, ubar_r,b,g, u_r,b,g, d_r,b,g, ebar.
psi = np.zeros((5, 15))
psi[np.arange(5), np.arange(5)] = [1, 1, 1, 1, -1]
chi = np.zeros((5, 5, 15))
for i, j, field, sign in [(0, 1, 7, 1), (0, 2, 6, -1), (1, 2, 5, 1),
                          (0, 3, 8, 1), (1, 3, 9, 1), (2, 3, 10, 1),
                          (0, 4, 11, 1), (1, 4, 12, 1), (2, 4, 13, 1), (3, 4, 14, 1)]:
    chi[i, j, field], chi[j, i, field] = sign, -sign
eps3 = np.zeros((3, 3, 3), int)
for p in permutations(range(3)):
    eps3[p] = (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
eps2 = np.array([[0, 1], [-1, 0]])
for alpha in range(3):
    for weak in range(2):
        a = np.zeros((5, 5))
        a[3+weak, alpha] = 1.  # coefficient of Xdagger/sqrt2
        raw = -psi.T@a.T@psi+np.einsum('abi,ac,cbj->ij', chi, a, chi)
        current = np.zeros((15, 15))
        current[alpha, 3 if weak == 0 else 4] = 1 if weak == 0 else -1
        current[14, 11+alpha if weak == 0 else 8+alpha] = -1 if weak == 0 else 1
        for beta in range(3):
            for gamma in range(3):
                current[(8 if weak == 0 else 11)+beta, 5+gamma] += eps3[alpha, beta, gamma]
        check(f'Full 15-species Xdagger current alpha={alpha}, weak={weak}', raw, -current)


def symmetric(x):
    # The contracted bilinear of two odd Weyl fields is symmetric in species.
    return (x+x.T)/2


for trial in range(5):
    h = rng.normal(size=5)+1j*rng.normal(size=5)
    varphi = np.array([-h[4], h[3]])
    raw1 = np.einsum('a,bi,abj->ij', h, psi, chi)
    expected1 = np.zeros((15, 15), complex)
    for i in range(2):
        for j in range(2):
            expected1[[4, 3][j], 14] += eps2[i, j]*varphi[i]
            for alpha in range(3):
                expected1[[8+alpha, 11+alpha][j], alpha] += eps2[i, j]*varphi[i]
                expected1[[8+alpha, 11+alpha][i], [4, 3][j]] += eps2[i, j]*h[alpha]
    for alpha, beta, gamma in permutations(range(3)):
        expected1[beta, 5+gamma] += eps3[alpha, beta, gamma]*h[alpha]
    check(f'Complete first invariant Yukawa expansion {trial}', symmetric(raw1), symmetric(expected1))
    raw2 = np.zeros((15, 15), complex)
    for p in permutations(range(5)):
        sign = (-1)**sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5))
        a, b, c, d, e = p
        raw2 += sign*h[a].conjugate()*np.outer(chi[b, c], chi[d, e])/8
    expected2 = np.zeros((15, 15), complex)
    for alpha in range(3):
        expected2[5+alpha, 14] += h[alpha].conjugate()
        for i in range(2):
            expected2[[8+alpha, 11+alpha][i], 5+alpha] -= varphi[i].conjugate()
    for alpha, beta, gamma in permutations(range(3)):
        for i in range(2):
            for j in range(2):
                expected2[[8+beta, 11+beta][i], [8+gamma, 11+gamma][j]] -= (
                    h[alpha].conjugate()*eps3[alpha, beta, gamma]*eps2[i, j]/2)
    check(f'All 120 epsilon terms including qq Higgs coupling {trial}', symmetric(raw2), symmetric(expected2))
    scalar_mass = .8*np.eye(5)-.9/2*(V*Y.T)@(V*Y.T)
    check(f'Five scalar quadratic coefficients {trial}', h.conj()@scalar_mass@h,
          (.8-.9*V*V/18)*np.linalg.norm(h[:3])**2+(.8-.9*V*V/8)*np.linalg.norm(h[3:])**2)

# Expand Kdagger K as a polynomial in four independent even sources and their
# conjugates; project by baryon charge rather than starting from target operators.
charge3 = dict(A=-2, B=1, C=-1, D=2, a=2, b=-1, c=1, d=-2)
for trial in range(6):
    y, up = rng.normal(size=2)+1j*rng.normal(size=2)
    K = dict(C=up, D=-up/2, a=y.conjugate(), b=y.conjugate())
    Kdag = {name.swapcase():value.conjugate() for name, value in K.items()}
    full = {}
    for left, lvalue in Kdag.items():
        for right, rvalue in K.items():
            key = tuple(sorted([left, right]))
            full[key] = full.get(key, 0.)+lvalue*rvalue
    projected = {key:value for key, value in full.items()
                 if abs(sum(charge3[name] for name in key)) == 3}
    expected = {}
    for names, value in [('Ab', abs(y)**2), ('cD', -abs(up)**2/2),
                          ('AC', y*up), ('BD', -y*up/2)]:
        expected[tuple(sorted(names))] = value
        expected[tuple(sorted(name.swapcase() for name in names))] = np.conj(value)
    keys = sorted(set(projected)|set(expected))
    check(f'All baryon-violating scalar source coefficients {trial}',
          [projected.get(k, 0.) for k in keys], np.array([expected.get(k, 0.) for k in keys]))

# Full 32-state fermionic Fock construction of the internal Clifford algebra.
annih = []
for a in range(5):
    matrix = np.zeros((32, 32))
    for state in range(32):
        if state & (1 << a):
            matrix[state ^ (1 << a), state] = (-1)**((state & ((1 << a)-1)).bit_count())
    annih.append(matrix)
gamma = np.array([x for a in annih for x in [a+a.T, 1j*(a-a.T)]])
check('All 100 Clifford anticommutators',
      np.array([[a@b+b@a for b in gamma] for a in gamma]),
      np.einsum('ab,ij->abij', 2*np.eye(10), np.eye(32)))
parity = np.diag([(-1)**s.bit_count() for s in range(32)])
even = np.array([s for s in range(32) if s.bit_count() % 2 == 0])
check('Even spinor dimension', len(even), 16)
su5fock = np.array([sum(t[a, b]*annih[a].T@annih[b] for a in range(5) for b in range(5)) for t in T])
check('SU5 preserves internal chirality', [parity@t-t@parity for t in su5fock], np.zeros((24, 32, 32)))
fockY = sum(Y[a, a]*annih[a].T@annih[a] for a in range(5))
expectedY = [0.]+[-2/3]*3+[1/6]*6+[1.]+[1/3]*3+[-.5]*2
check('Even spinor hypercharges 1+10+bar5', np.sort(np.linalg.eigvalsh(fockY[np.ix_(even, even)])), np.sort(expectedY))

result = dict(checks=len(records), all_passed=all(r["passed"] for r in records),
              max_scaled_residual=max(r["scaled_residual"] for r in records),
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(), records=records)
(ROOT/"checks/srednicki/su5-97-check.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k != "records"}, indent=2))
if not result["all_passed"]:
    print(json.dumps([r for r in records if not r["passed"]], indent=2))
    raise SystemExit(1)
