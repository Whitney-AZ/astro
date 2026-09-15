#!/usr/bin/env python3
"""New S64 finite-spinor and finite-width evidence; no earlier script is imported."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import platform
import numpy as np
import scipy
from scipy.integrate import quad

report = {
    "executed_at_utc": datetime.now(timezone.utc).isoformat(),
    "executed_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "software": {"Python": platform.python_version(), "NumPy": np.__version__, "SciPy": scipy.__version__},
    "conventions": "g=(-,+,+,+), Clifford=-2g, e<0, m>0, canonical rest spin up; "
                   "A2=B*x at time0; radial Gaussian normalized with d3p/((2pi)^3 2E).",
    "scope": "C64.23-28 and EX64.1.14 radial limit; finite differences and quadrature "
             "are evidence for tested cases, not proof of general remainder bounds.",
    "basis_conversion": [], "bilinears": [], "gaussian_width": [],
}
I = np.eye(2, dtype=complex)
O = np.zeros((2, 2), dtype=complex)
sig = [np.array([[0, 1], [1, 0]], complex),
       np.array([[0, -1j], [1j, 0]], complex),
       np.diag([1., -1.]).astype(complex)]
gw = [np.block([[O, I], [I, O]])] + [np.block([[O, s], [-s, O]]) for s in sig]
gd = [np.block([[I, O], [O, -I]])] + [np.block([[O, s], [-s, O]]) for s in sig]
T = np.block([[I, I], [-I, I]])/np.sqrt(2)
for mu in range(4):
    err = float(np.max(np.abs(T @ gw[mu] @ T.conjugate().T-gd[mu])))
    assert err < 5e-15
    report["basis_conversion"].append({"mu": mu, "matrix_max_residual": err})
m = 1.7
chi = np.array([1., 0.], complex)
def u(p):
    E = np.sqrt(m*m+np.dot(p, p))
    return np.sqrt(E+m)*np.r_[chi, sum(p[j]*sig[j] for j in range(3)) @ chi/(E+m)]
S12 = .25j*(gd[1] @ gd[2]-gd[2] @ gd[1])
step = 1e-5*m
shift = np.array([step, 0., 0.])
for p in [np.array([.31, -.27, .48]), np.array([-.6, .2, -.4]), np.array([.9, .8, -.7])]:
    E = np.sqrt(m*m+np.dot(p, p))
    uu = u(p)
    bar = uu.conjugate() @ gd[0]
    derivative = (u(p+shift)-u(p-shift))/(2*step)
    minimal = bar @ (1j*gd[2]) @ derivative
    pauli = bar @ S12 @ uu
    targets = [1-p[0]**2/(E*(E+m)), E-p[2]**2/(E+m)]
    values = [minimal, pauli]
    residuals = [float(abs(v-t)) for v, t in zip(values, targets)]
    assert residuals[0] < 2e-9 and residuals[1] < 2e-13
    report["bilinears"].append({
        "p": p.tolist(), "mass": m, "finite_difference_step": step,
        "minimal_complex": [float(minimal.real), float(minimal.imag)],
        "pauli_complex": [float(pauli.real), float(pauli.imag)],
        "derived_targets": targets, "absolute_residuals": residuals})
du0 = (u(shift)-u(-shift))/(2*step)
rest_target = -gd[1] @ u(np.zeros(3))/(2*m)
rest_error = float(np.max(np.abs(du0-rest_target)))
assert rest_error < 2e-10
report["rest_derivative"] = {"max_residual": rest_error, "step": step}

for am in [4., 8., 16.]:
    w = lambda k: np.sqrt(1+(k/am)**2)
    weight = lambda k: k*k*np.exp(-k*k)/w(k)
    denominator, denominator_error = quad(weight, 0, np.inf, epsabs=2e-12, epsrel=2e-12)
    functions = {
        "minimal": (lambda k: (2*w(k)+1)/(3*w(k)**2), 1-1/am**2, 4.),
        "pauli_coefficient": (lambda k: (2*w(k)+1)/(3*w(k)), 1-1/(4*am**2), 1.),
        "orbital_coefficient": (lambda k: 1/w(k), 1-3/(4*am**2), 3.),
    }
    entry = {"am": am, "normalization_radial_integral": denominator,
             "estimated_denominator_error": denominator_error, "values": {}}
    for name, (f, leading, tolerance) in functions.items():
        numerator, err = quad(lambda k: weight(k)*f(k), 0, np.inf,
                              epsabs=2e-12, epsrel=2e-12)
        value = numerator/denominator
        scaled = abs(value-leading)*am**4
        assert scaled < tolerance
        entry["values"][name] = {
            "normalized_quadrature": value, "rest_plus_first_width_term": leading,
            "am4_times_absolute_difference": scaled,
            "acceptance_scaled_tolerance": tolerance,
            "estimated_numerator_error": err,
            "note": "Tolerance checks tested asymptotic scaling only; it is not a universal analytic bound."}
    report["gaussian_width"].append(entry)
report["comparison_groups"] = 4+6+1+9
report["status"] = "pass"
(Path(__file__).resolve().parents[2] / "checks/srednicki/magnetic64-check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
print(json.dumps(report, ensure_ascii=False, indent=2))
