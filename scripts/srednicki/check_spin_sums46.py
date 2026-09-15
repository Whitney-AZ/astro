#!/usr/bin/env python3
"""Section 46 calculation: explicit spin amplitudes vs ordered traces/invariants.

No pre-existing S38 check is imported or rerun. Spinors use the source38
rest phases and positive-mass boost. Independent rotations of the complete
external spin bases make the polarized interference terms complex.
All matrix operations below are ordinary complex-number linear algebra.
"""
import collections
import datetime
import hashlib
import itertools
import json
import math
import pathlib
import platform
import sys

import numpy as np

I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
PAULI = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
]
BETA = np.block([[Z2, I2], [I2, Z2]])
GAMMA = [BETA] + [np.block([[Z2, s], [-s, Z2]]) for s in PAULI]
GAMMA5 = np.diag([-1, -1, 1, 1]).astype(complex)
EPSILON_LOWER = np.array([[0, -1], [1, 0]], dtype=complex)
TOLERANCE = 1e-8
comparisons = []


def dot(p, q):
    return -p[0] * q[0] + np.dot(p[1:], q[1:])


def slash(p):
    return -p[0] * GAMMA[0] + sum(
        (p[j] * GAMMA[j] for j in range(1, 4)),
        np.zeros((4, 4), dtype=complex),
    )


def bar(w):
    return w.conj().T @ BETA


def adjoint(A):
    return BETA @ A.conj().T @ BETA


def basis_rotation(theta, phi):
    c, s = math.cos(theta / 2), math.sin(theta / 2)
    phase = np.exp(1j * phi)
    return np.array([[c, -phase.conjugate() * s], [phase * s, c]], dtype=complex)


def spinors(p, m, antiparticle=False, rotation=None):
    # exp(i eta phat.K) = [(E+m)I + gamma0 gamma.p]/sqrt[2m(E+m)].
    spatial_slash = sum(
        (p[j] * GAMMA[j] for j in range(1, 4)),
        np.zeros((4, 4), dtype=complex),
    )
    boost = ((p[0] + m) * I4 + BETA @ spatial_slash) / math.sqrt(
        2 * m * (p[0] + m)
    )
    rest = (
        np.vstack([EPSILON_LOWER, -EPSILON_LOWER])
        if antiparticle
        else np.vstack([I2, I2])
    ) * math.sqrt(m)
    result = boost @ rest
    if rotation is not None:
        result = result @ basis_rotation(*rotation)
    return result


def spin_axis(p, m):
    # Same rotation-free Lorentz boost of z_rest=(0,0,0,1) as source38.
    z = np.zeros(4)
    z[0] = p[3] / m
    z[1:] = np.array([0.0, 0.0, 1.0]) + p[1:] * p[3] / (m * (p[0] + m))
    return z


def cm_vectors(m1, m2, q, theta, phi):
    ei, ej = math.hypot(m1, q), math.hypot(m2, q)
    n = np.array(
        [math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)]
    )
    return (
        np.array([ei, 0.0, 0.0, q]),
        np.array([ej, 0.0, 0.0, -q]),
        np.r_[ei, q * n],
        np.r_[ej, -q * n],
    )


def compare(category, case, actual, expected):
    actual, expected = complex(actual), complex(expected)
    err = abs(actual - expected) / max(1.0, abs(actual), abs(expected))
    comparisons.append({"category": category, "case": case, "error": float(err)})
    return float(err)


def real_value(x):
    return float(complex(x).real)


def electron_scalar(case):
    name, g, m, M, q, theta, phi = case
    p, k, pp, kp = cm_vectors(m, M, q, theta, phi)
    s, t, u = -dot(p + k, p + k), -dot(p - pp, p - pp), -dot(p - kp, p - kp)
    ds, du = m * m - s, m * m - u
    F = lambda r: (-slash(r) + m * I4) / (dot(r, r) + m * m)
    original = g * g * (F(p + k) + F(p - kp))
    a = 2 * m * (1 / ds + 1 / du)
    b = -k / ds + kp / du
    A = g * g * (a * I4 + slash(b))
    Abar = adjoint(A)
    U, Up = spinors(p, m), spinors(pp, m)
    P, Pp = -slash(p) + m * I4, -slash(pp) + m * I4
    z, zp = spin_axis(p, m), spin_axis(pp, m)
    direct_sum = 0.0
    polarized_errors = []
    largest_amplitude_imag = 0.0
    for i, j in itertools.product(range(2), repeat=2):
        amplitude = bar(Up[:, j]) @ original @ U[:, i]
        reduced = bar(Up[:, j]) @ A @ U[:, i]
        compare("electron_original_vs_on_shell_reduced", name, amplitude, reduced)
        sigma, sigmap = 1 - 2 * i, 1 - 2 * j
        polarized_trace = 0.25 * np.trace(
            (I4 - sigmap * GAMMA5 @ slash(zp))
            @ Pp
            @ A
            @ (I4 - sigma * GAMMA5 @ slash(z))
            @ P
            @ Abar
        )
        polarized_errors.append(
            compare("electron_polarized_trace", name, abs(amplitude) ** 2, polarized_trace)
        )
        direct_sum += abs(amplitude) ** 2 / 2
        largest_amplitude_imag = max(largest_amplitude_imag, abs(amplitude.imag))
    trace_average = 0.5 * np.trace(Pp @ A @ P @ Abar)
    # Independently contracted two/four-gamma expression, without matrix traces.
    x, y = dot(p, b), dot(pp, b)
    contracted = 2 * g**4 * (
        a * a * (m * m - dot(pp, p))
        + 2 * a * m * (x + y)
        + 2 * x * y
        - (dot(pp, p) + m * m) * dot(b, b)
    )
    compare("electron_unpolarized_trace", name, direct_sum, trace_average)
    compare("electron_scalar_contraction", name, direct_sum, contracted)
    return {
        "name": name,
        "parameters": {"g": g, "m": m, "M": M, "q_cm": q, "theta": theta, "phi": phi},
        "four_momenta": dict(zip(["p", "k", "pprime", "kprime"], [v.tolist() for v in (p, k, pp, kp)])),
        "mandelstam": {"s": float(s), "t": float(t), "u": float(u)},
        "explicit_4_spin_amplitudes_averaged": float(direct_sum),
        "trace_average": real_value(trace_average),
        "scalar_contraction": float(contracted),
        "max_polarized_normalized_error": max(polarized_errors),
        "largest_imaginary_spin_amplitude": float(largest_amplitude_imag),
        "threshold_exact_expectation": 0.0 if q == 0 else None,
    }


BASIS_ROTATIONS = [(0.31, 0.82), (1.11, -0.44), (0.71, 1.37), (1.43, -0.93)]


def pair_scattering(case):
    name, g, m, M, q, theta, phi = case
    p1, p2, p3, p4 = cm_vectors(m, m, q, theta, phi)
    s, t, u = -dot(p1 + p2, p1 + p2), -dot(p1 - p3, p1 - p3), -dot(p1 - p4, p1 - p4)
    dt, ds = M * M - t, M * M - s
    U1 = spinors(p1, m, rotation=BASIS_ROTATIONS[0])
    V2 = spinors(p2, m, True, BASIS_ROTATIONS[1])
    U3 = spinors(p3, m, rotation=BASIS_ROTATIONS[2])
    V4 = spinors(p4, m, True, BASIS_ROTATIONS[3])
    direct_sum = 0.0
    max_polarized_error, max_interference_imag = 0.0, 0.0
    for i, j, k, l in itertools.product(range(2), repeat=4):
        u1, v2, u3, v4 = U1[:, i], V2[:, j], U3[:, k], V4[:, l]
        direct = (bar(u3) @ u1) * (bar(v2) @ v4)
        annihilation = (bar(v2) @ u1) * (bar(u3) @ v4)
        # Fock ordering b1dag d2dag used in the website article.
        amplitude = -g * g * (direct / dt - annihilation / ds)
        P1, Q2, P3, Q4 = [np.outer(w, bar(w)) for w in [u1, v2, u3, v4]]
        cross1 = np.trace(P1 @ Q2 @ Q4 @ P3)
        cross2 = np.trace(P1 @ P3 @ Q4 @ Q2)
        compare("pair_ordered_interference1", name, cross1, direct * annihilation.conjugate())
        compare("pair_ordered_interference2", name, cross2, annihilation * direct.conjugate())
        polarized = g**4 * (
            np.trace(P1 @ P3) * np.trace(Q4 @ Q2) / dt**2
            + np.trace(P1 @ Q2) * np.trace(Q4 @ P3) / ds**2
            - cross1 / (dt * ds)
            - cross2 / (ds * dt)
        )
        err = compare("pair_polarized_four_term_trace", name, abs(amplitude) ** 2, polarized)
        max_polarized_error = max(max_polarized_error, err)
        max_interference_imag = max(max_interference_imag, abs(cross1.imag))
        direct_sum += abs(amplitude) ** 2 / 4
    P1, Q2 = -slash(p1) + m * I4, -slash(p2) - m * I4
    P3, Q4 = -slash(p3) + m * I4, -slash(p4) - m * I4
    cross1 = np.trace(P1 @ Q2 @ Q4 @ P3)
    cross2 = np.trace(P1 @ P3 @ Q4 @ Q2)
    trace_average = g**4 / 4 * (
        np.trace(P1 @ P3) * np.trace(Q4 @ Q2) / dt**2
        + np.trace(P1 @ Q2) * np.trace(Q4 @ P3) / ds**2
        - (cross1 + cross2) / (dt * ds)
    )
    # Independently reduced invariant expression from the report's Clifford algebra.
    invariant = g**4 * (
        (4 * m * m - t) ** 2 / dt**2
        + (s - 4 * m * m) ** 2 / ds**2
        + (s * t - 4 * m * m * u) / (dt * ds)
    )
    compare("pair_unpolarized_trace", name, direct_sum, trace_average)
    compare("pair_mandelstam_reduction", name, direct_sum, invariant)
    heavy_leading = (
        g**4 / M**4 * ((4 * m * m - t) ** 2 + (s - 4 * m * m) ** 2 + s * t - 4 * m * m * u)
        if M > 0
        else None
    )
    return {
        "name": name,
        "parameters": {"g": g, "m": m, "M": M, "q_cm": q, "theta": theta, "phi": phi},
        "four_momenta": dict(zip(["p1", "p2", "p1prime", "p2prime"], [v.tolist() for v in (p1, p2, p3, p4)])),
        "mandelstam": {"s": float(s), "t": float(t), "u": float(u)},
        "explicit_16_spin_amplitudes_averaged": float(direct_sum),
        "trace_average": real_value(trace_average),
        "mandelstam_expression": float(invariant),
        "max_polarized_normalized_error": max_polarized_error,
        "max_imaginary_polarized_interference_trace": float(max_interference_imag),
        "unpolarized_interference_traces": [real_value(cross1), real_value(cross2)],
        "threshold_exact_expectation": 16 * g**4 * m**4 / M**4 if q == 0 else None,
        "massless_M0_tree_value": 3 * g**4 if M == 0 else None,
        "relative_difference_from_massless_M0_limit": abs(direct_sum / (3 * g**4) - 1) if M == 0 else None,
        "heavy_kernel_leading_value": float(heavy_leading) if name == "pair_heavy_scalar" else None,
        "relative_heavy_correction": abs(direct_sum / heavy_leading - 1) if name == "pair_heavy_scalar" else None,
        "s_over_M2": float(s / M**2) if name == "pair_heavy_scalar" else None,
    }


def main():
    electron_cases = [
        ("electron_generic", 0.7, 1.0, 0.6, 0.8, 1.1, 0.73),
        ("electron_threshold", 0.5, 1.0, 0.5, 0.0, 0.7, 1.2),
        ("electron_high_energy", 0.8, 1.0, 0.5, 25.0, 1.27, 0.51),
    ]
    pair_cases = [
        ("pair_generic", 0.7, 1.0, 0.6, 0.8, 1.1, 0.73),
        ("pair_threshold", 0.5, 1.0, 0.7, 0.0, 0.9, 0.6),
        ("pair_heavy_scalar", 0.6, 1.0, 50.0, 1.3, 0.81, 0.42),
        ("pair_near_massless", 0.65, 1e-5, 0.0, 1.7, 0.83, 1.29),
    ]
    results_e = [electron_scalar(c) for c in electron_cases]
    results_p = [pair_scattering(c) for c in pair_cases]
    by_category = collections.defaultdict(list)
    for c in comparisons:
        by_category[c["category"]].append(c["error"])
    failures = [c for c in comparisons if c["error"] > TOLERANCE]
    output = {
        "status": "pass" if not failures else "fail",
        "executed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "python_version": sys.version,
        "numpy_version": np.__version__,
        "platform": platform.platform(),
        "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "random_seed": None,
        "sampling": "Seven fully specified deterministic kinematic points; no random draws.",
        "conventions": {
            "metric": "(-,+,+,+)",
            "gamma_anticommutator": "-2g",
            "slash": "-p0 gamma0 + pi gammai",
            "rest_spinors": "u=sqrt(m)(e,e), v=sqrt(m)(E e,-E e), E=[[0,-1],[1,0]]",
            "spinors": "Source38 rotation-free boost; no prior spinor-check script imported or rerun.",
            "pair_basis_rotations_theta_phi": BASIS_ROTATIONS,
            "propagators": "Real off-pole tree denominators; no finite width or absorptive part.",
            "spin_average": "1/2 for one unpolarized initial fermion;1/4 for independent unpolarized pair.",
        },
        "normalized_error_definition": "abs(actual-expected)/max(1,abs(actual),abs(expected))",
        "tolerance": TOLERANCE,
        "scalar_comparisons": len(comparisons),
        "max_normalized_error": max(c["error"] for c in comparisons),
        "categories": {
            k: {"count": len(v), "max_normalized_error": max(v)}
            for k, v in by_category.items()
        },
        "electron_scalar_cases": results_e,
        "pair_cases": results_p,
        "failures": failures,
        "limitations": "Finite evidence for the tested points; no proof of all kinematics, loop corrections, continuum limits or source47 results.",
    }
    destination = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).with_name("results_s46_spin_sums.json")
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": output["status"], "output": str(destination), "comparisons": len(comparisons), "max_normalized_error": output["max_normalized_error"], "failures": len(failures)}))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
