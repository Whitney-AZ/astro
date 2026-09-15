#!/usr/bin/env python3
"""One new S49 check: three Majorana exchange channels with fixed Fock order.

The source gamma matrices and positive-mass spinor boost are inputs previously
derived in S38/S46, not re-tested here.  Each v basis is obtained from the same
u basis by charge conjugation.  The new calculations are the six interference
kernels, the full 16-component spin sum, and initial/final antisymmetry.
"""
import datetime
import hashlib
import itertools
import json
import math
import pathlib
import platform

import numpy as np


I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
E2 = np.array([[0, -1], [1, 0]], dtype=complex)
PAULI = [np.array(x, dtype=complex) for x in (
    [[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]
BETA = np.block([[Z2, I2], [I2, Z2]])
GAMMA = [BETA] + [np.block([[Z2, s], [-s, Z2]]) for s in PAULI]
C = np.block([[E2, Z2], [Z2, -E2]])
TOLERANCE = 2e-11
CASES = [
    {"name": "below_scalar_pole", "m": 0.8, "M": 3.7, "g": 0.71,
     "q": 0.5, "theta": 1.1, "phi": 0.4},
    {"name": "above_scalar_pole", "m": 1.2, "M": 2.5, "g": 0.9,
     "q": 1.3, "theta": 0.73, "phi": 1.2},
    {"name": "asymmetric_angle", "m": 0.47, "M": 2.1, "g": 0.36,
     "q": 0.83, "theta": 2.13, "phi": 0.91},
]
# theta, phi, and the two column phases of four complete spin bases.
BASES = [(0.43, 0.71, 0.21, -0.32), (1.13, -0.62, -0.57, 0.24),
         (0.91, 1.41, 0.38, 0.81), (1.67, 0.28, -0.71, 0.49)]


def dot(p, q):
    return -p[0] * q[0] + np.dot(p[1:], q[1:])


def slash(p):
    return -p[0] * GAMMA[0] + sum(
        (p[j] * GAMMA[j] for j in range(1, 4)), np.zeros((4, 4), complex))


def bar(w):
    return w.conj().T @ BETA


def charge(w):
    return C @ bar(w).T


def spinors(p, m, basis):
    theta, phi, alpha, beta = basis
    c, s, z = math.cos(theta / 2), math.sin(theta / 2), np.exp(1j * phi)
    rotation = np.array([[c, -z.conjugate() * s], [z * s, c]])
    rotation = rotation @ np.diag(np.exp(1j * np.array([alpha, beta])))
    spatial = sum((p[j] * GAMMA[j] for j in range(1, 4)),
                  np.zeros((4, 4), complex))
    boost = ((p[0] + m) * I4 + BETA @ spatial) / math.sqrt(2 * m * (p[0] + m))
    return boost @ (math.sqrt(m) * np.vstack([I2, I2])) @ rotation


def channels(w):
    u1, u2, u3, u4 = w
    v2, v4 = charge(u2), charge(u4)
    return {"t": (bar(u3) @ u1) * (bar(u4) @ u2),
            "u": (bar(u4) @ u1) * (bar(u3) @ u2),
            "s": (bar(v2) @ u1) * (bar(u3) @ v4)}


def mandelstam(p):
    p1, p2, p3, p4 = p
    return {"s": -dot(p1 + p2, p1 + p2),
            "t": -dot(p1 - p3, p1 - p3),
            "u": -dot(p1 - p4, p1 - p4)}


def amplitude(p, w, M, g):
    k, inv = channels(w), mandelstam(p)
    d = {a: M * M - inv[a] for a in "stu"}
    return g * g * (k["t"] / d["t"] - k["u"] / d["u"] + k["s"] / d["s"])


def scalar(z):
    z = complex(z)
    return {"real": z.real, "imag": z.imag}


def relerr(actual, expected):
    return float(abs(actual - expected) / max(1.0, abs(actual), abs(expected)))


def run_case(case):
    m, M, g, q = (case[k] for k in ("m", "M", "g", "q"))
    th, ph = case["theta"], case["phi"]
    energy = math.hypot(m, q)
    out = q * np.array([math.sin(th) * math.cos(ph),
                        math.sin(th) * math.sin(ph), math.cos(th)])
    p = [np.array([energy, 0, 0, q]), np.array([energy, 0, 0, -q]),
         np.r_[energy, out], np.r_[energy, -out]]
    U = [spinors(momentum, m, basis) for momentum, basis in zip(p, BASES)]
    inv = mandelstam(p)
    s, t, u = (inv[x] for x in "stu")
    ds, dt, du = (M * M - inv[x] for x in "stu")
    r = m * m
    P = [-slash(momentum) + m * I4 for momentum in p]
    Q = [-slash(momentum) - m * I4 for momentum in p]
    expected = {"tt": (t - 4 * r) ** 2, "uu": (u - 4 * r) ** 2,
                "ss": (s - 4 * r) ** 2, "tu": -t * u / 2 + 2 * r * s,
                "ts": s * t / 2 - 2 * r * u, "us": -u * s / 2 + 2 * r * t}
    traces = {
        "tt": np.trace(P[0] @ P[2]) * np.trace(P[1] @ P[3]) / 4,
        "uu": np.trace(P[0] @ P[3]) * np.trace(P[1] @ P[2]) / 4,
        "ss": np.trace(P[0] @ Q[1]) * np.trace(Q[3] @ P[2]) / 4,
        "tu": np.trace(P[0] @ P[3] @ P[1] @ P[2]) / 4,
        "ts": -np.trace(P[0] @ Q[1] @ Q[3] @ P[2]) / 4,
        "us": np.trace(P[0] @ Q[1] @ Q[2] @ P[3]) / 4,
    }
    kernels = dict.fromkeys(expected, 0j)
    spin_sum = wrong_s_sum = max_initial = max_final = max_polarized_imag = 0.0
    for spins in itertools.product(range(2), repeat=4):
        w = [U[j][:, spins[j]] for j in range(4)]
        k = channels(w)
        for pair in kernels:
            kernels[pair] += k[pair[0]] * k[pair[1]].conjugate() / 4
        a = amplitude(p, w, M, g)
        spin_sum += abs(a) ** 2 / 4
        wrong_s_sum += abs(g * g * (k["t"] / dt - k["u"] / du - k["s"] / ds)) ** 2 / 4
        max_polarized_imag = max(max_polarized_imag, abs((k["t"] * k["s"].conjugate()).imag))
        swapped_in = amplitude([p[1], p[0], p[2], p[3]],
                               [w[1], w[0], w[2], w[3]], M, g)
        swapped_out = amplitude([p[0], p[1], p[3], p[2]],
                                [w[0], w[1], w[3], w[2]], M, g)
        max_initial = max(max_initial, relerr(swapped_in, -a))
        max_final = max(max_final, relerr(swapped_out, -a))
    closed_form = g ** 4 * (
        (s - 4 * r) ** 2 / ds ** 2 + (s * t - 4 * r * u) / (ds * dt)
        + (t - 4 * r) ** 2 / dt ** 2 + (t * u - 4 * r * s) / (dt * du)
        + (u - 4 * r) ** 2 / du ** 2 + (u * s - 4 * r * t) / (du * ds))
    errors = [relerr(kernels[k], expected[k]) for k in expected]
    errors += [relerr(kernels[k], traces[k]) for k in expected]
    errors += [relerr(spin_sum, closed_form), max_initial, max_final]
    return {
        "input": case, "momenta": [x.tolist() for x in p], "mandelstam": inv,
        "denominators": {"s": ds, "t": dt, "u": du},
        "kernels": {key: {"direct_spin_sum": scalar(kernels[key]),
                          "ordered_trace": scalar(traces[key]), "invariant": expected[key]}
                    for key in expected},
        "spin_average": spin_sum, "source_49_8": closed_form,
        "wrong_s_sign_spin_average": wrong_s_sum,
        "wrong_s_sign_relative_difference": relerr(wrong_s_sum, closed_form),
        "maximum_polarized_ts_imaginary_part": max_polarized_imag,
        "maximum_initial_exchange_error": max_initial,
        "maximum_final_exchange_error": max_final,
        "maximum_scaled_error": max(errors),
    }


def main():
    results = [run_case(case) for case in CASES]
    max_error = max(case["maximum_scaled_error"] for case in results)
    report = {
        "execution_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "software": {"python": platform.python_version(), "numpy": np.__version__,
                     "platform": platform.platform()},
        "program_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "assumptions": {
            "metric": "(-,+,+,+)", "natural_units": True,
            "slash": "-p0 gamma0 + p_i gamma_i; Clifford anticommutator=-2g",
            "C": "diag(E,-E), E=[[0,-1],[1,0]], C^-1=-C",
            "paired_spinors": "v=C bar(u)^T for each full complex spin basis",
            "Fock_order": "ket=b1^dag b2^dag|0>, bra=<0|b4 b3",
            "amplitude": "g^2(Dt/(M^2-t)-Du/(M^2-u)+Ds/(M^2-s))",
            "spin_average": "1/4 on two independent initial spins; sum all final spins",
            "phase_space": "No identical-final-state factor belongs to this amplitude check",
            "domain": "m,M>0, real g, on-shell CM external momenta, real tree denominators away from scalar pole",
            "scope": "3 finite cases, not a proof; no old check script imported or executed",
        },
        "complete_spin_bases": BASES, "tolerance": TOLERANCE,
        "maximum_scaled_error": max_error, "passed": max_error <= TOLERANCE,
        "cases": results,
    }
    output = pathlib.Path("checks/srednicki/majorana49-check.json")
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(output), "passed": report["passed"],
                      "maximum_scaled_error": max_error,
                      "wrong_s_sign_differences": [x["wrong_s_sign_relative_difference"] for x in results],
                      "software": report["software"]}, ensure_ascii=False))
    if not report["passed"]:
        raise SystemExit("S49 new Majorana channel check failed; inspect recorded kernels.")


if __name__ == "__main__":
    main()
