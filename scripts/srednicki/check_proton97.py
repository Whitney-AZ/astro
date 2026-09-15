"""Open gamma chains, independent RG integration and full proton spin amplitudes."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np
from check_helicity60 import GAMMA, slash
GAMMA = np.asarray(GAMMA)

ROOT = Path(__file__).resolve().parents[2]
rng = np.random.default_rng(971015)
metric = np.array([-1., 1., 1., 1.])
I = np.eye(4)
gamma5 = np.diag([-1., -1., 1., 1.])
PL, PR = (I-gamma5)/2, (I+gamma5)/2
records = []


def check(name, actual, expected, tol=2e-10):
    err = float(np.max(np.abs(np.asarray(actual)-expected)))
    scale = max(1., float(np.max(np.abs(expected))))
    records.append(dict(name=name, scaled_residual=err/scale, passed=err < tol*scale))


for sample in range(4):
    directions = np.linalg.qr(rng.normal(size=(4, 4)))[0].T.astype(complex)
    directions[:, 0] *= 1j  # Wick-rotated orthonormal Euclidean angular quadrature.
    for xi in [-.3, 0., .6, 1.]:
        vectors = []
        for ell in directions:
            ell2 = ell@(metric*ell)
            P = np.diag(metric)-(1-xi)*np.outer(metric*ell, metric*ell)/ell2
            def numerator(insert):
                return sum(GAMMA[mu]@slash(ell)@insert@slash(ell)@GAMMA[nu]*P[mu, nu]
                           for mu in range(4) for nu in range(4))
            check(f'Full scalar UV chain sample={sample}, xi={xi}, direction={len(vectors)}',
                  numerator(I), (3+xi)*ell2*I)
            vectors.append([numerator(g) for g in GAMMA])
        check(f'Angular vector UV chain sample={sample}, xi={xi}',
              np.mean(vectors, axis=0), xi*GAMMA)


def su(n):
    out = []
    for i in range(n):
        for j in range(i+1, n):
            x, y = np.zeros((n, n), complex), np.zeros((n, n), complex)
            x[i, j] = x[j, i] = .5
            y[i, j], y[j, i] = -.5j, .5j
            out += [x, y]
    for k in range(1, n):
        out.append(np.diag([1.]*k+[-float(k)]+[0.]*(n-k-1))/np.sqrt(2*k*(k+1)))
    return out


for n in [2, 3]:
    tensors = []
    for i in range(n):
        for j in range(i+1, n):
            e = np.zeros((n, n))
            e[i, j], e[j, i] = 1., -1.
            tensors.append(e)
    for j, eps in enumerate(tensors):
        direct = sum(t.T@eps@t for t in su(n))
        check(f'Full antisymmetric tensor pair SU{n}, basis={j}', direct, -(n+1)/(2*n)*eps)
    check(f'Fundamental and antifundamental singlet pair SU{n}',
          -sum(t@t for t in su(n)), -(n*n-1)/(2*n)*np.eye(n))

alpha_inv, alpha3, MZ = 127.91, .1187, 91.2
B = 1/alpha3
numeric = {}
for model, b in [('SM', np.array([41/6, -19/6, -7.])), ('MSSM', np.array([11., 1., -3.]))]:
    # Solve the two original matching equations, independent of the printed closed expressions.
    inv5, L = np.linalg.solve([[1., b[2]/(2*np.pi)], [8/3, (b[0]+b[1])/(2*np.pi)]],
                             [B, alpha_inv])
    a5, MX = 1/inv5, MZ*np.exp(L)
    low_inv = np.array([5/3, 1., 1.])*inv5+b*L/(2*np.pi)
    weak = low_inv[1]/alpha_inv
    check(f'{model} electromagnetic input recovered', low_inv[0]+low_inv[1], alpha_inv)
    check(f'{model} color input recovered', 1/low_inv[2], alpha3)
    expected = ([41.4743, 29.6654, .20736] if model == 'SM'
                else [(3*alpha_inv+12*B)/20, np.pi*(alpha_inv-8*B/3)/10, .2+7*B/(15*alpha_inv)])
    check(f'{model} printed unification solution', [inv5, L, weak], expected, 2e-6)
    numeric[model] = dict(inv_alpha5=inv5, log_scale=L, MX=MX, weak_angle=weak)
    if model == 'SM':
        boundary = np.sqrt(4*np.pi*a5*np.array([3/5, 1., 1.]))
        low_alpha = 1/low_inv
        sm_a5, sm_MX, sm_L = a5, MX, L


def integrate(fun, y, start, end, steps=2400):
    h = (end-start)/steps
    y = y.copy()
    for _ in range(steps):
        k1 = fun(y)
        k2 = fun(y+h*k1/2)
        k3 = fun(y+h*k2/2)
        k4 = fun(y+h*k3)
        y += h*(k1+2*k2+2*k3+k4)/6
    return y


def high(y):
    g = y[:3]
    g1, g2, g3 = g*g
    return np.r_[np.array([41/6, -19/6, -7])*g**3,
                 -(4*g3+4.5*g2+11*g1/6), -(4*g3+4.5*g2+23*g1/6),
                 -8*g3+10*g1/3]/(16*np.pi**2)


high_result = integrate(high, np.r_[boundary, 0., 0., 0.], sm_L, 0.)
ratio_alpha = low_alpha/(sm_a5*np.array([3/5, 1., 1.]))
high_C = np.array([np.prod(ratio_alpha**[-3*a/41, 27/38, 2/7]) for a in [11/6, 23/6]])
high_r = ratio_alpha[2]**(4/7)*ratio_alpha[0]**(10/41)
check('RK4 full three gauge beta functions', high_result[:3]**2/(4*np.pi), low_alpha)
check('RK4 two Wilson coefficients', np.exp(high_result[3:5]), high_C)
check('RK4 Yukawa ratio', np.exp(high_result[5]), high_r)


def low(y):
    g3 = y[0]
    return np.array([-23*g3**3/3, -4*g3*g3, -4*g3*g3, -8*g3*g3])/(16*np.pi**2)


for mu in [2., 4.3]:
    result = integrate(low, np.r_[high_result[2], high_result[3:]], 0., np.log(mu/MZ))
    a3 = 1/(B+23*np.log(mu/MZ)/(6*np.pi))
    check(f'RK4 low QCD coupling at {mu}', result[0]**2/(4*np.pi), a3)
    check(f'RK4 low Wilson coefficients at {mu}', np.exp(result[1:3]),
          high_C*(a3/alpha3)**(6/23))
    check(f'RK4 low Yukawa ratio at {mu}', np.exp(result[3]), high_r*(a3/alpha3)**(12/23))
    if mu == 2.:
        CX = 4*np.pi*sm_a5/sm_MX**2
        C_low = CX*np.exp(result[1:3])
    else:
        tau_mass = 4.3/np.exp(result[3])
check('Printed Wilson coefficients in units 1e-30', C_low/1e-30, [1.75291, 1.85398], 3e-6)
check('Printed tau mass in GeV', tau_mass, 1.40001, 4e-6)


def spinors(p, mass):
    val, vec = np.linalg.eigh((-slash(p)+mass*I)@GAMMA[0])
    positive = val > 1e-9
    return vec[:, positive]*np.sqrt(val[positive])


def boost(p, beta):
    b2 = beta@beta
    ga = 1/np.sqrt(1-b2)
    return np.r_[ga*(p[0]+beta@p[1:]),
                 p[1:]+((ga-1)*(beta@p[1:])/b2+ga*p[0])*beta]


mp, mpi, fp, gA, Ahad = .938, .135, .0924, 1.27, .0090
momentum = (mp*mp-mpi*mpi)/(2*mp)
for trial in range(12):
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    beta = rng.normal(size=3)
    beta *= .55/np.linalg.norm(beta)
    p = boost(np.array([mp, 0., 0., 0.]), beta)
    r = boost(np.r_[momentum, momentum*n], beta)
    k = p-r
    u, w = spinors(p, mp), spinors(r, 0.)
    bw = w.conj().T@GAMMA[0]
    c1, c2 = rng.normal(size=2)+1j*rng.normal(size=2)
    K, Km = c1*PL+2*c2*PR, c1*PL-2*c2*PR
    pole = bw@K@(-slash(r)+mp*I)@slash(k)@gamma5@u/(r@(metric*r)+mp*mp)
    direct = -bw@Km@u
    check(f'All physical spin transitions: pole/contact ratio {trial}', pole, direct)
    summed = np.sum(abs(bw@Km@u)**2)/2
    expected = -(p@(metric*r))*(abs(c1)**2+4*abs(c2)**2)
    check(f'Full spin bases including complex chiral coefficients {trial}', summed, expected)
    Kmbar = GAMMA[0]@Km.conj().T@GAMMA[0]
    trace = np.trace(Km@(-slash(p)+mp*I)@Kmbar@(-slash(r)))/2
    check(f'Direct spin sums versus full four-dimensional trace {trial}', summed, trace)
    check(f'Off-shell intermediate nucleon inverse {trial}',
          (-slash(r)+mp*I)@(slash(r)+mp*I), mp*mp*I)

# Compute the phase-space factor from the energy delta Jacobian before comparison.
Er, Ek = momentum, np.sqrt(momentum**2+mpi**2)
jacobian = momentum*(1/Er+1/Ek)
phase_integral = 4*np.pi/(16*np.pi**2)*momentum**2/(Er*Ek*jacobian)
spin_average = Ahad**2*(1+gA)**2/(4*fp*fp)*(mp*mp-mpi*mpi)/2*(C_low[0]**2+4*C_low[1]**2)
width = phase_integral*spin_average/(2*mp)
lifetime = 6.5821195695e-25/width/(365.25*86400)
check('Full phase-space Jacobian and spin factor: width in 1e-63 GeV', width/1e-63, 1.83960, 3e-6)
check('Historical proton lifetime in 1e31 years', lifetime/1e31, 1.13381, 4e-6)
numeric.update(CX=CX, C_low=C_low.tolist(), high_C=high_C.tolist(), high_r=high_r,
               tau_mass=tau_mass, proton_width=width, proton_lifetime_years=lifetime)

result = dict(checks=len(records), all_passed=all(r["passed"] for r in records),
              max_scaled_residual=max(r["scaled_residual"] for r in records),
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
              helper_sha256=sha256((Path(__file__).parent/"check_helicity60.py").read_bytes()).hexdigest(),
              numerical_results=numeric, records=records)
(ROOT/"checks/srednicki/proton97-check.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k != "records"}, indent=2))
if not result["all_passed"]:
    print(json.dumps([r for r in records if not r["passed"]], indent=2))
    raise SystemExit(1)
