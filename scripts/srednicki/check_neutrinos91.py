"""Takagi construction, Schur elimination and vacuum oscillation cross-checks."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
rng = np.random.default_rng(910915)
records = []


def check(name, actual, expected, tol=3e-11):
    err = float(np.max(np.abs(np.asarray(actual)-expected)))
    scale = max(1., float(np.max(np.abs(expected))))
    records.append(dict(name=name, scaled_residual=err/scale, passed=err < tol*scale))


def unitary(n):
    return np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]


def takagi(A):
    n = len(A)
    H = np.block([[A.real, -A.imag], [-A.imag, -A.real]])
    eig, vec = np.linalg.eigh(H)
    keep = eig > 1e-10*max(1., np.max(abs(eig)))
    pos = vec[:n, keep]+1j*vec[n:, keep]
    if pos.shape[1] < n:
        _, sv, vh = np.linalg.svd(A)
        zero = vh.conj().T[:, sv <= 1e-10*max(1., sv.max())]
        N = np.column_stack([pos, zero])
    else:
        N = pos
    D = np.r_[eig[keep], np.zeros(n-pos.shape[1])]
    return N, D


for n in [2, 3, 6]:
    for case in ['generic', 'degenerate', 'zero', 'all zero']:
        U = unitary(n)
        d = np.arange(1., n+1)
        if case == 'degenerate': d[:2] = 1.
        if case == 'zero': d[0] = 0.
        if case == 'all zero': d[:] = 0.
        A = U.conj()@np.diag(d)@U.conj().T
        N, D = takagi(A)
        check(f'Takagi unitary {n,case}', N.conj().T@N, np.eye(n))
        check(f'Takagi congruence {n,case}', N.T@A@N, np.diag(D))
        check(f'Takagi singular values {n,case}', np.sort(D), np.sort(d))

for ratio in [0., .0001, .03, .5, 2.]:
    M, d = 4., 4.*ratio
    A = np.array([[0., d], [d, M]])
    angle = .5*np.arctan2(2*d, M)
    c, s = np.cos(angle), np.sin(angle)
    N = np.array([[1j*c, s], [-1j*s, c]])
    # Stable formula for the small root avoids subtracting two nearly equal numbers.
    mh = (np.sqrt(M*M+4*d*d)+M)/2
    ml = d*d/mh
    check(f'exact one-generation masses {ratio}', N.T@A@N, np.diag([ml,mh]))
    check(f'exact mass difference {ratio}', mh-ml, M)
    check(f'exact mixing direction {ratio}', np.tan(angle), d/mh)

for sample in range(6):
    V, L = unitary(3), unitary(3)
    M = V.conj()@np.diag([2., 3., 5.])@V.conj().T
    Y = rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    K = Y@np.linalg.solve(M,Y.T)
    Mp, Yp = V.T@M@V, L.T@Y@V
    check(f'effective symmetric mass {sample}', K, K.T)
    check(f'basis covariance {sample}', Yp@np.linalg.solve(Mp,Yp.T), L.T@K@L)
    d = .002*Y
    R = np.linalg.solve(M, d.T)
    full = np.block([[np.zeros((3,3)), d], [d.T, M]])
    W = np.block([[np.eye(3), np.zeros((3,3))], [-R, np.eye(3)]])
    target = np.block([[-d@R, np.zeros((3,3))], [np.zeros((3,3)), M]])
    check(f'exact Schur block elimination {sample}', W.T@full@W, target)
    check(f'leading kinetic normalization {sample}', (W.conj().T@W)[:3,:3],
          np.eye(3)+R.conj().T@R)
    N, mass = takagi(-d@R)
    charged = unitary(3)
    X = N.conj().T@charged
    check(f'charged basis mass {sample}', charged.T@(-d@R)@charged,
          X.T@np.diag(mass)@X)

for sample in range(7):
    X = unitary(3)
    m2 = np.array([0., .7, 2.])
    t = .3+sample
    Dphase = np.diag(np.exp(1j*rng.normal(size=3)))
    Ephase = np.diag(np.exp(1j*rng.normal(size=3)))
    direct = X.conj().T@np.diag(np.exp(-1j*m2*t))@X
    probabilities = abs(direct.T)**2  # rows source alpha, columns detected beta
    formula = np.eye(3)
    for alpha in range(3):
        for beta in range(3):
            for i in range(3):
                for j in range(i):
                    Q = X[i,beta].conjugate()*X[i,alpha]*X[j,beta]*X[j,alpha].conjugate()
                    delta = (m2[i]-m2[j])*t
                    formula[alpha,beta] += -4*Q.real*np.sin(delta/2)**2+2*Q.imag*np.sin(delta)
    check(f'oscillation interference expansion {sample}', probabilities, formula)
    check(f'probability conservation {sample}', probabilities.sum(axis=1), np.ones(3))
    Xp = Dphase@X@Ephase
    other = Xp.conj().T@np.diag(np.exp(-1j*m2*t))@Xp
    check(f'Majorana and charged phase cancellation {sample}', abs(other)**2, abs(direct)**2)
    check(f'zero baseline {sample}', abs(X.conj().T@X)**2, np.eye(3))
    for angle in [.2, .6]:
        c, s = np.cos(angle), np.sin(angle)
        X2 = np.array([[c,s],[-s,c]])
        A2 = X2.T@np.diag(np.exp(-1j*m2[:2]*t))@X2
        check(f'two-flavor transition {sample,angle}', abs(A2[1,0])**2,
              np.sin(2*angle)**2*np.sin((m2[1]-m2[0])*t/2)**2)

result = dict(checks=len(records), passed=all(r['passed'] for r in records),
              records=records, script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'checks/srednicki/neutrinos91-check.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(dict(checks=len(records), passed=result['passed'],
                     max_scaled_residual=max(r['scaled_residual'] for r in records),
                     failures=[r for r in records if not r['passed']]), indent=2))
raise SystemExit(0 if result['passed'] else 1)
