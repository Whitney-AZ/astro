#!/usr/bin/env python3
"""Exercise66.4: source-only sharp thresholds, two independently summed routes."""

import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import sys


# mass text/unit and signed charge in the source tables' positive-proton units.
# Squaring the charge also applies when the QED convention has e < 0.
INPUTS = [
    ("e", "0.511", "MeV", 1, "-1", "S88 PDF360/348 table2"),
    ("mu", "105.7", "MeV", 1, "-1", "S88 PDF360/348 table2"),
    ("tau", "1777", "MeV", 1, "-1", "S88 PDF360/348 table2"),
    ("u", "300", "MeV", 3, "2/3", "S66 PDF275/263 exercise66.4 threshold"),
    ("d", "300", "MeV", 3, "-1/3", "S66 PDF275/263 exercise66.4 threshold"),
    ("s", "300", "MeV", 3, "-1/3", "S66 PDF275/263 exercise66.4 threshold"),
    ("c", "1.3", "GeV", 3, "2/3", "S83 PDF340/328 table1"),
    ("b", "4.3", "GeV", 3, "-1/3", "S83 PDF340/328 table1"),
    ("t", "178", "GeV", 3, "2/3", "S83 PDF340/328 table1"),
    ("nu_e", "0", "MeV", 1, "0", "S88 PDF360/348 table2; neutral"),
    ("nu_mu", "0", "MeV", 1, "0", "S88 PDF360/348 table2; neutral"),
    ("nu_tau", "0", "MeV", 1, "0", "S88 PDF360/348 table2; neutral"),
]
MW_GEV = 80.4  # S87 PDF357/345, actual value after source(87.12).
ALPHA_OS_INVERSE = 137.036  # S66 PDF275/263, source(66.32) input.


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("results_S66_thresholds.json"))
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit("Refusing to overwrite previous execution: " + str(args.output))
    factor = 2.0 / (3.0 * math.pi)
    species = []
    for name, mass_text, unit, color, charge_text, source in INPUTS:
        mass = float(mass_text) * (0.001 if unit == "MeV" else 1.0)
        weight = color * Fraction(charge_text) ** 2
        species.append({
            "name": name, "source_mass_text": mass_text, "source_mass_unit": unit,
            "mass_GeV": mass, "colors": color, "source_charge": charge_text,
            "N_c_Q_squared": str(weight), "source": source,
            "active_below_MW": bool(weight and mass < MW_GEV),
            "exclusion_reason": "neutral" if weight == 0 else (
                "mass above MW" if mass >= MW_GEV else None),
        })
    active = sorted([s for s in species if s["active_below_MW"]], key=lambda s: s["mass_GeV"])
    flavor_rows, terms = [], []
    for s in active:
        logarithm = math.log(MW_GEV / s["mass_GeV"])
        term = float(Fraction(s["N_c_Q_squared"])) * logarithm
        terms.append(term)
        cumulative = math.fsum(terms)
        flavor_rows.append({
            "name": s["name"], "mass_GeV": s["mass_GeV"],
            "N_c_Q_squared": s["N_c_Q_squared"], "log_MW_over_m": logarithm,
            "weighted_log": term, "inverse_alpha_drop": factor * term,
            "cumulative_weighted_log_by_flavor": cumulative,
            "inverse_at_MW_after_this_subset": ALPHA_OS_INVERSE - factor * cumulative,
        })
    direct_sum = math.fsum(terms)
    boundaries = sorted({s["mass_GeV"] for s in active} | {MW_GEV})
    intervals, interval_terms = [], []
    inverse = ALPHA_OS_INVERSE
    for low, high in zip(boundaries, boundaries[1:]):
        present = [s for s in active if s["mass_GeV"] <= low]
        weight = sum((Fraction(s["N_c_Q_squared"]) for s in present), Fraction())
        area = float(weight) * math.log(high / low)
        interval_terms.append(area)
        next_inverse = inverse - factor * area
        intervals.append({
            "lower_GeV": low, "upper_GeV": high,
            "active_flavors": [s["name"] for s in present],
            "active_weight": str(weight), "weighted_log_interval": area,
            "inverse_alpha_start": inverse, "inverse_alpha_end": next_inverse,
        })
        inverse = next_inverse
    piecewise_sum = math.fsum(interval_terms)
    low_scale_controls = []
    for divisor in (2.0, 4.0):
        low = active[0]["mass_GeV"] / divisor
        maximum_sum = math.fsum(float(Fraction(s["N_c_Q_squared"]))
                               * math.log(MW_GEV / max(s["mass_GeV"], low)) for s in active)
        minimum_sum = math.fsum(float(Fraction(s["N_c_Q_squared"]))
                               * math.log(MW_GEV / min(s["mass_GeV"], low)) for s in active)
        low_scale_controls.append({
            "mu_GeV": low, "inverse_from_correct_max": ALPHA_OS_INVERSE - factor * maximum_sum,
            "inverse_from_printed_min": ALPHA_OS_INVERSE - factor * minimum_sum,
        })
    direct_inverse = ALPHA_OS_INVERSE - factor * direct_sum
    checks = {
        "direct_vs_piecewise_log_sum_abs_error": abs(direct_sum - piecewise_sum),
        "direct_vs_cumulative_inverse_abs_error": abs(direct_inverse - inverse),
        "max_low_scale_dependence_abs_error": abs(
            low_scale_controls[0]["inverse_from_correct_max"]
            - low_scale_controls[1]["inverse_from_correct_max"]),
        "printed_min_spurious_low_scale_change": (
            low_scale_controls[1]["inverse_from_printed_min"]
            - low_scale_controls[0]["inverse_from_printed_min"]),
        "inverse_alpha_positive": bool(direct_inverse > 0),
    }
    passed = (checks["direct_vs_piecewise_log_sum_abs_error"] < 1e-12
              and checks["direct_vs_cumulative_inverse_abs_error"] < 1e-12
              and checks["max_low_scale_dependence_abs_error"] == 0.0
              and abs(checks["printed_min_spurious_low_scale_change"]) > 0.1
              and checks["inverse_alpha_positive"])
    result = {
        "status": "passed" if passed else "failed",
        "execution": {
            "attempt": 1, "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "python": sys.version, "executable": sys.executable, "platform": platform.platform(),
            "argv": sys.argv, "randomness": "none",
            "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "model": {
            "MW_GeV": MW_GEV, "MW_source": "S87 PDF357/345 after(87.12)",
            "alpha_OS_inverse": ALPHA_OS_INVERSE, "species_inputs": species,
            "approximation": "One-loop QED with constant source masses, sharp thresholds "
                             "and continuous leading-log matching; no higher-order or QCD data.",
            "factor_2_over_3pi": factor,
        },
        "per_flavor": flavor_rows, "piecewise_intervals": intervals,
        "low_scale_controls": low_scale_controls, "checks": checks,
        "summary": {
            "active_flavors": len(active), "color_expanded_charged_Dirac_fields": sum(s["colors"] for s in active),
            "sum_active_NcQ2": str(sum((Fraction(s["N_c_Q_squared"]) for s in active), Fraction())),
            "direct_weighted_log_sum": direct_sum, "piecewise_weighted_log_sum": piecewise_sum,
            "inverse_alpha_drop": factor * direct_sum,
            "alpha_MW_inverse": direct_inverse, "alpha_MW": 1.0 / direct_inverse,
        },
    }
    with args.output.open("x", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(json.dumps({"status": result["status"], "summary": result["summary"],
                      "checks": checks, "output": str(args.output)}, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
