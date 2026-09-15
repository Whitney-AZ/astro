#!/usr/bin/env python3
"""One new S51 finite check: zero-momentum Yukawa vertex subtraction.

Compare the source three-denominator parameter numerator (including its
finite -1/2 term in units g^3/(16*pi^2)) with a convergent Euclidean radial
mass subtraction and an independently integrated two-denominator form.
No old Gaussian, Clifford, or loop check is imported or run.
"""
import datetime
import hashlib
import json
import math
import pathlib
import platform

import scipy
from scipy.integrate import quad


CASES = [
    {"name": "two_distinct_masses", "A_m_squared": 0.64, "B_M_squared": 1.21, "C_mu_squared": 0.9},
    {"name": "light_pseudoscalar", "A_m_squared": 2.25, "B_M_squared": 0.36, "C_mu_squared": 1.0},
    {"name": "equal_mass_removable_limit", "A_m_squared": 1.44, "B_M_squared": 1.44, "C_mu_squared": 0.81},
]
TOLERANCE = 2e-11
OPTIONS = {"epsabs": 3e-13, "epsrel": 3e-13, "limit": 100}


def integrate(function, low=0.0, high=1.0):
    value, estimate = quad(function, low, high, **OPTIONS)
    return value, estimate


def simplex(function):
    inner_error = []

    def outer(x1):
        value, err = integrate(lambda x2: function(x1, x2), 0.0, 1.0 - x1)
        inner_error.append(err)
        return 2.0 * value

    value, err = integrate(outer)
    return value, {"outer_quad_error_estimate": err,
                   "largest_inner_quad_error_estimate": max(inner_error)}


def run(case):
    a, b, c = (case[k] for k in ("A_m_squared", "B_M_squared", "C_mu_squared"))
    # D_* = (x1+x2)m^2 + (1-x1-x2)M^2; dF3 = 2 dx1 dx2.
    d0 = lambda x1, x2: a * (x1 + x2) + b * (1.0 - x1 - x2)
    log3, err_log3 = simplex(lambda x1, x2: math.log(d0(x1, x2) / c))
    inv3, err_inv3 = simplex(lambda x1, x2: 1.0 / d0(x1, x2))
    source_finite = -0.5 - log3 + 0.5 * a * inv3

    # The original numerator at p=p'=0 cancels one fermion denominator.
    two_parameter, err_two = integrate(lambda x: -math.log((a * x + b * (1.0 - x)) / c))
    if a == b:
        closed = -math.log(a / c)
    else:
        closed = 1.0 - (a * math.log(a / c) - b * math.log(b / c)) / (a - b)

    # Direct, absolutely convergent radial difference:
    # int_0^infty t[1/((t+a)(t+b))-1/(t+c)^2]dt.
    # Set t=c*u/(1-u) and combine the rational difference before evaluation.
    def radial(u):
        numerator = u * ((2.0 * c - a - b) * c * u + (c * c - a * b) * (1.0 - u))
        denominator = (a + (c - a) * u) * (b + (c - b) * u)
        return numerator / denominator

    radial_value, err_radial = integrate(radial)
    values = [source_finite, two_parameter, radial_value]
    errors = [abs(x - closed) / max(1.0, abs(x), abs(closed)) for x in values]
    return {
        "input": case,
        "three_parameter_log": log3,
        "three_parameter_inverse_mass": inv3,
        "source_51_47_finite_part": source_finite,
        "cancelled_two_parameter_integral": two_parameter,
        "convergent_radial_subtraction": radial_value,
        "analytic_closed_form": closed,
        "maximum_scaled_error": max(errors),
        "omit_source_finite_minus_half_residual": source_finite + 0.5 - closed,
        "quadrature_error_estimates": {"log3": err_log3, "inv3": err_inv3,
                                       "two_parameter": err_two, "radial": err_radial},
    }


def main():
    cases = [run(case) for case in CASES]
    error = max(x["maximum_scaled_error"] for x in cases)
    data = {
        "execution_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "software": {"python": platform.python_version(), "scipy": scipy.__version__,
                     "platform": platform.platform()},
        "program_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "assumptions": {
            "model": "Dirac pseudoscalar Yukawa, vertex -g gamma5, metric (-+++)",
            "positive_masses": "A=m^2>0, B=M^2>0, C=mu^2>0; M<2m in all cases",
            "momentum": "p=p'=0, off-shell subtraction point",
            "loop_normalization": "compare finite coefficient in units g^3 gamma5/(16*pi^2)",
            "dimension": "d=4-epsilon, g_d=g mu_tilde^(epsilon/2); common vertex mu_tilde^(epsilon/2) stripped",
            "scale": "mu^2=4*pi*exp(-gamma_E)*mu_tilde^2",
            "radial_measure": "d4q_E/(2*pi)^4 = t dt/(16*pi^2), t=q_E^2",
            "scope": "finite mass-subtracted integral only; does not numerically verify a divergent unregulated integral",
        },
        "quadrature_options": OPTIONS,
        "tolerance": TOLERANCE,
        "maximum_scaled_error": error,
        "passed": error <= TOLERANCE,
        "cases": cases,
    }
    target = pathlib.Path("checks/srednicki/zero-vertex51-check.json")
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(target), "passed": data["passed"],
                      "maximum_scaled_error": error, "software": data["software"]},
                     ensure_ascii=False))
    if not data["passed"]:
        raise SystemExit("S51 finite zero-vertex check failed; inspect saved results.")


if __name__ == "__main__":
    main()
