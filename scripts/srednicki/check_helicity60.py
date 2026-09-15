#!/usr/bin/env python3
"""One new S60 check: signed-energy endpoints and two-fermion/two-photon trees.

Only results_S60.json is written. Old check modules are neither imported nor
executed. The S50 positive-energy endpoint definitions are implemented locally;
new tests concern negative energies, all 16 assigned helicities, references,
and direct positive-energy physical amplitudes. No Fierz or massive trace test.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import itertools
import json
import math
import platform
import sys
import traceback
from pathlib import Path

import numpy as np


OUTPUT = Path(__file__).resolve().parents[2] / "checks/srednicki/helicity60-check.json"
CHARGE = -0.3
TOL = 2.0e-11
METRIC = np.array([-1., 1., 1., 1.])
I2 = np.eye(2, dtype=np.complex128)
Z2 = np.zeros((2, 2), dtype=np.complex128)
U = np.array([[0., 1.], [-1., 0.]], dtype=np.complex128)
PAULI = [np.array([[0, 1], [1, 0]], dtype=np.complex128),
         np.array([[0, -1j], [1j, 0]], dtype=np.complex128),
         np.array([[1, 0], [0, -1]], dtype=np.complex128)]
GAMMA = [np.block([[Z2, I2], [I2, Z2]])]
GAMMA += [np.block([[Z2, sigma], [-sigma, Z2]]) for sigma in PAULI]
ZERO4 = np.zeros((4, 4), dtype=np.complex128)
REPRESENTATIVES = ["+-+-", "+--+"]
CASES = [
    {"id": "annihilation", "energy": 2.3,
     "incoming_direction": {"theta": 0.7, "azimuth": 0.4},
     "outgoing_direction": {"theta": 1.4, "azimuth": -0.8},
     "negative_energy_legs": [1, 2]},
    {"id": "compton", "energy": 1.7,
     "incoming_direction": {"theta": 0.9, "azimuth": -0.6},
     "outgoing_direction": {"theta": 2.0, "azimuth": 0.8},
     "negative_energy_legs": [1, 3]},
]
REFERENCE_INPUTS = {
    "A": {"energy": 1.1, "theta": 1.05, "azimuth": 2.0},
    "B": {"energy": 0.8, "theta": 2.2, "azimuth": -1.7},
    "C": {"energy": 0.9, "theta": 0.45, "azimuth": 1.3},
    "D": {"energy": 1.4, "theta": 1.9, "azimuth": 0.2},
}


def direction(theta: float, azimuth: float) -> np.ndarray:
    return np.array([math.sin(theta) * math.cos(azimuth),
                     math.sin(theta) * math.sin(azimuth), math.cos(theta)])


def null_vector(energy: float, theta: float, azimuth: float) -> np.ndarray:
    return np.r_[energy, energy * direction(theta, azimuth)]


def dot(p: np.ndarray, q: np.ndarray) -> complex:
    return complex(np.sum(METRIC * p * q))


def slash(p: np.ndarray) -> np.ndarray:
    return sum((METRIC[mu] * p[mu] * GAMMA[mu] for mu in range(4)), ZERO4.copy())


def phi(positive_p: np.ndarray) -> np.ndarray:
    """Exactly the S50 source phase, without importing its executable module."""
    energy = float(positive_p[0])
    if energy <= 0:
        raise ValueError("phi requires positive energy")
    theta = math.acos(float(np.clip(positive_p[3] / energy, -1., 1.)))
    azimuth = math.atan2(float(positive_p[2]), float(positive_p[1]))
    return math.sqrt(2 * energy) * np.array(
        [-math.sin(theta / 2) * np.exp(-1j * azimuth), math.cos(theta / 2)],
        dtype=np.complex128)


def physical_u(positive_p: np.ndarray, helicity: str) -> np.ndarray:
    z = phi(positive_p)
    if helicity == "-":
        return np.r_[z, np.zeros(2, dtype=np.complex128)]
    return np.r_[np.zeros(2, dtype=np.complex128), U @ z.conjugate()]


def physical_bar(column: np.ndarray) -> np.ndarray:
    return column.conjugate() @ GAMMA[0]


def flip(helicity: str) -> str:
    return "".join("-" if h == "+" else "+" for h in helicity)


def endpoints(p: np.ndarray) -> dict:
    """All four analytic endpoints multiply the SAME c=1 or i, including rows."""
    energy_sign = 1 if p[0] > 0 else -1
    c = 1.0 + 0j if energy_sign == 1 else 1j
    positive_p = energy_sign * p
    square_ket = physical_u(positive_p, "-")
    angle_ket = physical_u(positive_p, "+")
    return {"energy_sign": energy_sign, "c": c,
            "square_ket": c * square_ket, "angle_ket": c * angle_ket,
            "square_bra": c * physical_bar(angle_ket),
            "angle_bra": c * physical_bar(square_ket)}


def angle(a: dict, b: dict) -> complex:
    return complex(a["angle_bra"] @ b["angle_ket"])


def square(a: dict, b: dict) -> complex:
    return complex(a["square_bra"] @ b["square_ket"])


def polarization(k: np.ndarray, helicity: str, reference: np.ndarray) -> np.ndarray:
    ek, eq = endpoints(k), endpoints(reference)
    if helicity == "+":
        row, column, denominator = eq["angle_bra"], ek["square_ket"], angle(eq, ek)
    else:
        row, column, denominator = eq["square_bra"], ek["angle_ket"], square(eq, ek)
    if abs(denominator) < 1.e-12:
        raise ValueError("invalid polarization reference")
    return -np.array([row @ gamma @ column for gamma in GAMMA]) / (math.sqrt(2) * denominator)


def compare(actual, expected, floor: float) -> dict:
    a, b = np.asarray(actual, dtype=np.complex128), np.asarray(expected, dtype=np.complex128)
    if a.shape != b.shape:
        raise ValueError((a.shape, b.shape))
    error = float(np.max(np.abs(a - b)))
    scale = max(float(floor), float(np.max(np.abs(a))), float(np.max(np.abs(b))))
    record = {"shape": list(a.shape), "absolute_residual": error,
              "scale": scale, "scaled_residual": error / scale,
              "passed": bool(error <= TOL * scale)}
    if a.ndim == 0:
        record.update(actual=complex(a), expected=complex(b))
    else:
        index = np.unravel_index(int(np.argmax(np.abs(a - b))), a.shape)
        record.update(largest_error_index=[int(i) for i in index],
                      actual_at_index=complex(a[index]), expected_at_index=complex(b[index]))
    return record


def assigned_diagrams(momenta: list[np.ndarray], ep: list[dict], helicities: str,
                      reference3: np.ndarray, reference4: np.ndarray) -> dict:
    """Literal 4x4 chains of source (60.28), both diagrams kept for all helicities."""
    p1, p2, k3, k4 = momenta
    col1 = ep[0]["square_ket" if helicities[0] == "+" else "angle_ket"]
    row2 = ep[1]["square_bra" if helicities[1] == "+" else "angle_bra"]
    eps3 = polarization(k3, helicities[2], reference3)
    eps4 = polarization(k4, helicities[3], reference4)
    s13 = -dot(p1 + k3, p1 + k3).real
    s14 = -dot(p1 + k4, p1 + k4).real
    t13 = -CHARGE ** 2 / s13 * (row2 @ slash(eps4) @ slash(p1 + k3) @ slash(eps3) @ col1)
    t14 = -CHARGE ** 2 / s14 * (row2 @ slash(eps3) @ slash(p1 + k4) @ slash(eps4) @ col1)
    return {"graph13": complex(t13), "graph14": complex(t14), "total": complex(t13 + t14)}


def bracket_predictions(ep: list[dict]) -> dict[str, complex]:
    """R60.22 and the signed-energy all-helicity-flip relation; other labels zero."""
    a13, a23 = angle(ep[0], ep[2]), angle(ep[1], ep[2])
    a14, a24 = angle(ep[0], ep[3]), angle(ep[1], ep[3])
    values = {"+-+-": 2 * CHARGE ** 2 * a24 ** 2 / (a13 * a23),
              "+--+": 2 * CHARGE ** 2 * a23 ** 2 / (a14 * a24)}
    energy_factor = ep[0]["energy_sign"] * ep[1]["energy_sign"]
    for key in list(values):
        values[flip(key)] = energy_factor * values[key].conjugate()
    return values


def physical_diagrams(case_id: str, positive: list[np.ndarray], helicities: str,
                      reference3: np.ndarray, reference4: np.ndarray) -> dict:
    """Direct positive-energy u/v endpoints and physical incoming conjugation.

    No assigned amplitude or proposed common phase is used in this function.
    The propagator numerator is -slash(actual internal arrow momentum).
    """
    p, q_or_pprime, k_or_kprime1, kprime2 = positive
    h1 = flip(helicities[0])  # Incoming electron.
    col = physical_u(p, h1)
    if case_id == "annihilation":
        h2 = flip(helicities[1])  # Incoming positron; v_h = u_{-h} in S50.
        row = physical_bar(physical_u(q_or_pprime, flip(h2)))
        h3, h4 = helicities[2], helicities[3]
        eps3 = polarization(k_or_kprime1, h3, reference3)
        eps4 = polarization(kprime2, h4, reference4)
        internal13, internal14 = p - k_or_kprime1, p - kprime2
    else:
        h2 = helicities[1]  # Outgoing electron.
        row = physical_bar(physical_u(q_or_pprime, h2))
        h3, h4 = flip(helicities[2]), helicities[3]
        eps3 = polarization(k_or_kprime1, h3, reference3).conjugate()
        eps4 = polarization(kprime2, h4, reference4)
        internal13, internal14 = p + k_or_kprime1, p - kprime2
    t13 = CHARGE ** 2 * (row @ slash(eps4) @ (-slash(internal13)) @ slash(eps3) @ col) / dot(internal13, internal13)
    t14 = CHARGE ** 2 * (row @ slash(eps3) @ (-slash(internal14)) @ slash(eps4) @ col) / dot(internal14, internal14)
    return {"physical_helicities_in_leg_order": h1 + h2 + h3 + h4,
            "graph13": complex(t13), "graph14": complex(t14), "total": complex(t13 + t14)}


def calculate_case(inputs: dict, references: dict[str, np.ndarray]) -> dict:
    energy = inputs["energy"]
    n = direction(**inputs["incoming_direction"])
    out = direction(**inputs["outgoing_direction"])
    initial_e, initial_other = np.r_[energy, energy * n], np.r_[energy, -energy * n]
    final_first, final_second = np.r_[energy, energy * out], np.r_[energy, -energy * out]
    if inputs["id"] == "annihilation":
        positive = [initial_e, initial_other, final_first, final_second]
    else:
        positive = [initial_e, final_first, initial_other, final_second]
    signs = [-1 if i + 1 in inputs["negative_energy_legs"] else 1 for i in range(4)]
    momenta = [sign * p for sign, p in zip(signs, positive)]
    ep = [endpoints(p) for p in momenta]
    sij = {f"{i+1}{j+1}": -dot(momenta[i] + momenta[j], momenta[i] + momenta[j]).real
           for i, j in itertools.combinations(range(4), 2)}
    checks = []
    momentum_check = compare(sum(momenta), np.zeros(4), energy)
    shell_checks = [compare(dot(p, p), 0., energy ** 2) for p in momenta]
    checks += [momentum_check, *shell_checks]

    negative_endpoints = []
    for leg in inputs["negative_energy_legs"]:
        p, endpoint = momenta[leg - 1], ep[leg - 1]
        outer = np.outer(endpoint["square_ket"], endpoint["angle_bra"])
        outer += np.outer(endpoint["angle_ket"], endpoint["square_bra"])
        complete = compare(outer, -slash(p), energy)
        adj_angle = compare(endpoint["angle_bra"], -physical_bar(endpoint["square_ket"]), math.sqrt(energy))
        adj_square = compare(endpoint["square_bra"], -physical_bar(endpoint["angle_ket"]), math.sqrt(energy))
        wrong_gap = float(np.linalg.norm(endpoint["angle_bra"] - physical_bar(endpoint["square_ket"])))
        control = bool(wrong_gap > 1.e-8 * math.sqrt(energy))
        negative_endpoints.append({"leg": leg, "analytic_endpoints": endpoint,
                                   "minus_slash_outer_sum": complete,
                                   "signed_angle_adjoint": adj_angle, "signed_square_adjoint": adj_square,
                                   "ordinary_adjoint_wrong_gap_norm": wrong_gap,
                                   "ordinary_adjoint_control_passed": control})
        checks += [complete, adj_angle, adj_square, {"passed": control}]

    signed_brackets = []
    for i, j in itertools.combinations(range(4), 2):
        if signs[i] == 1 and signs[j] == 1:
            continue  # This task does not repeat the S50 all-positive checks.
        aij, sji = angle(ep[i], ep[j]), square(ep[j], ep[i])
        conj_check = compare(aij.conjugate(), signs[i] * signs[j] * sji, energy)
        invariant_check = compare(aij * sji, sij[f"{i+1}{j+1}"], energy ** 2)
        modulus_check = compare(abs(aij) ** 2, abs(sij[f"{i+1}{j+1}"]), energy ** 2)
        signed_brackets.append({"legs": [i + 1, j + 1], "angle_ij": aij,
                                "square_ji": sji, "conjugation": conj_check,
                                "invariant": invariant_check, "absolute_modulus": modulus_check})
        checks += [conj_check, invariant_check, modulus_check]

    expected = bracket_predictions(ep)
    amplitudes = {}
    for helicities in map("".join, itertools.product("+-", repeat=4)):
        diagrams = assigned_diagrams(momenta, ep, helicities, references["A"], references["B"])
        prediction = expected.get(helicities, 0j)
        check = compare(diagrams["total"], prediction, CHARGE ** 2)
        amplitudes[helicities] = {**diagrams, "prediction_kind": "R60.22 or all-flip" if helicities in expected else "zero selection rule",
                                  "comparison": check}
        checks.append(check)

    reference_changes = []
    base = amplitudes["+-+-"]
    for changed_leg in [3, 4]:
        for alternative in ["C", "D"]:
            names = {3: "A", 4: "B"}
            names[changed_leg] = alternative
            value = assigned_diagrams(momenta, ep, "+-+-", references[names[3]], references[names[4]])
            check = compare(value["total"], base["total"], CHARGE ** 2)
            difference13, difference14 = value["graph13"] - base["graph13"], value["graph14"] - base["graph14"]
            control = bool(abs(difference13) > 1.e-8 * CHARGE ** 2 and abs(difference14) > 1.e-8 * CHARGE ** 2)
            reference_changes.append({"changed_photon": changed_leg, "reference3": names[3], "reference4": names[4],
                                      **value, "total_comparison": check,
                                      "graph13_change": difference13, "graph14_change": difference14,
                                      "single_graph_change_control_passed": control})
            checks += [check, {"passed": control}]

    physical = []
    phase = -1.0 + 0j if inputs["id"] == "annihilation" else 1j
    for helicities in REPRESENTATIVES:
        actual = physical_diagrams(inputs["id"], positive, helicities, references["A"], references["B"])
        assigned = amplitudes[helicities]["total"]
        check = compare(actual["total"], phase * assigned, CHARGE ** 2)
        physical.append({"assigned_helicities": helicities, **actual,
                         "physical_over_assigned": actual["total"] / assigned,
                         "predicted_common_phase": phase, "comparison": check})
        checks.append(check)

    average = sum(abs(value["total"]) ** 2 for value in amplitudes.values()) / 4
    absolute_formula = 2 * CHARGE ** 4 * (abs(sij["13"] / sij["14"]) + abs(sij["14"] / sij["13"]))
    unsigned_source = 2 * CHARGE ** 4 * (sij["13"] / sij["14"] + sij["14"] / sij["13"])
    average_check = compare(average, absolute_formula, CHARGE ** 4)
    signed_source_control = bool(unsigned_source < 0 < average) if inputs["id"] == "compton" else bool(unsigned_source > 0)
    checks += [average_check, {"passed": signed_source_control}]
    reference_denominators = {}
    for name, reference in references.items():
        er = endpoints(reference)
        reference_denominators[name] = {str(leg): {"angle": angle(er, ep[leg - 1]),
                                                   "square": square(er, ep[leg - 1])}
                                        for leg in [3, 4]}
    return {"inputs": inputs, "positive_physical_momenta": positive,
            "assigned_momenta": momenta, "energy_signs": signs,
            "cosine_between_incoming_electron_and_outgoing_first": float(n @ out),
            "invariants": sij, "momentum_conservation": momentum_check, "shell_checks": shell_checks,
            "negative_endpoint_checks": negative_endpoints, "signed_bracket_checks": signed_brackets,
            "reference_bracket_denominators": reference_denominators,
            "assigned_amplitudes": amplitudes, "reference_changes": reference_changes,
            "direct_physical_amplitudes": physical, "spin_average": float(average),
            "absolute_formula_R60_24": float(absolute_formula), "source_60_33_without_absolute_values": float(unsigned_source),
            "spin_average_comparison": average_check, "source_sign_control_passed": signed_source_control,
            "passed": bool(all(check["passed"] for check in checks))}


def json_ready(value):
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
    source_text = Path(__file__).read_text()
    references = {key: null_vector(**value) for key, value in REFERENCE_INPUTS.items()}
    run = {"invocation": len(previous["runs"]) + 1,
           "started_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
           "command": "python3 scripts/srednicki/check_helicity60.py",
           "script_sha256": hashlib.sha256(source_text.encode()).hexdigest(),
           "software": {"python": sys.version, "numpy": np.__version__, "platform": platform.platform(),
                        "matrix_dtype": "complex128", "float64_epsilon": float(np.finfo(np.float64).eps)},
           "source": {"file": "量子场论（Srednicki中译本）.pdf",
                      "sha256": "91eead3d237b8e750dc8e0b3b778d39809a087a9336c4eac3b930a98d434425b",
                      "formula_pages": [248, 249, 251, 252], "source_equations": ["60.1", "60.7", "60.8", "60.17", "60.28", "60.31-60.33"],
                      "analytic_reference": "checks/review_S60_source.md R60.11-13,R60.18-25",
                      "positive_endpoint_implementation_read_only": "checks/check_s50_spinor_helicity.py phi/spinors/bar; not imported or run"},
           "conventions": {"metric": [-1, 1, 1, 1], "clifford": "-2g", "charge": CHARGE,
                           "all_outgoing": True, "negative_endpoint_phase_rows_and_columns": "i",
                           "assigned_positive_fermion": "square endpoint", "photon_incoming": "complex-conjugate physical polarization",
                           "initial_average": 0.25, "final_state_factorial_included": False},
           "random_seed": None, "sampling": "two fixed real massless CM configurations",
           "reference_inputs": REFERENCE_INPUTS, "reference_momenta": references,
           "baseline_references": {"photon3": "A", "photon4": "B"}, "tolerance": TOL,
           "scope": "Finite massless hard-angle tree checks; not a proof for general momenta or arbitrary Fock reordering.",
           "cases": [], "passed": False}
    try:
        for inputs in CASES:
            run["cases"].append(calculate_case(inputs, references))
        run["passed"] = bool(all(case["passed"] for case in run["cases"]))
    except Exception:
        run["exception"] = traceback.format_exc()
    if not run["passed"]:
        run["failed_script_source"] = source_text
    run["finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    previous["schema_version"] = 1
    previous["runs"].append(json_ready(run))
    previous["actual_invocation_count"] = len(previous["runs"])
    previous["latest_passed"] = bool(run["passed"])
    OUTPUT.write_text(json.dumps(previous, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"result": str(OUTPUT), "actual_invocation_count": len(previous["runs"]),
                      "passed": bool(run["passed"]),
                      "case_status": {case["inputs"]["id"]: case["passed"] for case in run["cases"]}}, ensure_ascii=False))
    return 0 if run["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
