#!/usr/bin/env python3
"""Exact, labelled bosonic Wick enumeration for a bounded set of S65 graphs.

Only Python's standard library is used.  Every field slot at every insertion
is distinct; external labels are fixed.  The generator knows the two allowed
contractions and forbids external--external contractions.  Graph filters
know topology, not a diagram symmetry factor.  Vertex normalizations are
obtained from separate, explicitly enumerated one-vertex tree cases.

The output is exclusive-created to preserve this run's evidence.  To
reproduce later, pass a different --output path.  This script neither reads
nor changes central coverage, manuscript, source inventory, or old checks.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from math import factorial
from pathlib import Path
import platform
import sys
import traceback


@dataclass(frozen=True)
class Field:
    name: str
    species: str
    vertex: int | None
    external_label: str | None = None
    physical_role: str | None = None


SLOTS = {
    "seagull": ("phidag", "phi", "A", "A"),
    "quartic": ("phidag", "phidag", "phi", "phi"),
}
LOCAL_NORMALIZATION = {"seagull": Fraction(1), "quartic": Fraction(1, 4)}
SCALAR_EXTERNALS = (
    ("1", "phidag", "incoming charged scalar"),
    ("2", "phidag", "incoming charged scalar"),
    ("3", "phi", "outgoing charged scalar"),
    ("4", "phi", "outgoing charged scalar"),
)
MIXED_EXTERNALS = (
    ("1", "phidag", "incoming charged scalar"),
    ("3", "phi", "outgoing charged scalar"),
    ("mu", "A", "fixed photon index mu"),
    ("nu", "A", "fixed photon index nu"),
)
TWO_SCALAR_EXTERNALS = (SCALAR_EXTERNALS[0], SCALAR_EXTERNALS[2])


def fraction_record(value: Fraction) -> dict:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "exact": str(value),
    }


def fields_for(kind, vertex_count, external_data):
    fields = [
        Field("ext." + label, species, None, label, role)
        for label, species, role in external_data
    ]
    for vertex in range(vertex_count):
        occurrences = Counter()
        for species in SLOTS[kind]:
            name = f"v{vertex}.{species}{occurrences[species]}"
            occurrences[species] += 1
            fields.append(Field(name, species, vertex))
    return tuple(fields)


def compatible(a: Field, b: Field) -> bool:
    if a.vertex is None and b.vertex is None:
        return False
    return ((a.species == "A" and b.species == "A")
            or {a.species, b.species} == {"phi", "phidag"})


def matchings(fields):
    """Pick the first unpaired slot; every unordered perfect matching once."""
    if not fields:
        yield ()
        return
    first = fields[0]
    for index in range(1, len(fields)):
        partner = fields[index]
        if compatible(first, partner):
            rest = fields[1:index] + fields[index + 1:]
            for suffix in matchings(rest):
                yield ((first, partner),) + suffix


def matching_string(pairs) -> str:
    """Lossless compact archive; '--' joins slots and '; ' joins pairs."""
    edges = sorted(tuple(sorted((a.name, b.name))) for a, b in pairs)
    return "; ".join(a + "--" + b for a, b in edges)


def classify_pairs(pairs, vertex_count):
    attachments = [[] for _ in range(vertex_count)]
    endpoint_slots = {}
    internal = []
    for a, b in pairs:
        if a.vertex is None:
            attachments[b.vertex].append(a.external_label)
            endpoint_slots[a.external_label] = b.name
        elif b.vertex is None:
            attachments[a.vertex].append(b.external_label)
            endpoint_slots[b.external_label] = a.name
        else:
            internal.append((a, b))
    return tuple(tuple(sorted(group)) for group in attachments), endpoint_slots, internal


def connected(vertex_count, internal, removed=None) -> bool:
    reached = {0}
    while True:
        before = len(reached)
        for index, (a, b) in enumerate(internal):
            if index == removed:
                continue
            if a.vertex in reached or b.vertex in reached:
                reached.add(a.vertex)
                reached.add(b.vertex)
        if len(reached) == before:
            return len(reached) == vertex_count


def filter_reason(topology, vertex_count, external_count, groups, internal):
    expected_internal = {"tree": 0, "tadpole": 1, "bubble": 2}[topology]
    if any(len(group) != external_count // vertex_count for group in groups):
        return "external_degree_not_selected_topology"
    if len(internal) != expected_internal:
        return "wrong_internal_edge_count"
    if topology == "bubble" and any(a.vertex == b.vertex for a, b in internal):
        return "internal_self_contraction_instead_of_two_crossing_lines"
    if not connected(vertex_count, internal):
        return "disconnected_vertex_graph"
    if any(not connected(vertex_count, internal, removed=i)
           for i in range(len(internal))):
        return "one_particle_reducible"
    return None


def case(name, kind, vertex_count, external_data, topology, source):
    fields = fields_for(kind, vertex_count, external_data)
    all_seen = set()
    accepted = []
    rejections = Counter()
    allocation_counts = Counter()
    by_allocation = defaultdict(list)
    endpoint_counts = Counter()
    internal_types = Counter()
    directed_edges = Counter()
    loop_numbers = Counter()
    for pairing in matchings(fields):
        text = matching_string(pairing)
        if text in all_seen:
            raise AssertionError("Generator repeated an unordered pairing: " + text)
        all_seen.add(text)
        groups, endpoint_slots, internal = classify_pairs(pairing, vertex_count)
        reason = filter_reason(topology, vertex_count, len(external_data), groups, internal)
        if reason:
            rejections[reason] += 1
            continue
        accepted.append(text)
        allocation_counts[groups] += 1
        by_allocation[groups].append(text)
        endpoint_counts[tuple(sorted(endpoint_slots.items()))] += 1
        types = tuple(sorted("photon" if a.species == "A" else "complex_scalar"
                             for a, b in internal))
        internal_types[types] += 1
        # The scalar propagator arrow is phidag -> phi; photon edges are undirected.
        arrows = []
        for a, b in internal:
            if a.species == "A":
                arrows.append("A:" + str(min(a.vertex, b.vertex))
                              + "--" + str(max(a.vertex, b.vertex)))
            else:
                start, end = (a, b) if a.species == "phidag" else (b, a)
                arrows.append(f"scalar:{start.vertex}->{end.vertex}")
        directed_edges[tuple(sorted(arrows))] += 1
        loop_numbers[len(internal) - vertex_count + 1] += 1

    expansion_denominator = factorial(vertex_count)
    prefactor = LOCAL_NORMALIZATION[kind] ** vertex_count / expansion_denominator
    result = {
        "case_id": name,
        "source": source,
        "input": {
            "vertex_kind": kind,
            "labelled_vertex_count": vertex_count,
            "fields": [asdict(field) for field in fields],
            "selected_topology": topology,
            "identical_insertion_expansion_denominator": expansion_denominator,
            "local_monomial_coefficient_each": fraction_record(LOCAL_NORMALIZATION[kind]),
            "combined_prefactor_before_pairing_count": fraction_record(prefactor),
        },
        "generated_compatible_pairings_without_external_external": len(all_seen),
        "accepted_pairing_count": len(accepted),
        "rejections": dict(sorted(rejections.items())),
        "accepted_internal_species": [
            {"species": list(key), "pairing_count": count}
            for key, count in sorted(internal_types.items())
        ],
        "accepted_internal_arrows": [
            {"arrows": list(key), "pairing_count": count}
            for key, count in sorted(directed_edges.items())
        ],
        "loop_number_counts": {str(k): v for k, v in sorted(loop_numbers.items())},
        "total_normalized_weight": fraction_record(prefactor * len(accepted)),
    }
    if vertex_count == 2:
        labels = tuple(sorted(label for label, _, _ in external_data))
        ordered = []
        unordered_counts = Counter()
        unordered_keys = set()
        for left in combinations(labels, 2):
            right = tuple(label for label in labels if label not in left)
            groups = (left, right)
            key = tuple(sorted(groups))
            count = allocation_counts[groups]
            unordered_keys.add(key)
            unordered_counts[key] += count
            ordered.append({
                "v0_external_labels": list(left),
                "v1_external_labels": list(right),
                "pairing_count": count,
                "normalized_weight": fraction_record(prefactor * count),
                "raw_pairings": sorted(by_allocation[groups]),
            })
        result["ordered_external_allocations"] = ordered
        result["vertex_exchange_classes"] = [
            {
                "external_partition": [list(block) for block in key],
                "pairing_count_including_both_vertex_labellings": unordered_counts[key],
                "normalized_weight": fraction_record(prefactor * unordered_counts[key]),
            }
            for key in sorted(unordered_keys)
        ]
    else:
        result["endpoint_choices"] = [
            {"external_to_vertex_slot": dict(key), "pairing_count": count}
            for key, count in sorted(endpoint_counts.items())
        ]
        result["raw_pairings"] = sorted(accepted)
    return result


CASE_INPUTS = (
    ("tree_seagull", "seagull", 1, MIXED_EXTERNALS, "tree",
     "Auxiliary differentiation normalization of -e^2 phidag phi A^2"),
    ("tree_quartic", "quartic", 1, SCALAR_EXTERNALS, "tree",
     "Auxiliary differentiation normalization of -lambda phidag^2 phi^2/4"),
    ("self_energy_photon_tadpole", "seagull", 1, TWO_SCALAR_EXTERNALS, "tadpole",
     "PDF268-269, (65.19)-(65.20), Fig.65.2 upper-right; S65-D005"),
    ("self_energy_scalar_tadpole", "quartic", 1, TWO_SCALAR_EXTERNALS, "tadpole",
     "PDF268-269, (65.19)-(65.20), Fig.65.2 lower-left; S65-D006"),
    ("four_scalar_photon_bubbles", "seagull", 2, SCALAR_EXTERNALS, "bubble",
     "PDF271, (65.34), Fig.65.5 first/second; S65-D015/S65-D016"),
    ("four_scalar_scalar_bubbles", "quartic", 2, SCALAR_EXTERNALS, "bubble",
     "PDF271, (65.34), Fig.65.5 third/fourth/fifth; S65-D017/S65-D018/S65-D019"),
    ("mixed_four_two_seagull_bubbles", "seagull", 2, MIXED_EXTERNALS, "bubble",
     "Optional bounded extension: PDF271, (65.31), Fig.65.4 first class; S65-D012"),
)


def check_record(name, actual, expected):
    return {"check": name, "actual": actual, "expected": expected, "passed": actual == expected}


def run(payload):
    cases = [case(*input_row) for input_row in CASE_INPUTS]
    payload["cases"] = cases
    by_name = {item["case_id"]: item for item in cases}
    tree_weights = {
        kind: Fraction(by_name["tree_" + kind]["total_normalized_weight"]["exact"])
        for kind in ("seagull", "quartic")
    }
    for item in cases:
        kind = item["input"]["vertex_kind"]
        power = item["input"]["labelled_vertex_count"]
        reference = tree_weights[kind] ** power
        item["enumerated_differentiated_vertex_product"] = fraction_record(reference)
        item["weight_relative_to_that_vertex_product"] = fraction_record(
            Fraction(item["total_normalized_weight"]["exact"]) / reference)
        for group in item.get("vertex_exchange_classes", []):
            group["relative_weight_from_count_not_assigned_symmetry_factor"] = fraction_record(
                Fraction(group["normalized_weight"]["exact"]) / reference)
    # These manually derived numbers are read only here, after enumeration.
    # They do not enter the generator, graph filter, normalization, or grouping.
    checks = []
    expected_totals = {
        "tree_seagull": (2, 2, "2"),
        "tree_quartic": (4, 4, "1"),
        "self_energy_photon_tadpole": (1, 1, "1"),
        "self_energy_scalar_tadpole": (4, 4, "1"),
        "four_scalar_photon_bubbles": (12, 8, "4"),
        "four_scalar_scalar_bubbles": (288, 80, "5/2"),
        "mixed_four_two_seagull_bubbles": (48, 16, "8"),
    }
    for name, (generated, accepted, weight) in expected_totals.items():
        item = by_name[name]
        checks.append(check_record(name + ": raw/accepted/normalized",
                                   [item["generated_compatible_pairings_without_external_external"],
                                    item["accepted_pairing_count"],
                                    item["total_normalized_weight"]["exact"]],
                                   [generated, accepted, weight]))
    allocation_expectations = {
        "four_scalar_photon_bubbles": [0, 2, 2, 2, 2, 0],
        "four_scalar_scalar_bubbles": [8, 16, 16, 16, 16, 8],
        "mixed_four_two_seagull_bubbles": [0, 4, 4, 4, 4, 0],
    }
    for name, expected in allocation_expectations.items():
        actual = [g["pairing_count"] for g in by_name[name]["ordered_external_allocations"]]
        checks.append(check_record(name + ": all six ordered external allocations", actual, expected))
    for name, expected in (
        ("self_energy_photon_tadpole", "1/2"),
        ("self_energy_scalar_tadpole", "1"),
    ):
        actual = by_name[name]["weight_relative_to_that_vertex_product"]["exact"]
        checks.append(check_record(name + ": relative to independently counted vertex", actual, expected))
    expected_class_weights = {
        "four_scalar_photon_bubbles": ["0", "1/2", "1/2"],
        "four_scalar_scalar_bubbles": ["1/2", "1", "1"],
        "mixed_four_two_seagull_bubbles": ["0", "1", "1"],
    }
    for name, expected in expected_class_weights.items():
        actual = [g["relative_weight_from_count_not_assigned_symmetry_factor"]["exact"]
                  for g in by_name[name]["vertex_exchange_classes"]]
        checks.append(check_record(name + ": derived weights by external partition", actual, expected))
    for item in cases:
        checks.append(check_record(
            item["case_id"] + ": exhaustive partition of generated pairings",
            item["accepted_pairing_count"] + sum(item["rejections"].values()),
            item["generated_compatible_pairings_without_external_external"]))
        expected_loops = 0 if item["input"]["selected_topology"] == "tree" else 1
        checks.append(check_record(
            item["case_id"] + ": all accepted graphs have selected loop number",
            sorted(item["loop_number_counts"]), [str(expected_loops)]))
    payload["checks"] = checks
    payload["status"] = "passed" if all(row["passed"] for row in checks) else "failed"
    payload["summary"] = {
        "case_count": len(cases),
        "generated_pairing_total": sum(c["generated_compatible_pairings_without_external_external"]
                                       for c in cases),
        "accepted_pairing_total": sum(c["accepted_pairing_count"] for c in cases),
        "explicit_ordered_allocations": sum(len(c.get("ordered_external_allocations", []))
                                            for c in cases),
        "checks_passed": sum(row["passed"] for row in checks),
        "checks_total": len(checks),
        "failed_checks": [row["check"] for row in checks if not row["passed"]],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("results_S65_wick.json"))
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit("Refusing to overwrite existing execution evidence: " + str(args.output))
    payload = {
        "schema_version": 1,
        "check_id": "S65_labelled_Wick_contractions",
        "execution": {
            "attempt_number": 1,
            "previous_attempts": [],
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "python_version": sys.version,
            "python_implementation": platform.python_implementation(),
            "python_executable": sys.executable,
            "platform": platform.platform(),
            "argv": sys.argv,
            "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "random_seed": None,
            "randomness": "none; exhaustive deterministic integer enumeration",
            "arithmetic": "Python integers and fractions.Fraction; no tolerance or rounding",
        },
        "model": {
            "local_monomials": {
                "seagull": "-e^2 phidag phi A^2",
                "quartic": "-lambda phidag^2 phi^2 / 4",
            },
            "allowed_contractions": [["phi", "phidag"], ["A", "A"]],
            "external_external_contractions": "forbidden by generator",
            "external_state_convention":
                "phi = integral(a exp(ipx)+bdag exp(-ipx)); incoming a gives phidag "
                "at external correlator insertion, outgoing a gives phi",
            "bosonic_pairing_weight": 1,
            "normal_ordered_interactions": False,
            "bubble_selection":
                "two labelled identical insertions; two external slots per vertex; "
                "exactly two internal lines, both cross vertices; connected and still "
                "connected after deleting any one internal line",
            "factor_convention":
                "Positive rational multiplicity after factoring couplings, (-i)^V "
                "from insertions, (1/i)^I from internal propagators, external propagators, "
                "spacetime/loop integrations, and photon Lorentz tensors",
            "dimension_and_metric":
                "Applicable to the book's (-+++) and d=4-epsilon; combinatorics "
                "does not numerically evaluate d, metric contractions, momenta, or regulators",
            "excluded_claims":
                "No UV/IR integral, Ward identity, Fock phase, gauge-propagator trace, "
                "or all-order diagram theorem is tested.",
        },
    }
    try:
        run(payload)
    except Exception:
        payload["status"] = "exception"
        payload["failure_traceback"] = traceback.format_exc()
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(json.dumps({"status": payload["status"], "output": str(args.output),
                      "summary": payload.get("summary"),
                      "code_sha256": payload["execution"]["code_sha256"]},
                     ensure_ascii=False, indent=2))
    return 0 if payload["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
