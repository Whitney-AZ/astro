"""Direct matrix action checks for the S79 SU(2)/U(2) four-gluon example."""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
from check_background78 import Poly, METRIC, dot

# Use I,sigma as the matrix basis so kappa=1 has integer coefficients.
# Each basis matrix is sqrt(2) times the article's unit-trace generator.
# Thus the central propagator is g^{mu nu}/(2 i P^2), and a four-external-leg
# coefficient is divided by 4 to recover the article's normalization (g^2=2).
SIGMA = [
    [[1, 0], [0, 1]], [[0, 1], [1, 0]],
    [[0, -1j], [1j, 0]], [[1, 0], [0, -1]],
]


def zero():
    return [[Poly() for _ in range(2)] for _ in range(2)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def scale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def mul(a, b):
    return [[a[i][0] * b[0][j] + a[i][1] * b[1][j] for j in range(2)] for i in range(2)]


def trace(a):
    return a[0][0] + a[1][1]


def coefficient(legs, variant):
    a = [zero() for _ in range(4)]
    for tag, (color, momentum, polarization) in enumerate(legs):
        for mu, i, j in product(range(4), range(2), range(2)):
            value = METRIC[mu] * polarization[mu] * SIGMA[color][i][j]
            if value:
                a[mu][i][j] += Poly({1 << tag: value})

    def derivative(m, mu):
        return [[Poly({mask: value * 1j * METRIC[mu] *
                       sum(leg[1][mu] for tag, leg in enumerate(legs) if mask & (1 << tag))
                       for mask, value in m[i][j].items()})
                 for j in range(2)] for i in range(2)]

    lagrangian = Poly()
    if variant == "compact":
        for mu, nu in product(range(4), repeat=2):
            d = derivative(a[nu], mu)
            factor = METRIC[mu] * METRIC[nu]
            lagrangian += -0.5 * factor * trace(mul(d, d))
            lagrangian += -2j * factor * trace(mul(mul(d, a[nu]), a[mu]))
            lagrangian += 0.5 * factor * trace(mul(mul(mul(a[mu], a[nu]), a[mu]), a[nu]))
    else:
        for mu, nu in product(range(4), repeat=2):
            commutator = add(mul(a[mu], a[nu]), scale(-1, mul(a[nu], a[mu])))
            f = add(add(derivative(a[nu], mu), scale(-1, derivative(a[mu], nu))), scale(-1j, commutator))
            lagrangian += -0.25 * METRIC[mu] * METRIC[nu] * trace(mul(f, f))
        gauge = zero()
        for mu in range(4):
            gauge = add(gauge, scale(METRIC[mu], add(derivative(a[mu], mu), scale(-1j, mul(a[mu], a[mu])))))
        if variant == "projected":
            half_trace = 0.5 * trace(gauge)
            gauge = [[gauge[i][j] + (-1) * half_trace if i == j else gauge[i][j]
                      for j in range(2)] for i in range(2)]
        lagrangian += -0.5 * trace(mul(gauge, gauge))
    return 1j * lagrangian.get((1 << len(legs)) - 1, 0)


def main():
    checks = []
    # Complete integrated polynomial identity: total external momentum is zero.
    for colors in [(1, 2, 3), (0, 1, 1), (1, 2, 1, 2), (0, 1, 0, 1)]:
        n = len(colors)
        momenta = [[(i + 1) * (mu + 2) - mu for mu in range(4)] for i in range(n - 1)]
        momenta += [[-sum(p[mu] for p in momenta) for mu in range(4)]]
        legs = [(c, momenta[i], [((i + 2) * (mu + 1)) % 7 - 3 for mu in range(4)])
                for i, c in enumerate(colors)]
        full, compact = coefficient(legs, "full"), coefficient(legs, "compact")
        checks.append(dict(kind="full_action_vs_compact", colors=colors,
                           full=str(full), compact=str(compact), residual=abs(full-compact),
                           passed=abs(full-compact) < 1e-10))

    scattering = []
    for energy, sine, cosine in [(1, 1, 0), (5, 4, 3), (13, 12, 5)]:
        momenta = [(energy, 0, 0, energy), (energy, 0, 0, -energy),
                   (-energy, -sine, 0, -cosine), (-energy, sine, 0, cosine)]
        polarization = (0, 0, 1, 0)
        legs = [(1, k, polarization) for k in momenta]
        null = [dot(k, k) for k in momenta]
        transverse = [dot(k, polarization) for k in momenta]
        su_contact = coefficient(legs, "projected") / 4
        full_contact = coefficient(legs, "full") / 4
        compact_contact = coefficient(legs, "compact") / 4
        exchanges = []
        su_exchanges = []
        for left, right in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
            p = [momenta[left[0]][mu] + momenta[left[1]][mu] for mu in range(4)]
            p2 = dot(p, p)
            assert p2 != 0
            for color in range(4):
                exchange = 0j
                for mu in range(4):
                    basis = [int(mu == nu) for nu in range(4)]
                    l = [(color, [-v for v in p], basis), legs[left[0]], legs[left[1]]]
                    r = [(color, p, basis), legs[right[0]], legs[right[1]]]
                    vl = coefficient(l, "full")
                    vr = coefficient(r, "full")
                    exchange += vl * METRIC[mu] * vr / (2j * p2) / 4
                if color == 0:
                    exchanges.append(dict(channel=[left, right], momentum_squared=p2, value=str(exchange)))
                else:
                    su_exchanges.append(exchange)
        total_central = sum(complex(x["value"]) for x in exchanges)
        residual = full_contact + total_central
        passed = (null == [0]*4 and transverse == [0]*4 and su_contact == 0
                  and all(abs(v) < 1e-10 for v in su_exchanges)
                  and abs(full_contact-6j) < 1e-10 and full_contact == compact_contact
                  and abs(residual) < 1e-10)
        scattering.append(dict(energy=energy, momenta=momenta, polarization=polarization,
                               k_squared=null, k_dot_epsilon=transverse,
                               projected_SU2_contact=str(su_contact),
                               unprojected_contact=str(full_contact),
                               compact_contact=str(compact_contact),
                               central_exchanges=exchanges,
                               noncentral_exchange_max=max(abs(v) for v in su_exchanges),
                               complete_U2_result=str(residual), passed=passed))
    out = dict(
        task="S79: matrix action expansion and central exchange at three transverse four-point configurations",
        utc_time=datetime.now(timezone.utc).isoformat(),
        command="python3 scripts/srednicki/check_gervais79.py",
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        helper_sha256=sha256(Path(__file__).with_name("check_background78.py").read_bytes()).hexdigest(),
        physical_g_squared=2, basis="Pauli plus identity, then divide four-leg amplitudes by 4",
        scope="Finite SU(2)/U(2) matrix and tree samples; does not prove general BRST or global gauge equivalence",
        polynomial_checks=checks, scattering_checks=scattering,
        all_passed=all(x["passed"] for x in checks+scattering))
    path=Path(__file__).resolve().parents[2]/"checks/srednicki/gervais79-check.json"
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(out,ensure_ascii=False,indent=2))
    if not out["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
