"""Compare the six background vertices with direct multilinear action expansion.

Finite SU(2) samples with integer momenta/polarizations, g=2, xi=1,2.
Dyadic complex arithmetic is exact at these sizes. Ghost coefficients are
extracted in the fixed antighost-before-ghost order; no closed ghost loops.
"""
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

METRIC = (-1, 1, 1, 1)
G = 2


def eps(a, b, c):
    if len({a, b, c}) < 3:
        return 0
    return 1 if (a, b, c) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1


class Poly(dict):
    """Multilinear tagged plane waves, with each source tag nilpotent."""
    def __add__(self, other):
        out = defaultdict(complex, self)
        for mask, value in other.items():
            out[mask] += value
        return Poly({k: v for k, v in out.items() if v})

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            return Poly({k: v * other for k, v in self.items() if v * other})
        out = defaultdict(complex)
        for a, va in self.items():
            for b, vb in other.items():
                if not a & b:
                    out[a | b] += va * vb
        return Poly({k: v for k, v in out.items() if v})

    __rmul__ = __mul__


def dot(a, b):
    return sum(m * x * y for m, x, y in zip(METRIC, a, b))


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def action_coefficient(legs, xi):
    n = len(legs)
    bg = [[Poly() for _ in range(4)] for _ in range(3)]
    q = [[Poly() for _ in range(4)] for _ in range(3)]
    cb, c = [Poly() for _ in range(3)], [Poly() for _ in range(3)]
    for tag, leg in enumerate(legs):
        kind, color, momentum, polarization = leg
        if kind in ("B", "q"):
            target = bg if kind == "B" else q
            for mu in range(4):
                target[color][mu] += Poly({1 << tag: METRIC[mu] * polarization[mu]})
        else:
            (cb if kind == "barc" else c)[color] += Poly({1 << tag: 1})
    total = [[bg[a][mu] + q[a][mu] for mu in range(4)] for a in range(3)]

    def derivative(poly, mu):
        return Poly({mask: value * 1j * METRIC[mu] *
                     sum(leg[2][mu] for i, leg in enumerate(legs) if mask & (1 << i))
                     for mask, value in poly.items()})

    def cov_derivative(field, connection, a, mu):
        out = derivative(field[a], mu)
        for b, d in product(range(3), repeat=2):
            out += G * eps(a, b, d) * connection[b][mu] * field[d]
        return out

    lagrangian = Poly()
    for a, mu, nu in product(range(3), range(4), range(4)):
        f = derivative(total[a][nu], mu) + (-1) * derivative(total[a][mu], nu)
        for b, d in product(range(3), repeat=2):
            f += G * eps(a, b, d) * total[b][mu] * total[d][nu]
        lagrangian += (-0.25 * METRIC[mu] * METRIC[nu]) * f * f
    for a in range(3):
        gauge = Poly()
        for mu in range(4):
            field = [q[b][mu] for b in range(3)]
            gauge += METRIC[mu] * cov_derivative(field, bg, a, mu)
        lagrangian += (-0.5 / xi) * gauge * gauge
        for mu in range(4):
            lagrangian += (-METRIC[mu]) * cov_derivative(cb, bg, a, mu) * cov_derivative(c, total, a, mu)
    return 1j * lagrangian.get((1 << n) - 1, 0)


def vertex_formula(legs, xi):
    kind = tuple(leg[0] for leg in legs)
    colors = [leg[1] for leg in legs]
    momenta = [leg[2] for leg in legs]
    vectors = [leg[3] for leg in legs]
    if kind == ("B", "q", "q"):
        a, b, c = colors
        k, p, r = momenta
        u, v, w = vectors
        tensor = dot(sub(p, r), u) * dot(v, w)
        tensor += dot(sub(r, k), v) * dot(w, u) + dot(sub(k, p), w) * dot(u, v)
        tensor += (dot(p, v) * dot(u, w) - dot(r, w) * dot(u, v)) / xi
        return -G * eps(a, b, c) * tensor
    if kind in (("B", "B", "q", "q"), ("B", "q", "q", "q")):
        a, b, c, d = colors
        u, v, w, z = vectors
        fab = sum(eps(a, b, e) * eps(c, d, e) for e in range(3))
        fac = sum(eps(a, c, e) * eps(b, d, e) for e in range(3))
        fad = sum(eps(a, d, e) * eps(b, c, e) for e in range(3))
        tensor = fab * (dot(u, w) * dot(v, z) - dot(u, z) * dot(v, w))
        tensor += fac * (dot(u, v) * dot(w, z) - dot(u, z) * dot(v, w))
        tensor += fad * (dot(u, v) * dot(w, z) - dot(u, w) * dot(v, z))
        if kind[1] == "B":
            tensor += (fac * dot(u, w) * dot(v, z) + fad * dot(u, z) * dot(v, w)) / xi
        return -1j * G**2 * tensor
    if kind == ("B", "barc", "c"):
        a, i, j = colors
        return -G * eps(a, i, j) * dot(sub(momenta[1], momenta[2]), vectors[0])
    a, b, i, j = colors
    ab = -sum(eps(a, i, t) * eps(b, t, j) for t in range(3))
    if kind[1] == "B":
        ab -= sum(eps(b, i, t) * eps(a, t, j) for t in range(3))
    return -1j * G**2 * ab * dot(vectors[0], vectors[1])


def main():
    cases = []
    families = [
        (("B", "q", "q"), (0, 1, 2)),
        (("B", "B", "q", "q"), (0, 1, 0, 1)),
        (("B", "q", "q", "q"), (0, 1, 0, 1)),
        (("B", "barc", "c"), (0, 1, 2)),
        (("B", "B", "barc", "c"), (0, 1, 1, 0)),
        (("B", "q", "barc", "c"), (0, 1, 1, 0)),
    ]
    for seed, xi, (kinds, colors) in product(range(3), (1, 2), families):
        n = len(kinds)
        momenta = [[(i + 1) * (mu + 2) - seed * (mu - 1) for mu in range(4)] for i in range(n - 1)]
        momenta.append([-sum(p[mu] for p in momenta) for mu in range(4)])
        legs = [(kind, (color + seed) % 3, momenta[i],
                 [((i + 2) * (mu + seed + 1)) % 7 - 3 for mu in range(4)])
                for i, (kind, color) in enumerate(zip(kinds, colors))]
        actual = action_coefficient(legs, xi)
        expected = vertex_formula(legs, xi)
        cases.append(dict(family=" ".join(kinds), seed=seed, xi=xi, legs=legs,
                          action_iV=str(actual), formula_iV=str(expected),
                          residual=str(actual - expected), passed=actual == expected))
    out = dict(
        task="S78: six mixed vertices from full Yang-Mills, gauge-fixing and ghost actions",
        utc_time=datetime.now(timezone.utc).isoformat(),
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        command="python3 scripts/srednicki/check_background78.py",
        scope="36 SU(2) off-shell polynomial samples; exact dyadic complex values; no loop integration or general-group proof",
        cases=cases, nonzero_cases=sum(complex(c["action_iV"]) != 0 for c in cases),
        all_passed=all(c["passed"] for c in cases))
    path=Path(__file__).resolve().parents[2] / "checks/srednicki/background78-check.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "cases"}, indent=2))
    if not out["all_passed"]:
        print(json.dumps([c for c in cases if not c["passed"]], indent=2))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
