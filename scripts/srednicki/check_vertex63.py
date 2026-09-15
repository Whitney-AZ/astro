#!/usr/bin/env python3
"""New S63 finite checks: raw spinor chains, simplex integral, finite Ward terms, IR slope."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import platform
import numpy as np
import scipy
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

report = {
    "executed_at_utc": datetime.now(timezone.utc).isoformat(),
    "executed_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "software": {"Python": platform.python_version(),
                 "NumPy": np.__version__, "SciPy": scipy.__version__},
    "conventions": "g=(-,+,+,+); Clifford=-2g; slash p = p_mu gamma^mu; "
                   "m>0; future equal-mass electron shells; q=pprime-p; epsilon0123=+1",
    "scope": "Finite evidence for C63.16/17/28/14/30 and EX63.1.4; "
             "not a proof of all kinematics or of convergence.",
    "projected_chains": [], "parity_dual": [], "pauli_integral": [],
    "finite_ward": [], "infrared_slope": {},
}
I2 = np.eye(2, dtype=complex)
O2 = np.zeros((2, 2), dtype=complex)
sigma = [np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.array([[1, 0], [0, -1]], complex)]
gamma = [np.block([[I2, O2], [O2, -I2]])]
gamma += [np.block([[O2, s], [-s, O2]]) for s in sigma]
g = np.array([-1., 1., 1., 1.])
I4 = np.eye(4, dtype=complex)
gamma5 = 1j*gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
slash = lambda v: sum(g[i]*v[i]*gamma[i] for i in range(4))
dot = lambda v, w: float(np.sum(g*v*w))
m = 1.4
mu_scale = .9

def external(v):
    E = np.sqrt(m*m+np.dot(v, v))
    p = np.r_[E, v]
    lower = sum(v[i]*sigma[i] for i in range(3))/(E+m)
    U = np.sqrt(E+m)*np.vstack([I2, lower])
    assert np.max(np.abs((slash(p)+m*I4) @ U)) < 2e-14
    return p, U

p, U = external(np.array([.4, -.2, .7]))
pp, Up = external(np.array([-.3, .6, .5]))
barUp = Up.conjugate().T @ gamma[0]
q, K = pp-p, pp+p
x, y = .21, .35
x3 = 1-x-y
a1, a2 = x*p-(1-y)*pp, y*pp-(1-x)*p
report["input"] = {"mass": m, "mu_scale": mu_scale,
                   "p": p.tolist(), "pprime": pp.tolist(), "x1": x, "x2": y}
for index in range(4):
    raw = sum(g[nu]*gamma[nu] @ (slash(a1)+m*I4) @ gamma[index]
              @ (slash(a2)+m*I4) @ gamma[nu] for nu in range(4))
    projected_16 = (
        (4*(1-x-y+x*y)*dot(p, pp)+2*(2*x-x*x+2*y-y*y)*m*m)*gamma[index]
        +4*m*(x*x-y+x*y)*p[index]*I4
        +4*m*(y*y-x+x*y)*pp[index]*I4)
    projected_17 = (
        2*((1-2*x3-x3*x3)*m*m-(x3+x*y)*dot(q, q))*gamma[index]
        -2*m*x3*(1-x3)*K[index]*I4
        -2*m*((x+x*x)-(y+y*y))*q[index]*I4)
    actual = barUp @ raw @ U
    for label, candidate in [("C63.16", projected_16), ("C63.17", projected_17)]:
        residuals = np.abs(actual-barUp @ candidate @ U)
        assert np.max(residuals) < 2e-12
        report["projected_chains"].append({
            "mu": index, "formula": label,
            "four_spin_pair_residuals": residuals.tolist()})

def epsilon(indices):
    if len(set(indices)) != 4:
        return 0
    inversions = sum(indices[i] > indices[j] for i in range(4) for j in range(i+1, 4))
    return (-1)**inversions

for index in range(4):
    dual = sum(-1j*epsilon([index, nu, rho, s])*g[nu]*p[nu]*g[rho]*pp[rho]
               *g[s]*gamma[s] @ gamma5
               for nu in range(4) for rho in range(4) for s in range(4))
    direct = gamma[index] @ slash(p) @ slash(pp) + p[index]*slash(pp) \
             - pp[index]*slash(p) + dot(p, pp)*gamma[index]
    residual = float(np.max(np.abs(dual-direct)))
    assert residual < 2e-13
    report["parity_dual"].append({"mu": index, "matrix_max_residual": residual})

def J(z):
    return 4*np.arctanh(np.sqrt(z/(z+4)))/np.sqrt(z*(z+4))

nodes, weights = leggauss(64)
nodes, weights = (nodes+1)/2, weights/2
for z in [.1, 4., 30.]:
    value = 0.
    for third, wt in zip(nodes, weights):
        upper = 1-third
        first = upper*nodes
        second = 1-third-first
        D = first*second*z+(1-third)**2
        integrand = 2*third*(1-third)/D
        value += wt*upper*np.dot(weights, integrand)
    closed = J(z)
    residual = abs(value-closed)
    assert residual < 2e-12
    report["pauli_integral"].append({
        "q2_over_m2": z, "original_simplex_gauss64x64": float(value),
        "closed": float(closed), "absolute_residual": float(residual),
        "note": "Interior nodes evaluate original x1,x3 integrand and variable interval; no endpoint cancellation in code."})

def integrate(f, a):
    val, err = quad(f, 0, 1, points=[a], epsabs=2e-11, epsrel=2e-11)
    return val, err

for a in [.03, .15, .5]:
    h = lambda t: t*t+a*a*(1-t)
    L = lambda t: np.log(m*m*h(t)/(mu_scale*mu_scale))
    kap1, er1 = integrate(lambda x3: (1-x3)*(1-4*x3+x3*x3)/
                         ((1-x3)**2+x3*a*a), a)
    kap2, er2 = integrate(lambda t: -2*t*(1-t*t)/h(t), a)
    log1, er3 = integrate(lambda t: t*L(t), a)
    log2, er4 = integrate(lambda t: (1-t)*L(t), a)
    finite1 = 1+log1-kap1
    finite2 = .5+log2-kap2
    residual = abs(finite1-finite2)
    assert residual < 3e-10
    report["finite_ward"].append({
        "m_gamma_over_m": a, "kappa1": kap1, "kappa2": kap2,
        "deltaZ1_over_c_plus_1_over_epsilon": finite1,
        "deltaZ2_over_c_plus_1_over_epsilon": finite2,
        "absolute_residual": residual,
        "sum_estimated_quadrature_errors": er1+er2+er3+er4})

yn, yw = leggauss(80)
yn, yw = (yn+1)/2, yw/2
z = 2.
values = []
for a in [.003, .0003]:
    value, estimated_error = 0., 0.
    for yy, ww in zip(yn, yw):
        w = yy*(1-yy)
        def f(t):
            x3 = 1-t
            R = 1-4*x3+x3*x3
            B = x3+t*t*w
            d0 = t*t+(1-t)*a*a
            d = d0+t*t*z*w
            return 2*t*(np.log(d/d0)+R/d0+(B*z-R)/d)
        v, er = integrate(f, a)
        value += ww*v
        estimated_error += ww*er
    values.append(float(value))
    report["infrared_slope"].setdefault("integrals", []).append(
        {"m_gamma_over_m": a, "full_regulated_F1_bracket": float(value),
         "weighted_estimated_t_quadrature_error": float(estimated_error)})
slope = (values[1]-values[0])/np.log(10)
coefficient = 2*((z+2)*J(z)-2)
residual = abs(slope-coefficient)
assert residual < .02
report["infrared_slope"].update({
    "q2_over_m2": z, "difference_quotient_in_log_1_over_a": float(slope),
    "derived_log_coefficient": float(coefficient), "absolute_difference": float(residual),
    "acceptance_absolute_tolerance": .02,
    "note": "Finite-regulator asymptotic evidence; t quadrature estimates exclude Gauss-y error; not a rigorous remainder bound."})
report["scalar_comparisons"] = 32+4+3+3+1
report["status"] = "pass"
(Path(__file__).resolve().parents[2] / "checks/srednicki/vertex63-check.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2)+"\n")
print(json.dumps(report, ensure_ascii=False, indent=2))
