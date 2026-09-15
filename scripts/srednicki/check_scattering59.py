#!/usr/bin/env python3
"""S59: new finite 4x4 checks, independent of earlier project programs.

Run from the project root: python3 scripts/srednicki/check_scattering59.py
Only checks/srednicki/scattering59-check.json is written. Every invocation is retained in that file.
The four source traces are multiplied explicitly. The separate polarization
route contracts A with two actual real transverse vectors for each photon.
No random sampling, massless approximation, phase-space factor, or old check.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
import platform
import sys
import traceback
from pathlib import Path

import numpy as np


OUTPUT = Path(__file__).resolve().parents[2] / "checks/srednicki/scattering59-check.json"
METRIC = np.array([-1.0, 1.0, 1.0, 1.0])
IDENTITY = np.eye(4, dtype=np.complex128)
ZERO = np.zeros((4, 4), dtype=np.complex128)
E_CHARGE = -0.3  # A chosen dimensionless test input, not a measured constant.
TOLERANCE = 2.0e-10
CASES = [
    {"id": "threshold", "m": 1.0, "E_over_m": 1.0,
     "theta": 0.8, "azimuth": 0.4},
    {"id": "near_threshold", "m": 0.7, "E_over_m": 1.0008,
     "theta": 1.1, "azimuth": 0.7},
    {"id": "general_angle", "m": 1.3, "E_over_m": 1.8,
     "theta": 1.2, "azimuth": -0.6},
    {"id": "high_energy_near_forward", "m": 0.9, "E_over_m": 20.0,
     "theta": 0.018, "azimuth": 0.5},
]


def weyl_gamma() -> tuple[np.ndarray, np.ndarray]:
    """gamma^mu=(0,sigma^mu;barsigma^mu,0), with Clifford=-2g."""
    i2 = np.eye(2, dtype=np.complex128)
    z2 = np.zeros((2, 2), dtype=np.complex128)
    pauli = [i2, np.array([[0, 1], [1, 0]], dtype=np.complex128),
             np.array([[0, -1j], [1j, 0]], dtype=np.complex128),
             np.array([[1, 0], [0, -1]], dtype=np.complex128)]
    upper = np.array([np.block([[z2, pauli[mu]],
                               [pauli[mu] if mu == 0 else -pauli[mu], z2]])
                      for mu in range(4)])
    lower = METRIC[:, None, None] * upper
    return upper, lower


GUP, GDOWN = weyl_gamma()


def dot(v: np.ndarray, w: np.ndarray) -> float:
    return float(np.sum(METRIC * v * w))


def slash(v: np.ndarray) -> np.ndarray:
    return -v[0] * GUP[0] + sum((v[i] * GUP[i] for i in range(1, 4)), ZERO.copy())


def adjoint(a: np.ndarray) -> np.ndarray:
    return GUP[0] @ a.conj().T @ GUP[0]


def frobenius(a: np.ndarray) -> float:
    return float(np.linalg.norm(a))


def comparison(actual: complex, expected: complex, scale_floor: float) -> dict:
    absolute = float(abs(actual - expected))
    scale = float(max(scale_floor, abs(actual), abs(expected)))
    return {"actual": complex(actual), "expected": complex(expected),
            "absolute_residual": absolute, "scale": scale,
            "scaled_residual": absolute / scale,
            "passed": bool(absolute <= TOLERANCE * scale)}


def source_four_traces(p: np.ndarray, q: np.ndarray,
                       na: np.ndarray, nb: np.ndarray) -> dict[str, complex]:
    """Source (59.19): each line is independently multiplied, including 1/4.

    Upper/lower gamma contractions are literal matrix sums. In particular
    tu and ut are both computed; neither is assigned the other's value.
    """
    answer = {key: 0j for key in ("tt", "tu", "ut", "uu")}
    for mu in range(4):
        for nu in range(4):
            answer["tt"] += np.trace(GUP[nu] @ na @ GUP[mu] @ p
                                     @ GDOWN[mu] @ na @ GDOWN[nu] @ q) / 4
            answer["tu"] += np.trace(GUP[nu] @ na @ GUP[mu] @ p
                                     @ GDOWN[nu] @ nb @ GDOWN[mu] @ q) / 4
            answer["ut"] += np.trace(GUP[mu] @ nb @ GUP[nu] @ p
                                     @ GDOWN[mu] @ na @ GDOWN[nu] @ q) / 4
            answer["uu"] += np.trace(GUP[mu] @ nb @ GUP[nu] @ p
                                     @ GDOWN[nu] @ nb @ GDOWN[mu] @ q) / 4
    return {key: complex(value) for key, value in answer.items()}


def source_polynomials(s: float, t: float, u: float, r: float) -> dict[str, float]:
    """Independent scalar arithmetic: source (59.22)--(59.25)."""
    return {"tt": 2 * (t * u - r * (3 * t + u) - r * r),
            "tu": 2 * r * (s - 4 * r),
            "ut": 2 * r * (s - 4 * r),
            "uu": 2 * (t * u - r * (3 * u + t) - r * r)}


def tensor_terms(na: np.ndarray, nb: np.ndarray,
                 denom_t: float, denom_u: float) -> tuple[np.ndarray, np.ndarray]:
    at = np.empty((4, 4, 4, 4), dtype=np.complex128)
    au = np.empty_like(at)
    for mu in range(4):
        for nu in range(4):
            at[mu, nu] = E_CHARGE ** 2 * GDOWN[nu] @ na @ GDOWN[mu] / denom_t
            au[mu, nu] = E_CHARGE ** 2 * GDOWN[mu] @ nb @ GDOWN[nu] / denom_u
    return at, au


def polarization_basis(momentum: np.ndarray, photon: int) -> np.ndarray:
    """Coulomb-gauge real linear polarizations; no metric polarization sum."""
    n = momentum[1:] / np.linalg.norm(momentum[1:])
    reference = np.array([0.0, 0.0, 1.0] if photon == 1 else [1.0, 0.0, 0.0])
    if abs(float(reference @ n)) > 0.85:
        reference = np.array([0.0, 1.0, 0.0])
    first = np.cross(reference, n)
    first /= np.linalg.norm(first)
    second = np.cross(n, first)
    angle = 0.23 if photon == 1 else -0.37
    rotated = [math.cos(angle) * first + math.sin(angle) * second,
               -math.sin(angle) * first + math.cos(angle) * second]
    return np.array([np.r_[0.0, vector] for vector in rotated])


def largest_entry(a: np.ndarray) -> dict:
    index = np.unravel_index(int(np.argmax(np.abs(a))), a.shape)
    return {"index": [int(i) for i in index], "value": complex(a[index])}


def ward_leg(at: np.ndarray, au: np.ndarray, momentum: np.ndarray,
             photon: int, p: np.ndarray, q: np.ndarray, m: float) -> dict:
    components = []
    for other in range(4):
        if photon == 1:
            wt = sum((momentum[mu] * at[mu, other] for mu in range(4)), ZERO.copy())
            wu = sum((momentum[mu] * au[mu, other] for mu in range(4)), ZERO.copy())
        else:
            wt = sum((momentum[nu] * at[other, nu] for nu in range(4)), ZERO.copy())
            wu = sum((momentum[nu] * au[other, nu] for nu in range(4)), ZERO.copy())
        pt, pu = q @ wt @ p, q @ wu @ p
        total = q @ (wt + wu) @ p  # Essential: external on-shell matrices.
        scale = max(E_CHARGE ** 2 * m ** 2, frobenius(pt) + frobenius(pu))
        components.append({
            "remaining_index": other,
            "projected_t_norm": frobenius(pt), "projected_u_norm": frobenius(pu),
            "projected_total_norm": frobenius(total),
            "projected_total_largest_entry": largest_entry(total),
            "unprojected_total_norm": frobenius(wt + wu),
            "unprojected_total_largest_entry": largest_entry(wt + wu),
            "scale": float(scale), "scaled_residual": frobenius(total) / scale,
            "passed": bool(frobenius(total) <= TOLERANCE * scale),
        })
    t_max = max(row["projected_t_norm"] for row in components)
    u_max = max(row["projected_u_norm"] for row in components)
    control_floor = 1.0e-8 * E_CHARGE ** 2 * m ** 2
    return {"photon": photon, "components": components,
            "single_graph_t_max_norm": t_max, "single_graph_u_max_norm": u_max,
            "single_graph_nonzero_floor": control_floor,
            "single_graph_control_passed": bool(t_max > control_floor and u_max > control_floor),
            "max_unprojected_total_norm": max(row["unprojected_total_norm"] for row in components),
            "max_scaled_residual": max(row["scaled_residual"] for row in components),
            "passed": bool(all(row["passed"] for row in components)
                           and t_max > control_floor and u_max > control_floor)}


def calculate_case(inputs: dict) -> dict:
    m, ratio = inputs["m"], inputs["E_over_m"]
    energy = m * ratio
    pz = m * math.sqrt((ratio - 1.0) * (ratio + 1.0))
    theta, azimuth = inputs["theta"], inputs["azimuth"]
    n = np.array([math.sin(theta) * math.cos(azimuth),
                  math.sin(theta) * math.sin(azimuth), math.cos(theta)])
    p1, p2 = np.array([energy, 0., 0., pz]), np.array([energy, 0., 0., -pz])
    k1, k2 = np.r_[energy, energy * n], np.r_[energy, -energy * n]
    a, b = p1 - k1, p1 - k2
    r, s, t, u = m * m, -dot(p1 + p2, p1 + p2), -dot(a, a), -dot(b, b)
    denom_t, denom_u = r - t, r - u
    p, q = -slash(p1) + m * IDENTITY, -slash(p2) - m * IDENTITY
    na, nb = -slash(a) + m * IDENTITY, -slash(b) + m * IDENTITY
    trace_values = source_four_traces(p, q, na, nb)
    polynomial_values = source_polynomials(s, t, u, r)
    traces = {key: comparison(trace_values[key], polynomial_values[key], r * r)
              for key in trace_values}

    def assemble(values: dict) -> complex:
        return E_CHARGE ** 4 * (values["tt"] / denom_t ** 2
                               + (values["tu"] + values["ut"]) / (denom_t * denom_u)
                               + values["uu"] / denom_u ** 2)

    assembled_trace, assembled_polynomial = assemble(trace_values), assemble(polynomial_values)
    at, au = tensor_terms(na, nb, denom_t, denom_u)
    amplitude = at + au
    polarizations = [polarization_basis(k1, 1), polarization_basis(k2, 2)]
    basis_checks = []
    for momentum, basis in zip([k1, k2], polarizations):
        gram_error = float(np.max(np.abs(basis[:, 1:] @ basis[:, 1:].T - np.eye(2))))
        transverse_error = float(max(abs(dot(momentum, eps)) for eps in basis)) / energy
        basis_checks.append({"gram_max_residual": gram_error,
                             "transverse_scaled_residual": transverse_error,
                             "passed": bool(max(gram_error, transverse_error) < TOLERANCE)})
    physical_pairs = []
    for first in range(2):
        for second in range(2):
            eps1, eps2 = polarizations[0][first], polarizations[1][second]
            chain = sum((eps1[mu] * eps2[nu] * amplitude[mu, nu]
                         for mu in range(4) for nu in range(4)), ZERO.copy())
            value = complex(np.trace(chain @ p @ adjoint(chain) @ q) / 4)
            scale = max(E_CHARGE ** 4, abs(value))
            physical_pairs.append({"polarization_indices": [first, second],
                                   "spin_average": value,
                                   "real_nonnegative_passed": bool(abs(value.imag) <= TOLERANCE * scale
                                                                  and value.real >= -TOLERANCE * scale)})
    physical_sum = sum(row["spin_average"] for row in physical_pairs)
    physical_checks = {
        "against_four_matrix_traces": comparison(physical_sum, assembled_trace, E_CHARGE ** 4),
        "against_four_source_polynomials": comparison(physical_sum, assembled_polynomial, E_CHARGE ** 4),
    }
    ward = [ward_leg(at, au, k1, 1, p, q, m), ward_leg(at, au, k2, 2, p, q, m)]
    swapped_t, swapped_u = tensor_terms(nb, na, denom_u, denom_t)
    bose_residual = frobenius(amplitude - (swapped_t + swapped_u).swapaxes(0, 1))
    bose_scale = max(abs(E_CHARGE ** 2 / m), frobenius(amplitude))
    bose = {"tensor_difference_norm": bose_residual, "scale": bose_scale,
            "scaled_residual": bose_residual / bose_scale,
            "passed": bool(bose_residual <= TOLERANCE * bose_scale)}
    shells = [dot(p1, p1) + r, dot(p2, p2) + r, dot(k1, k1), dot(k2, k2)]
    kinematics = {"p1": p1, "p2": p2, "k1": k1, "k2": k2,
                  "a": a, "b": b, "s": s, "t": t, "u": u,
                  "beta": pz / energy, "denom_t": denom_t, "denom_u": denom_u,
                  "s_over_4m2": s / (4 * r), "m2_over_s": r / s,
                  "shell_residuals": shells,
                  "momentum_conservation_residual": p1 + p2 - k1 - k2,
                  "s_plus_t_plus_u_minus_2m2": s + t + u - 2 * r,
                  "passed": bool(m > 0 and denom_t > 0 and denom_u > 0
                                 and max(abs(v) for v in shells) <= TOLERANCE * energy ** 2
                                 and abs(s + t + u - 2 * r) <= TOLERANCE * energy ** 2
                                 and np.linalg.norm(p1 + p2 - k1 - k2) <= TOLERANCE * energy)}
    threshold = None
    if ratio == 1.0:
        threshold = comparison(physical_sum, 4 * E_CHARGE ** 4, E_CHARGE ** 4)
    passed = (kinematics["passed"] and all(row["passed"] for row in traces.values())
              and all(row["passed"] for row in basis_checks)
              and all(row["real_nonnegative_passed"] for row in physical_pairs)
              and all(row["passed"] for row in physical_checks.values())
              and all(row["passed"] for row in ward) and bose["passed"]
              and (threshold is None or threshold["passed"]))
    return {"inputs": inputs, "kinematics": kinematics, "four_traces": traces,
            "assembled_from_traces": complex(assembled_trace),
            "assembled_from_polynomials": complex(assembled_polynomial),
            "physical_polarization_bases": polarizations, "basis_checks": basis_checks,
            "physical_pairs": physical_pairs, "physical_sum": complex(physical_sum),
            "physical_comparisons": physical_checks, "ward": ward, "bose": bose,
            "threshold_4e4": threshold, "passed": bool(passed)}


def json_ready(value):
    """Use ordinary Python bool/float/int, including NumPy scalar contents."""
    if isinstance(value, np.ndarray):
        return json_ready(value.tolist())
    if isinstance(value, np.generic):
        return json_ready(value.item())
    if isinstance(value, complex):
        return {"real": float(value.real), "imag": float(value.imag)}
    if isinstance(value, dict):
        return {str(key): json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_ready(item) for item in value]
    return value


def main() -> int:
    previous = json.loads(OUTPUT.read_text()) if OUTPUT.exists() else {"runs": []}
    script_text = Path(__file__).read_text()
    run = {
        "invocation": len(previous["runs"]) + 1,
        "started_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "command": "python3 scripts/srednicki/check_scattering59.py",
        "script_sha256": hashlib.sha256(script_text.encode()).hexdigest(),
        "software": {"python": sys.version, "numpy": np.__version__,
                     "platform": platform.platform(), "machine": platform.machine(),
                     "matrix_dtype": "complex128", "real_dtype": "float64",
                     "float64_epsilon": float(np.finfo(np.float64).eps)},
        "source": {"file": "量子场论（Srednicki中译本）.pdf",
                   "sha256": "91eead3d237b8e750dc8e0b3b778d39809a087a9336c4eac3b930a98d434425b",
                   "pdf_pages": [245, 246, 247], "printed_pages": [233, 234, 235],
                   "equations": ["59.4", "59.8", "59.15", "59.18", "59.19", "59.22-59.25"]},
        "conventions": {"metric": [-1, 1, 1, 1], "clifford": "-2g",
                        "slash": "-p0 gamma0 + pi gammai", "e": E_CHARGE,
                        "spin_average": 0.25, "photon_polarizations": "sum, not average",
                        "final_photon_phase_space_factor_included": False,
                        "ward_projection": "Q @ contraction(A) @ P",
                        "finite_i_epsilon": "not used; both internal denominators positive"},
        "tolerance": TOLERANCE, "random_seed": None,
        "sampling": "four fixed inputs; no random number generator",
        "scope_limits": ["finite on-shell 4D tree examples, not an all-kinematics proof",
                         "squared kernels cannot test the common Fock phase",
                         "no phase-space integration or cross-section threshold limit",
                         "mass retained in the high-energy near-forward example"],
        "cases": [], "passed": False,
    }
    try:
        for inputs in CASES:
            run["cases"].append(calculate_case(inputs))
        run["passed"] = bool(all(case["passed"] for case in run["cases"]))
    except Exception:
        run["exception"] = traceback.format_exc()
    if not run["passed"]:
        run["failed_script_source"] = script_text
    run["finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    previous["schema_version"] = 1
    previous["runs"].append(json_ready(run))
    previous["actual_invocation_count"] = len(previous["runs"])
    previous["latest_passed"] = bool(run["passed"])
    OUTPUT.write_text(json.dumps(previous, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"result": str(OUTPUT), "actual_invocation_count": len(previous["runs"]),
                      "passed": bool(run["passed"]),
                      "case_status": {case["inputs"]["id"]: case["passed"] for case in run["cases"]}},
                     ensure_ascii=False))
    return 0 if run["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
