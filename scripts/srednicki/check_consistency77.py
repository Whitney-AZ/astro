#!/usr/bin/env python3
"""Solve the specified S77 consistency ansatz over an exact graded trace algebra.

The coefficients of w aab, w aba, w baa and w aaaa are unknown inputs.
No anomaly coefficients or expected solution are inserted in this program.
Only the standard library is used. Polynomials are free noncommuting words;
trace cyclicity uses total form-plus-ghost parity.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys

DEGREES = {"a": (1, 0), "b": (2, 0), "w": (0, 1), "q": (1, 1)}
LETTERS = tuple(sorted(DEGREES))


def poly(terms):
    out = defaultdict(F)
    for word, coefficient in terms:
        out[tuple(word)] += F(coefficient)
    return {w: c for w, c in out.items() if c}


D_RULES = {
    "a": poly([("b", 1)]),
    "b": {},
    "w": poly([("q", 1)]),
    "q": {},
}
S_RULES = {
    "a": poly([("q", -1), ("aw", -1), ("wa", -1)]),
    "b": poly([("bw", 1), ("wb", -1), ("aq", -1), ("qa", 1)]),
    "w": poly([("ww", -1)]),
    "q": poly([("qw", 1), ("wq", -1)]),
}
ANSATZ_WORDS = ("wbb", "waab", "waba", "wbaa", "waaaa")
UNKNOWN_NAMES = ("b1", "b2", "b3", "c")


def degree(word):
    return tuple(sum(DEGREES[x][j] for x in word) for j in (0, 1))


def parity(word):
    return sum(degree(word)) % 2


def add(*polynomials):
    return poly((w, c) for p in polynomials for w, c in p.items())


def scale(p, c):
    return {w: F(c) * v for w, v in p.items() if F(c) * v}


def derive(p, rules):
    terms = []
    for word, coefficient in p.items():
        prefix_parity = 0
        for i, letter in enumerate(word):
            sign = -1 if prefix_parity else 1
            for replacement, factor in rules[letter].items():
                terms.append((word[:i] + replacement + word[i + 1:],
                              coefficient * sign * factor))
            prefix_parity ^= parity((letter,))
    return poly(terms)


@lru_cache(None)
def trace_word(word):
    """Return representative and relative sign, or None for a trace-zero word."""
    if not word:
        return (), 1
    rotations = {}
    for i in range(len(word)):
        rotated = word[i:] + word[:i]
        sign = (-1) ** (parity(word[:i]) * parity(word[i:]))
        if rotated in rotations and rotations[rotated] != sign:
            return None
        rotations[rotated] = sign
    representative = min(rotations)
    return representative, rotations[representative]


def trace(p):
    terms = []
    for word, coefficient in p.items():
        canonical = trace_word(word)
        if canonical is not None:
            representative, sign = canonical
            terms.append((representative, sign * coefficient))
    return poly(terms)


@lru_cache(None)
def words(form_degree, ghost_number):
    if form_degree == ghost_number == 0:
        return ((),)
    out = []
    for letter in LETTERS:
        f, g = DEGREES[letter]
        if f <= form_degree and g <= ghost_number:
            out.extend((letter,) + tail
                       for tail in words(form_degree - f, ghost_number - g))
    return tuple(out)


def trace_basis(f, g):
    result = set()
    for word in words(f, g):
        reduced = trace_word(word)
        if reduced is not None:
            result.add(reduced[0])
    return sorted(result, key=lambda w: (len(w), w))


def vector(p, basis):
    unexpected = set(p) - set(basis)
    if unexpected:
        raise ValueError(f"Polynomial outside requested basis: {unexpected}")
    return [p.get(word, F(0)) for word in basis]


def rref_solve(matrix, rhs):
    ncols = len(matrix[0])
    a = [[F(v) for v in row] + [F(b)] for row, b in zip(matrix, rhs)]
    pivots = []
    row = 0
    for col in range(ncols):
        found = next((i for i in range(row, len(a)) if a[i][col]), None)
        if found is None:
            continue
        a[row], a[found] = a[found], a[row]
        pivot = a[row][col]
        a[row] = [v / pivot for v in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                factor = a[i][col]
                a[i] = [v - factor * u for v, u in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    incompatible = [i for i, r in enumerate(a) if not any(r[:-1]) and r[-1]]
    if incompatible:
        return {"consistent": False, "rref": a, "incompatible_rows": incompatible}
    particular = [F(0)] * ncols
    for i, col in enumerate(pivots):
        particular[col] = a[i][-1]
    free = [j for j in range(ncols) if j not in pivots]
    nullspace = []
    for col in free:
        n = [F(0)] * ncols
        n[col] = F(1)
        for i, pivot in enumerate(pivots):
            n[pivot] = -a[i][col]
        nullspace.append(n)
    return {"consistent": True, "rref": a, "pivots": pivots,
            "free_columns": free, "particular": particular, "nullspace": nullspace}


def serial_poly(p):
    return [{"word": "".join(w), "coefficient": str(c)}
            for w, c in sorted(p.items(), key=lambda x: (len(x[0]), x[0]))]


def readable(p):
    return " + ".join(f"({c}) Tr({''.join(w) or '1'})"
                      for w, c in sorted(p.items(),
                                         key=lambda x: (len(x[0]), x[0]))) or "0"


def rational_json(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: rational_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [rational_json(v) for v in value]
    return value


def generator_checks():
    out = {}
    for letter in LETTERS:
        p = poly([(letter, 1)])
        dd = derive(derive(p, D_RULES), D_RULES)
        ss = derive(derive(p, S_RULES), S_RULES)
        ds = add(derive(derive(p, S_RULES), D_RULES),
                 derive(derive(p, D_RULES), S_RULES))
        out[letter] = {"d_squared": serial_poly(dd),
                       "s_squared": serial_poly(ss),
                       "d_s_plus_s_d": serial_poly(ds)}
    return out


def trace_descent_check(f, g, rules):
    failures = []
    for word in words(f, g):
        raw = poly([(word, 1)])
        residual = add(trace(derive(raw, rules)),
                       scale(trace(derive(trace(raw), rules)), -1))
        if residual:
            failures.append({"word": "".join(word), "residual": serial_poly(residual)})
    return {"input_degree": [f, g], "raw_words_checked": len(words(f, g)),
            "failures": failures}


def main():
    target = trace_basis(4, 2)
    primitives = trace_basis(3, 2)
    s_columns = [trace(derive(poly([(w, 1)]), S_RULES)) for w in ANSATZ_WORDS]
    d_columns = [trace(derive(poly([(w, 1)]), D_RULES)) for w in primitives]
    all_columns = s_columns[1:] + [scale(p, -1) for p in d_columns]
    columns = [vector(p, target) for p in all_columns]
    matrix = [list(row) for row in zip(*columns)]
    rhs = [-c for c in vector(s_columns[0], target)]
    solved = rref_solve(matrix, rhs)
    checks = generator_checks()
    descent_d = trace_descent_check(3, 2, D_RULES)
    descent_s = trace_descent_check(4, 1, S_RULES)
    result = {
        "task": "S77: solve s integrated Tr[w(bb+b1*aab+b2*aba+b3*baa+c*aaaa)]=0 modulo d",
        "execution": {
            "utc_time": datetime.now(timezone.utc).isoformat(),
            "command": "python3 scripts/srednicki/check_consistency77.py",
            "adapted_source": "/Users/Admin/Documents/Srednicki-QFT-Trans/checks/s77_consistency_check.py",
            "adapted_source_sha256": "412197408e5a59870517d4057a8b04885d44209347225778f603a21c4f298a53",
            "python_version": sys.version,
            "software": "Python standard library; fractions.Fraction exact rational arithmetic",
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "expected_coefficients_were_not_inputs": True,
        },
        "conventions": {
            "degrees_form_ghost": DEGREES,
            "parity": "(form degree + ghost number) mod 2",
            "d_rules": {x: serial_poly(p) for x, p in D_RULES.items()},
            "s_rules": {x: serial_poly(p) for x, p in S_RULES.items()},
            "trace_relation": "Tr(P Q)=(-1)^(total_parity(P)*total_parity(Q)) Tr(Q P)",
            "integrated_equivalence": "identify d of every (form degree 3, ghost number 2) trace word with zero",
            "density_ansatz": {"fixed": {"wbb": "1"},
                              "unknown": dict(zip(UNKNOWN_NAMES, ANSATZ_WORDS[1:]))},
        },
        "spaces": {
            "target_degree": [4, 2], "primitive_degree": [3, 2],
            "target_raw_word_count": len(words(4, 2)),
            "primitive_raw_word_count": len(words(3, 2)),
            "target_trace_basis": ["".join(w) for w in target],
            "primitive_trace_basis": ["".join(w) for w in primitives],
            "linear_matrix_shape": [len(matrix), len(matrix[0])],
            "column_order": list(UNKNOWN_NAMES) + ["primitive:" + "".join(w) for w in primitives],
        },
        "generator_checks_in_free_algebra": checks,
        "operators_descend_to_trace": {"d": descent_d, "s": descent_s},
        "linear_system": {"matrix": matrix, "rhs": rhs, "solution": solved},
        "scope": [
            "All words in the two stated bidegrees of the free algebra are included.",
            "No finite-matrix-size trace identities or extra Lie-algebra identities are imposed.",
            "The input BRST rules and the ansatz are assumed; this is not a derivation of a quantum anomaly.",
            "Modulo a total derivative means compact support or boundary conditions that remove that integral.",
            "This calculation does not establish global gauge-anomaly cancellation."
        ],
    }
    if solved["consistent"]:
        particular = solved["particular"]
        theta = particular[:4]
        certificate = poly(zip(primitives, particular[4:]))
        density = add(poly([(ANSATZ_WORDS[0], 1)]),
                      *(poly([(w, c)]) for w, c in zip(ANSATZ_WORDS[1:], theta)))
        s_density = trace(derive(density, S_RULES))
        d_certificate = trace(derive(certificate, D_RULES))
        residual = add(s_density, scale(d_certificate, -1))
        projection = [n[:4] for n in solved["nullspace"]]
        unique = all(not any(n) for n in projection)
        result["obtained"] = {
            "coefficients": dict(zip(UNKNOWN_NAMES, theta)),
            "coefficient_solution_unique": unique,
            "homogeneous_parameter_directions": projection,
            "rank": len(solved["pivots"]),
            "free_certificate_or_parameter_directions": len(solved["free_columns"]),
            "density_original_words": serial_poly(density),
            "primitive_certificate": serial_poly(certificate),
            "certificate_equation": "s Tr(density) = d Tr(primitive_certificate)",
            "readable_primitive": readable(certificate),
            "s_density_trace": serial_poly(s_density),
            "d_primitive_trace": serial_poly(d_certificate),
            "exact_certificate_residual": serial_poly(residual),
        }
        sanity = not any(p for check in checks.values() for p in check.values())
        result["all_required_checks_passed"] = (
            sanity and not descent_d["failures"] and not descent_s["failures"]
            and not residual
        )
    else:
        result["all_required_checks_passed"] = False
    output = Path(__file__).resolve().parents[2] / "checks/srednicki/consistency77-check.json"
    output.write_text(json.dumps(rational_json(result), ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(rational_json({
        "output": str(output), "spaces": result["spaces"],
        "obtained": result.get("obtained"),
        "all_required_checks_passed": result["all_required_checks_passed"],
    }), ensure_ascii=False, indent=2))
    return 0 if result["all_required_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

