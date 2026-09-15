#!/usr/bin/env python3
"""One bounded numerical matrix check of the new S75 triangle algebra.

Run: python3 scripts/srednicki/check_triangle75.py

Matrices are constructed in the book's Weyl basis, with metric (-+++),
{gamma^mu,gamma^nu}=-2g^{mu nu}, gamma5=i gamma0 gamma1 gamma2 gamma3,
epsilon^{0123}=1, and slash(v)=v_mu gamma^mu. The three points below are
fixed integer OFF-SHELL vectors, not a scan and not loop quadrature.

For all free Lorentz components at these points this directly checks the
odd numerator, its reflected second orientation, p/q/r contractions, and
the three six-gamma contractions. The source (75.45) comparison uses the
known p-leg surface expression and the exact p/q exchange of the full
two-orientation amplitude. No ultraviolet surface integral is evaluated.
The factor in the single-diagram shift uses source (75.49) as an analytic
input; this program checks only its gamma contraction and i factors.
"""

from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path
import platform
import sys

import numpy as np


METRIC = np.array([-1, 1, 1, 1], dtype=np.int64)
I2 = np.eye(2, dtype=np.complex128)
ZERO2 = np.zeros((2, 2), dtype=np.complex128)
PAULI = [
    np.array([[0, 1], [1, 0]], dtype=np.complex128),
    np.array([[0, -1j], [1j, 0]], dtype=np.complex128),
    np.array([[1, 0], [0, -1]], dtype=np.complex128),
]
GAMMA = [np.block([[ZERO2, I2], [I2, ZERO2]])]
GAMMA += [np.block([[ZERO2, sigma], [-sigma, ZERO2]]) for sigma in PAULI]
GAMMA5 = 1j * GAMMA[0] @ GAMMA[1] @ GAMMA[2] @ GAMMA[3]
TOLERANCE = 1e-10
POINTS = [
    {"p": [2, 1, -1, 3], "q": [1, -2, 2, 1], "ell": [5, 2, 1, -1]},
    {"p": [1, 3, 1, -2], "q": [2, -1, 2, 2], "ell": [4, 1, -3, 2]},
    {"p": [3, -2, 1, 1], "q": [1, 2, -3, 2], "ell": [6, -1, 2, 4]},
]


def epsilon(*indices):
    if len(set(indices)) < 4:
        return 0
    inversions = sum(indices[a] > indices[b] for a in range(4) for b in range(a + 1, 4))
    return (-1) ** inversions


def lower(vector):
    return METRIC * vector


def square(vector):
    return int(np.dot(lower(vector), vector))


def slash(vector):
    return sum((component * gamma for component, gamma in zip(lower(vector), GAMMA)),
               np.zeros((4, 4), dtype=np.complex128))


def odd_numerator(p, q, ell):
    """Source (75.18), computed solely as explicit matrix products."""
    left, middle, right = slash(ell - p), slash(ell), slash(ell + q)
    result = np.empty((4, 4, 4), dtype=np.complex128)
    for mu, nu, rho in itertools.product(range(4), repeat=3):
        result[mu, nu, rho] = np.trace(
            left @ GAMMA[mu] @ middle @ GAMMA[nu] @ right @ GAMMA[rho] @ GAMMA5
        ) / 2
    return result


def epsilon_contraction_rhs(p, q, ell):
    """Analytic RHS, formed independently by index sums, without gamma matrices."""
    p_low, q_low, ell_low = lower(p), lower(q), lower(ell)
    ell_minus_p_low, p_plus_q_low = lower(ell - p), lower(p + q)
    ell2, left2, right2 = square(ell), square(ell - p), square(ell + q)
    p_rhs = np.zeros((4, 4), dtype=np.complex128)
    q_rhs = np.zeros((4, 4), dtype=np.complex128)
    r_rhs = np.zeros((4, 4), dtype=np.complex128)
    for first, second, alpha, beta in itertools.product(range(4), repeat=4):
        p_rhs[first, second] += -2j * epsilon(alpha, first, beta, second) * (
            left2 * ell_low[alpha] * q_low[beta]
            - ell2 * ell_minus_p_low[alpha] * p_plus_q_low[beta]
        )
        q_rhs[first, second] += 2j * epsilon(alpha, first, beta, second) * (
            right2 * ell_low[alpha] * p_low[beta]
            - ell2 * ell_minus_p_low[alpha] * p_plus_q_low[beta]
        )
        r_rhs[first, second] += 2j * epsilon(alpha, second, beta, first) * (
            right2 * ell_low[alpha] * p_low[beta]
            + left2 * ell_low[alpha] * q_low[beta]
        )
    return {"p": p_rhs, "q": q_rhs, "r": r_rhs}


@lru_cache(maxsize=None)
def six_gamma_trace(alpha, mu, beta, nu, gamma, rho):
    return np.trace(GAMMA[alpha] @ GAMMA[mu] @ GAMMA[beta] @ GAMMA[nu]
                    @ GAMMA[gamma] @ GAMMA[rho] @ GAMMA5)


def six_gamma_contractions(a):
    a_low = lower(a)
    terms = np.zeros((3, 4, 4, 4), dtype=np.complex128)
    expected = np.zeros((4, 4, 4), dtype=np.complex128)
    for mu, nu, rho in itertools.product(range(4), repeat=3):
        for alpha, beta, gamma in itertools.product(range(4), repeat=3):
            weights = (
                a_low[alpha] * METRIC[beta] * int(beta == gamma),
                a_low[beta] * METRIC[gamma] * int(gamma == alpha),
                a_low[gamma] * METRIC[alpha] * int(alpha == beta),
            )
            if any(weights):
                trace = six_gamma_trace(alpha, mu, beta, nu, gamma, rho)
                for term, weight in enumerate(weights):
                    terms[term, mu, nu, rho] += weight * trace
        expected[mu, nu, rho] = 8j * sum(
            epsilon(mu, nu, rho, delta) * a_low[delta] for delta in range(4)
        )
    return terms, expected


def complex_pair(number):
    value = complex(number)
    return [float(value.real), float(value.imag)]


def compare(actual, expected):
    difference = actual - expected
    index = np.unravel_index(int(np.argmax(np.abs(actual))), actual.shape)
    maximum = float(np.max(np.abs(difference)))
    return {
        "components_checked": int(actual.size),
        "max_abs_residual": maximum,
        "pass": maximum <= TOLERANCE,
        "nonzero_actual_components": int(np.count_nonzero(actual)),
        "largest_actual_component_witness": {
            "indices": [int(component) for component in index],
            "actual_real_imag": complex_pair(actual[index]),
            "expected_real_imag": complex_pair(expected[index]),
        },
    }


def determinant3(matrix):
    a, b, c = [[int(entry) for entry in row] for row in matrix]
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def source_75_45_comparison(p, q):
    """Compare kernels after removing the common i*g^3/(8*pi^2).

    The p-leg input is eps^{alpha nu beta rho} p_alpha q_beta (75.44).
    Exchanging the uncontracted p,mu and q,nu labels gives q_from_exchange.
    Source (75.45) prints the other epsilon order with a PLUS sign.
    """
    p_low, q_low = lower(p), lower(q)
    q_from_exchange = np.zeros((4, 4), dtype=np.complex128)
    literal_printed = np.zeros((4, 4), dtype=np.complex128)
    for mu, rho, alpha, beta in itertools.product(range(4), repeat=4):
        q_from_exchange[mu, rho] += epsilon(alpha, mu, beta, rho) * q_low[alpha] * p_low[beta]
        literal_printed[mu, rho] += epsilon(alpha, rho, beta, mu) * q_low[alpha] * p_low[beta]
    return {
        "common_factor_removed": "i*g^3/(8*pi^2)",
        "corrected_minus_printed_epsilon": compare(q_from_exchange, -literal_printed),
        "literal_plus_printed_epsilon": compare(q_from_exchange, literal_printed),
        "interpretation": "The printed PLUS sign fails for all chosen nondegenerate momenta; with its epsilon order the coefficient must be negative. The analytic surface input (75.44) is not recomputed by this finite check.",
    }


def main():
    script = Path(__file__).resolve()
    output = script.parents[2] / "checks/srednicki/triangle75-check.json"
    identity = np.eye(4, dtype=np.complex128)
    clifford_residual = max(float(np.max(np.abs(
        GAMMA[mu] @ GAMMA[nu] + GAMMA[nu] @ GAMMA[mu]
        + 2 * METRIC[mu] * int(mu == nu) * identity
    ))) for mu, nu in itertools.product(range(4), repeat=2))
    orientation_trace = np.trace(GAMMA5 @ GAMMA[0] @ GAMMA[1] @ GAMMA[2] @ GAMMA[3])
    setup_pass = bool(clifford_residual == 0 and orientation_trace == -4j)
    point_results = []
    all_pass = setup_pass
    for number, point in enumerate(POINTS, 1):
        p, q, ell = [np.array(point[name], dtype=np.int64) for name in ("p", "q", "ell")]
        r, a = -p - q, p - q
        numerator = odd_numerator(p, q, ell)
        reflected_second = odd_numerator(q, p, -ell).transpose(1, 0, 2)
        reflection = compare(reflected_second, numerator)
        direct = {
            "p": np.einsum("m,mnr->nr", lower(p), numerator),
            "q": np.einsum("n,mnr->mr", lower(q), numerator),
            "r": np.einsum("r,mnr->mn", lower(r), numerator),
        }
        rhs = epsilon_contraction_rhs(p, q, ell)
        contractions = {leg: compare(direct[leg], rhs[leg]) for leg in ("p", "q", "r")}
        terms, expected_trace = six_gamma_contractions(a)
        traces = [compare(term, expected_trace) for term in terms]
        # (i/2)*(i/192)*sum(trace terms), with pi^-2 g^3 suppressed.
        shift = compare(-sum(terms) / 384, -expected_trace / 128)
        source_sign = source_75_45_comparison(p, q)
        virtualities = {
            "p_squared": square(p), "q_squared": square(q), "r_squared": square(r),
            "ell_squared": square(ell), "ell_minus_p_squared": square(ell - p),
            "ell_plus_q_squared": square(ell + q),
        }
        minor = determinant3([p[:3], q[:3], ell[:3]])
        first_denominator = square(ell - p) * square(ell) * square(ell + q)
        second_denominator = square(-ell - q) * square(-ell) * square(-ell + p)
        point_pass = (all(value != 0 for value in virtualities.values()) and minor != 0
                      and first_denominator == second_denominator and reflection["pass"]
                      and all(item["pass"] for item in contractions.values())
                      and all(item["pass"] for item in traces) and shift["pass"]
                      and source_sign["corrected_minus_printed_epsilon"]["pass"]
                      and not source_sign["literal_plus_printed_epsilon"]["pass"])
        all_pass = all_pass and point_pass
        point_results.append({
            "point_number": number,
            "contravariant_vectors_t_x_y_z": {**point, "r": r.tolist(), "a": a.tolist()},
            "covariant_vectors": {name: lower(vector).tolist() for name, vector in
                                  (("p", p), ("q", q), ("ell", ell), ("r", r), ("a", a))},
            "virtualities": virtualities,
            "nonzero_3_by_3_minor_of_p_q_ell_first_three_columns": minor,
            "first_denominator": first_denominator,
            "reflected_second_denominator": second_denominator,
            "odd_trace_reflection": reflection,
            "contracted_numerator_checks": contractions,
            "six_gamma_contractions_in_source_75_49_order": traces,
            "single_diagram_shift_pi_squared_over_g_cubed": shift,
            "source_75_45_sign": source_sign,
            "all_checks_pass": point_pass,
        })
    result = {
        "execution": {
            "utc_time": datetime.now(timezone.utc).isoformat(),
            "command": "python3 scripts/srednicki/check_triangle75.py",
            "actual_argv": sys.argv, "cwd": str(Path.cwd()),
            "python_version": sys.version, "python_executable": sys.executable,
            "numpy_version": np.__version__, "platform": platform.platform(),
            "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        },
        "conventions": {
            "ledger": "src/content/posts/Srednicki-75.md, equations 75.8 and 75.15-75.30",
            "metric_diagonal": METRIC.tolist(),
            "clifford": "{gamma^mu,gamma^nu}=-2*g^{mu nu}*I4",
            "gamma_basis": "gamma0=[[0,I],[I,0]]; gammai=[[0,sigma_i],[-sigma_i,0]]",
            "gamma5": "i*gamma0*gamma1*gamma2*gamma3 = diag(-1,-1,1,1)",
            "epsilon": "epsilon^{0123}=+1; vectors contracted with upper epsilon are lowered",
            "momenta": "p,q,r all outgoing; r=-p-q; slash(v)=v_mu*gamma^mu",
            "N": "(1/2)tr[slash(ell-p) gamma^mu slash(ell) gamma^nu slash(ell+q) gamma^rho gamma5]",
            "reflected_second_orientation": "N^{nu mu rho}(q,p,-ell) = N^{mu nu rho}(p,q,ell)",
            "p_rhs": "-2i eps^{a nu b rho}[(ell-p)^2 ell_a q_b-ell^2(ell-p)_a(p+q)_b]",
            "q_rhs": "+2i eps^{a mu b rho}[(ell+q)^2 ell_a p_b-ell^2(ell-p)_a(p+q)_b]",
            "r_rhs": "+2i eps^{a nu b mu}[(ell+q)^2 ell_a p_b+(ell-p)^2 ell_a q_b]",
            "six_trace_weights": ["a_alpha*g_beta_gamma", "a_beta*g_gamma_alpha", "a_gamma*g_alpha_beta"],
            "six_trace_target_each": "8i*epsilon^{mu nu rho delta}*a_delta",
            "single_diagram_shift_target": "delta V*pi^2/g^3 = -i*epsilon^{mu nu rho delta}*a_delta/16",
            "complex_witness_encoding": "[real part, imaginary part]",
            "dtype": "numpy.complex128", "absolute_tolerance": TOLERANCE,
        },
        "input_matrix_calibration": {
            "clifford_max_abs_residual": clifford_residual,
            "gamma5_trace_0123_real_imag": complex_pair(orientation_trace),
            "gamma5_diagonal": [complex_pair(value) for value in np.diag(GAMMA5)],
            "pass": setup_pass,
        },
        "points": point_results,
        "scope": {
            "primary_source": "Chinese PDF303-310; current review details are in checks/srednicki/reviews/75.md",
            "checks": "Three fixed nondegenerate integer points; every free Lorentz component of stated tensors; explicit matrix traces versus independently formed epsilon sums",
            "analytic_inputs_not_computationally_verified": "Regulated surface integrals (75.42)-(75.44) and (75.49); common UV/IR prescription; no dimension continuation of gamma5",
            "interpretation": "Finite matrix evidence for these triangle identities and the source (75.45) sign correction, not a proof for all momenta or an anomaly nonrenormalization theorem",
            "adapted_source_program": "/Users/Admin/Documents/Srednicki-QFT-Trans/checks/s75_triangle_check.py",
            "adapted_source_sha256": "05b671e6071cd835efc90c6a6c27badd193c13b62df120614291243f9b1d0735",
        },
        "all_checks_pass": all_pass,
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print("Input gamma calibration:", setup_pass, "Clifford residual:", clifford_residual)
    for entry in point_results:
        contractions = entry["contracted_numerator_checks"]
        print("point", entry["point_number"], "reflection",
              entry["odd_trace_reflection"]["max_abs_residual"],
              "p/q/r", [contractions[leg]["max_abs_residual"] for leg in ("p", "q", "r")],
              "six traces", [item["max_abs_residual"] for item in entry["six_gamma_contractions_in_source_75_49_order"]],
              "printed75.45 residual", entry["source_75_45_sign"]["literal_plus_printed_epsilon"]["max_abs_residual"])
    print("All corrected checks pass:", all_pass)
    print("Results:", output)
    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
