#!/usr/bin/env python3
"""New finite checks for C62.19, C62.33 and C62.39; no old checks imported."""
from pathlib import Path
import json
import platform
import numpy as np
import scipy
from scipy.integrate import quad

report = {
    "scope": "Three positive spacelike bubble integrals, three finite IR regulators, "
             "four matrix components of the finite vertex numerator",
    "software": {"Python": platform.python_version(),
                 "NumPy": np.__version__, "SciPy": scipy.__version__},
    "conventions": "g=(-,+,+,+), Clifford=-2g; Dirac matrix basis for an identity "
                   "independent of the book's spinor basis; all test vectors real",
    "bubble": [], "infrared": [], "vertex_numerator": {},
    "physics_certification": False,
}
for z in [0.05, 3.0, 200.0]:
    val, err = quad(lambda x: x*(1-x)*np.log1p(z*x*(1-x)),
                    0, 1, epsabs=2e-13, epsrel=2e-13)
    v = np.sqrt(z/(z+4))
    closed = .5*(1-1/(3*v*v))*(np.arctanh(v)/v-1)+1/18
    residual = abs(val-closed)
    assert residual < 2e-12
    report["bubble"].append({"k2_over_m2": z, "quadrature": val,
                             "estimated_quadrature_error": err,
                             "closed": closed, "absolute_residual": residual})

for a in [.1, .02, .004]:
    f = lambda x: x*(1-x*x)/(x*x+a*a*(1-x))
    low, e1 = quad(f, 0, a, epsabs=2e-12, epsrel=2e-12)
    high, e2 = quad(f, a, 1, epsabs=2e-12, epsrel=2e-12)
    kappa = -2*(low+high)
    leading = 2*np.log(a)+1
    bound = a*a*np.log((1+a*a)/(a*a))+np.log1p(a*a)+16*a/3
    remainder = kappa-leading
    assert -bound <= remainder <= 2e-12
    report["infrared"].append({"m_gamma_over_m": a, "kappa_quadrature": kappa,
                              "estimated_quadrature_error": 2*(e1+e2),
                              "log_plus_constant": leading, "remainder": remainder,
                              "analytic_remainder_absolute_bound": bound})

I2 = np.eye(2, dtype=complex)
O2 = np.zeros((2, 2), dtype=complex)
pauli = [np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.array([[1, 0], [0, -1]], complex)]
gamma = [np.block([[I2, O2], [O2, -I2]])]
gamma += [np.block([[O2, s], [-s, O2]]) for s in pauli]
metric = np.array([-1., 1., 1., 1.])
slash = lambda p: sum(metric[i]*p[i]*gamma[i] for i in range(4))
a = np.array([.7, -.2, .4, 1.1])
b = np.array([-.3, .9, .2, -.6])
m = 1.3
I4 = np.eye(4)
residuals = []
for mu in range(4):
    lhs = sum(metric[nu]*gamma[nu] @ (slash(a)+m*I4) @ gamma[mu]
              @ (slash(b)+m*I4) @ gamma[nu] for nu in range(4))
    rhs = 2*slash(b) @ gamma[mu] @ slash(a) \
          + 4*m*(a[mu]+b[mu])*I4 + 2*m*m*gamma[mu]
    residual = float(np.max(np.abs(lhs-rhs)))
    assert residual < 3e-13
    residuals.append(residual)
report["vertex_numerator"] = {"a_contravariant": a.tolist(),
                              "b_contravariant": b.tolist(), "mass": m,
                              "component_max_residuals": residuals}
report["status"] = "pass"
report["comparison_groups"] = 10
out = Path(__file__).resolve().parents[2] / "checks/srednicki/loops62-check.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
print(json.dumps(report, ensure_ascii=False, indent=2))
