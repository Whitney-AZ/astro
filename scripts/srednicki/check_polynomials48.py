#!/usr/bin/env python3
"""One new exact check of S48 four separate Phi polynomials and crossing weight.

Expand the ordered four-factor Clifford traces, using the already derived
even-trace recursion and an independently specified scalar-product table.
No prior spin-sum program is imported or executed. Coefficients are Fraction.
"""
import collections
import datetime
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import platform
import sys

NAMES = ("s", "u", "m", "M")


class Poly:
    def __init__(self, value=0):
        self.terms = (
            {key: F(val) for key, val in value.items() if val}
            if isinstance(value, dict)
            else ({(0, 0, 0, 0): F(value)} if value else {})
        )

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        out = collections.defaultdict(F, self.terms)
        for monomial, coefficient in other.terms.items():
            out[monomial] += coefficient
        return Poly(dict(out))

    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, Poly) else -F(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        out = collections.defaultdict(F)
        for ma, ca in self.terms.items():
            for mb, cb in other.terms.items():
                out[tuple(a + b for a, b in zip(ma, mb))] += ca * cb
        return Poly(dict(out))

    __rmul__ = __mul__

    def __pow__(self, n):
        out = Poly(1)
        for _ in range(n):
            out *= self
        return out

    def substitute(self, index, value):
        out = Poly()
        for monomial, coefficient in self.terms.items():
            rest = list(monomial)
            exponent = rest[index]
            rest[index] = 0
            out += Poly({tuple(rest): coefficient}) * value**exponent
        return out

    def encoded(self):
        return [
            {"powers_s_u_m_M": list(key), "coefficient": str(value)}
            for key, value in sorted(self.terms.items(), reverse=True)
        ]


def variable(i):
    exponents = [0] * 4
    exponents[i] = 1
    return Poly({tuple(exponents): F(1)})


s, u, m, M = [variable(i) for i in range(4)]
r, R = m**2, M**2
t = 2 * r + 2 * R - s - u


def sym_table(entries):
    out = {}
    for (a, b), value in entries.items():
        out[a, b] = out[b, a] = value
    return out


electron_dot = sym_table({
    ("p", "p"): -r, ("pprime", "pprime"): -r,
    ("k", "k"): -R, ("kprime", "kprime"): -R,
    ("p", "pprime"): t * F(1, 2) - r,
    ("k", "kprime"): t * F(1, 2) - R,
    ("p", "k"): (r + R - s) * F(1, 2),
    ("pprime", "kprime"): (r + R - s) * F(1, 2),
    ("p", "kprime"): (u - r - R) * F(1, 2),
    ("pprime", "k"): (u - r - R) * F(1, 2),
})
annihilation_dot = sym_table({
    ("p1", "p1"): -r, ("p2", "p2"): -r,
    ("k1", "k1"): -R, ("k2", "k2"): -R,
    ("p1", "p2"): r - s * F(1, 2),
    ("k1", "k2"): R - s * F(1, 2),
    ("p1", "k1"): (t - r - R) * F(1, 2),
    ("p2", "k2"): (t - r - R) * F(1, 2),
    ("p1", "k2"): (u - r - R) * F(1, 2),
    ("p2", "k1"): (u - r - R) * F(1, 2),
})


def trace_word(word, dot):
    if len(word) % 2:
        return Poly()
    if not word:
        return Poly(4)
    return sum(
        ((-1)**j * dot[word[0], word[j]]
         * trace_word(word[1:j] + word[j + 1:], dot) for j in range(1, len(word))),
        Poly(),
    )


def trace_product(factors, dot):
    # Factor is c*I + sign*slash(vector); preserve its position in each word.
    answer = Poly()
    for choices in itertools.product((0, 1), repeat=len(factors)):
        scalar, word = Poly(1), []
        for choose_vector, (constant, vector, sign) in zip(choices, factors):
            if choose_vector:
                scalar *= sign
                word.append(vector)
            else:
                scalar *= constant
        answer += scalar * trace_word(tuple(word), dot)
    return answer


def main():
    pp, p = (m, "pprime", -1), (m, "p", -1)
    ns, nu = (2 * m, "k", -1), (2 * m, "kprime", 1)
    factors = {"ss": (pp, ns, p, ns), "uu": (pp, nu, p, nu),
               "su": (pp, ns, p, nu), "us": (pp, nu, p, ns)}
    computed = {name: F(1, 2) * trace_product(fs, electron_dot) for name, fs in factors.items()}
    source = {
        "ss": -s*u + r*(9*s+u) + 7*r**2 - 8*r*R + R**2,
        "uu": -s*u + r*(9*u+s) + 7*r**2 - 8*r*R + R**2,
        "su": s*u + 3*r*(s+u) + 9*r**2 - 8*r*R - R**2,
        "us": s*u + 3*r*(s+u) + 9*r**2 - 8*r*R - R**2,
    }
    main_residuals = {name: (computed[name] - source[name]).encoded() for name in source}
    q2, p1 = (-m, "p2", -1), (m, "p1", -1)
    nt, nu = (2 * m, "k1", 1), (2 * m, "k2", 1)
    ann_factors = {"ss": (q2, nt, p1, nt), "uu": (q2, nu, p1, nu),
                   "su": (q2, nt, p1, nu), "us": (q2, nu, p1, nt)}
    # Name ss maps to annihilation tt; keeping keys makes the crossing explicit.
    ann = {name: F(1, 4) * trace_product(fs, annihilation_dot) for name, fs in ann_factors.items()}
    crossed = {name: phi.substitute(0, t) for name, phi in computed.items()}
    corrected_residuals = {name: (ann[name] + F(1, 2) * crossed[name]).encoded() for name in ann}
    source_claim_residuals = {name: (ann[name] + crossed[name]).encoded() for name in ann}
    wrong_factor_rejected = all(source_claim_residuals[name] for name in ann)
    passed = not any(main_residuals.values()) and not any(corrected_residuals.values()) and wrong_factor_rejected
    output = {
        "status": "pass" if passed else "fail",
        "executed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "python_version": sys.version, "platform": platform.platform(),
        "dependencies": "Python standard library only; fractions.Fraction exact coefficients",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "random_seed": None, "sampling": "Exact four-variable polynomials; no random draws.",
        "variables": list(NAMES), "constraint": "t=2m^2+2M^2-s-u",
        "clifford_and_trace": "{gamma,gamma}=-2g;Tr1=4;even trace recursion with (-1)^j dot;odd trace0",
        "electron_factors": "Pprime, Ns/Nu, P, Ns/Nu;P=-slashp+m;Ns=-slashk+2m;Nu=+slashkprime+2m",
        "annihilation_factors": "Q2,Nt/Nu,P1,Nt/Nu;Q2=-slashp2-m;Nt=+slashk1+2m;Nu=+slashk2+2m",
        "average_factors": {"electron_scalar": "1/2", "annihilation": "1/4"},
        "electron_polynomials": {name: value.encoded() for name, value in computed.items()},
        "source48_26_to_29_residuals": main_residuals,
        "corrected_crossing_minus_half_residuals": corrected_residuals,
        "source48_2_minus_one_residuals": source_claim_residuals,
        "source48_2_wrong_factor_rejected": wrong_factor_rejected,
        "exact_zero_comparisons": 8, "intentional_wrong_factor_controls": 4,
        "arithmetic_error": "0:exact rational polynomial coefficients",
        "limitations": "Checks algebraic numerators and crossing spin-average weights only; no new flux integral, loop correction, generic crossing analyticity theorem or optional decay computation.",
    }
    destination = Path("checks/srednicki/polynomials48-check.json")
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": output["status"], "exact_zero_comparisons": 8,
                      "intentional_wrong_factor_controls": 4,
                      "source48_2_wrong_factor_rejected": wrong_factor_rejected, "output": str(destination)}))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
