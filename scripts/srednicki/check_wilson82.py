"""Independent quadratures and SU(2) link matrices for section 82."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
nodes, weights = np.polynomial.legendre.leggauss(400)
records = []


def integral(f, lo, hi):
    x = lo + (nodes + 1) * (hi - lo) / 2
    return np.sum(weights * f(x)) * (hi - lo) / 2


def check(name, actual, expected, tolerance=2e-10):
    residual = float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))
    scale = max(1., float(np.max(np.abs(expected))))
    records.append(dict(name=name, residual=residual,
                        scaled_residual=residual/scale,
                        tolerance=tolerance, passed=residual <= tolerance*scale))


for ratio in [.001, .01, .1, .3, 1.]:
    delta = 2*np.arcsin(ratio/2)
    # Integrate the original tangent/chord kernel, on both sides of pi.
    actual = 4*np.pi*integral(
        lambda t: np.cos(delta*np.exp(t))/(4*np.sin(delta*np.exp(t)/2)**2)
        * delta*np.exp(t), 0, np.log(np.pi/delta))
    exact = 2*np.pi*(1/np.tan(delta/2)-np.pi+delta)
    check(f"circle chord a/R={ratio}", actual, exact)

for L, a in [(1., .01), (3., .07), (20., .03)]:
    actual = 2*integral(lambda t: (L-a*np.exp(t))/(a*np.exp(t)),
                        0, np.log(L/a))
    check(f"same edge L={L}", actual, 2*L/a-2-2*np.log(L/a))

for L, d in [(1., 3.), (3., 1.), (20., .2), (.3, .7)]:
    def kernel(t):
        u = d*np.expm1(t)
        return 2*(L-u)/(u*u+d*d)*d*np.exp(t)
    actual = integral(kernel, 0, np.log1p(L/d))
    check(f"opposite edges L={L}, d={d}", actual,
          2*L/d*np.arctan(L/d)-np.log1p((L/d)**2))

# SU(2) class measure on S^3. These are actual finite Haar integrals.
def haar(f):
    return 2/np.pi*integral(lambda t: np.sin(t)**2*f(2*np.cos(t)), 0, np.pi)

for power, exact in [(0, 1), (1, 0), (2, 1), (3, 0), (4, 2)]:
    check(f"SU2 trace moment {power}", haar(lambda w: w**power), exact)

for h in [.0001, .001, .01]:
    loop = haar(lambda w: w*np.exp(2*h*w))/haar(lambda w: np.exp(2*h*w))
    # The moments give 2h - 4h^3/3 + O(h^5), including normalization.
    check(f"SU2 one plaquette h={h}", loop, 2*h-4*h**3/3, 2e-9)

sigma = np.array([[[0,1],[1,0]], [[0,-1j],[1j,0]], [[1,0],[0,-1]]])
A = np.einsum("a,aij->ij", [.3, -.2, .7], sigma)/2
B = np.einsum("a,aij->ij", [.4, .6, -.1], sigma)/2
C = np.einsum("a,aij->ij", [-.2, .3, .1], sigma)/2
D = np.einsum("a,aij->ij", [.5, -.1, .2], sigma)/2
g = .7
F = D-C-1j*g*(A@B-B@A)


def unitary(H):
    vals, vecs = np.linalg.eigh(H)
    return (vecs*np.exp(1j*vals))@vecs.conj().T


curvature_errors = []
trace_errors = []
for a in [.1, .05, .025, .0125]:
    U = (unitary(-g*a*(B-a*D/2)) @ unitary(-g*a*(A+a*C/2))
         @ unitary(g*a*(B+a*D/2)) @ unitary(g*a*(A-a*C/2)))
    check(f"plaquette unitarity a={a}", U.conj().T@U, np.eye(2))
    curvature_errors.append(float(np.linalg.norm((U-np.eye(2))/(1j*g*a*a)-F)))
    ratio = (4-2*np.trace(U).real)/(g*g*a**4*np.trace(F@F).real)
    trace_errors.append(abs(ratio-1))
for i in range(1, 4):
    # Leading curvature matrix error is O(a); the trace error is O(a^2).
    check(f"curvature convergence step {i}",
          curvature_errors[i]/curvature_errors[i-1], .5, .02)
    check(f"real trace convergence step {i}",
          trace_errors[i]/trace_errors[i-1], .25, .03)

result = dict(checks=len(records), passed=all(r['passed'] for r in records),
              records=records, curvature_errors=curvature_errors,
              real_trace_errors=trace_errors,
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'checks/srednicki/wilson82-check.json').write_text(
    json.dumps(result, indent=2, ensure_ascii=False)+'\n')
print(json.dumps(result, indent=2, ensure_ascii=False))
raise SystemExit(0 if result['passed'] else 1)
