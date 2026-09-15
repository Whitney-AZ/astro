#!/usr/bin/env python3
"""One new S50 check: source-phase massless spinors, brackets, Fierz and tree amplitude.

No earlier project check is imported or executed. Input four-vectors are
contravariant, future null, with g=(-,+,+,+). All comparisons use actually
multiplied 4x4 matrices or independently specified momentum contractions.
"""
from pathlib import Path
import datetime as dt
import hashlib
import itertools
import json
import platform
import sys
import numpy as np

OUT = Path("checks/srednicki/spinor-helicity50-check.json")
TOL = 2e-12
G = np.array([-1., 1., 1., 1.])
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
PAULI = [
    np.array([[0, 1], [1, 0]], complex),
    np.array([[0, -1j], [1j, 0]], complex),
    np.array([[1, 0], [0, -1]], complex),
]
GAMMA = [np.block([[Z2, I2], [I2, Z2]])]
GAMMA += [np.block([[Z2, s], [-s, Z2]]) for s in PAULI]
GAMMA5 = np.diag([-1., -1., 1., 1.])
PL = (np.eye(4) - GAMMA5) / 2
E = np.array([[0, -1], [1, 0]], complex)  # lower epsilon
U = -E                                      # upper epsilon
C = np.block([[E, Z2], [Z2, -E]])
POINTS = {
    "p": [5., 3., 0., 4.],
    "q": [4., 0., 4., 0.],
    "r": [3., -1., 2., -2.],
    "s": [7., 6., 3., 2.],
}
MOM = {k: np.array(v) for k, v in POINTS.items()}
CM = {
    "p": [5., 3., 0., 4.],
    "k": [5., -3., 0., -4.],
    "pprime": [5., 0., 4., 3.],
    "kprime": [5., 0., -4., -3.],
}
PHASES = {"p": .173, "k": -.419, "pprime": .731, "kprime": -.293}
COUPLING = .7
records = []

def dot(p, q):
    return float(np.dot(p * G, q))

def slash(p):
    return sum((p[mu] * G[mu] * GAMMA[mu] for mu in range(4)),
               np.zeros((4, 4), complex))

def phi(p, phase=0.):
    w = float(p[0])
    theta = np.arccos(np.clip(p[3] / w, -1., 1.))
    azimuth = np.arctan2(p[2], p[1])
    value = np.sqrt(2 * w) * np.array(
        [-np.sin(theta / 2) * np.exp(-1j * azimuth), np.cos(theta / 2)],
        complex)
    return np.exp(1j * phase) * value

def spinors(z):
    return {
        "-": np.concatenate([z, np.zeros(2, complex)]),
        "+": np.concatenate([np.zeros(2, complex), U @ z.conjugate()]),
    }

def bar(u):
    return u.conjugate() @ GAMMA[0]

def square(a, b):
    return (U @ a) @ b

def angle(a, b):
    return a.conjugate() @ U @ b.conjugate()

def current(a, b, left_helicity, right_helicity):
    sa, sb = spinors(a), spinors(b)
    return np.array([bar(sa[left_helicity]) @ gam @ sb[right_helicity]
                     for gam in GAMMA])

def packed(z):
    arr = np.asarray(z)
    if arr.ndim == 0:
        v = complex(arr)
        return [float(v.real), float(v.imag)]
    return [packed(v) for v in arr]

def compare(label, left, right, retain=False):
    a, b = np.asarray(left, complex), np.asarray(right, complex)
    if a.shape != b.shape:
        raise ValueError((label, a.shape, b.shape))
    err = float(np.max(np.abs(a - b)))
    scale = max(1., float(np.max(np.abs(a))), float(np.max(np.abs(b))))
    rec = {"label": label, "shape": list(a.shape),
           "max_absolute_error": err, "normalized_error": err / scale,
           "pass": err / scale <= TOL}
    if retain:
        rec.update(actual=packed(a), expected=packed(b))
    records.append(rec)

def epsilon_contraction(vectors):
    cov = [p * G for p in vectors]
    result = 0.
    for perm in itertools.permutations(range(4)):
        inversions = sum(perm[i] > perm[j]
                         for i in range(4) for j in range(i + 1, 4))
        term = (-1.) ** inversions
        for row, col in enumerate(perm):
            term *= cov[row][col]
        result += term
    return float(result)

def bracket_amplitudes(z):
    a, b, c, d = (z[k] for k in ["p", "k", "pprime", "kprime"])
    return {
        "++": -COUPLING**2 * (square(c, b) / square(a, b)
                              + square(c, d) / square(a, d)),
        "--": -COUPLING**2 * (angle(c, b) / angle(a, b)
                              + angle(c, d) / angle(a, d)),
        "+-": 0j, "-+": 0j,
    }

def direct_amplitudes(mom, z):
    s_ch = mom["p"] + mom["k"]
    u_ch = mom["p"] - mom["kprime"]
    chain = -slash(s_ch) / dot(s_ch, s_ch) - slash(u_ch) / dot(u_ch, u_ch)
    si, so = spinors(z["p"]), spinors(z["pprime"])
    return {ho + hi: COUPLING**2 * (bar(so[ho]) @ chain @ si[hi])
            for ho in ["+", "-"] for hi in ["+", "-"]}

# The four independent test directions deliberately give a nonzero epsilon term.
for name, p in MOM.items():
    assert p[0] > 0 and dot(p, p) == 0
zs = {name: phi(p) for name, p in MOM.items()}
for name, p in MOM.items():
    z = zs[name]
    p_lower = -p[0] * I2 + sum(p[j + 1] * PAULI[j] for j in range(3))
    compare("rank_one_" + name, -np.outer(z, z.conjugate()), p_lower)
    ss = spinors(z)
    for h in ["+", "-"]:
        opposite = "-" if h == "+" else "+"
        compare("massless_C_phase_" + name + h, C @ bar(ss[h]).T, ss[opposite])

for a, b in itertools.combinations(MOM, 2):
    x, y = zs[a], zs[b]
    compare("angle_conjugate_" + a + b, angle(x, y),
            np.conjugate(square(y, x)))
    compare("bracket_dot_" + a + b, angle(x, y) * square(y, x),
            -2 * dot(MOM[a], MOM[b]))
    compare("bracket_Dirac_" + a + b,
            bar(spinors(x)["+"]) @ spinors(y)["-"], square(x, y))

p, q, r, s = [MOM[x] for x in ["p", "q", "r", "s"]]
a, b, c, d = [zs[x] for x in ["p", "q", "r", "s"]]
schouten_terms = [angle(a, b) * angle(c, d),
                  angle(a, c) * angle(d, b),
                  angle(a, d) * angle(b, c)]
compare("Schouten", sum(schouten_terms), 0, retain=True)
four_brackets = angle(a, b) * square(b, c) * angle(c, d) * square(d, a)
trace = np.trace(PL @ slash(p) @ slash(q) @ slash(r) @ slash(s))
eps = epsilon_contraction([p, q, r, s])
real_part = 2 * (dot(p, q) * dot(r, s) - dot(p, r) * dot(q, s)
                + dot(p, s) * dot(q, r))
compare("four_brackets_vs_projected_trace", four_brackets, trace, retain=True)
compare("projected_trace_vs_invariants", trace, real_part + 2j * eps, retain=True)
wrong_epsilon_value = real_part - 2j * eps
wrong_epsilon_rejected = bool(abs(trace - wrong_epsilon_value) > 1)

jL = current(a, b, "-", "-")
jR_reversed = current(b, a, "+", "+")
compare("single_gamma_reversal_50_38", jL, jR_reversed)
compare("single_gamma_conjugate_50_39", jL.conjugate(),
        current(b, a, "-", "-"))
compare("single_gamma_norm_50_40", current(a, a, "-", "-"), 2*p)
compare("single_gamma_zero_50_41", current(a, b, "-", "+"), np.zeros(4))
compare("single_gamma_zero_50_42", current(a, b, "+", "-"), np.zeros(4))
sa, sb = spinors(a), spinors(b)
compare("matrix_Fierz_50_43", -.5 * sum(
    (G[mu] * jL[mu] * GAMMA[mu] for mu in range(4)),
    np.zeros((4, 4), complex)),
    np.outer(sb["-"], bar(sa["-"])) + np.outer(sa["+"], bar(sb["+"])))
jR = current(a, b, "+", "+")
compare("matrix_Fierz_50_44", -.5 * sum(
    (G[mu] * jR[mu] * GAMMA[mu] for mu in range(4)),
    np.zeros((4, 4), complex)),
    np.outer(sb["+"], bar(sa["+"])) + np.outer(sa["-"], bar(sb["-"])))
compare("current_Fierz_50_45", np.sum(G * jR * current(c, d, "-", "-")),
        2 * square(a, d) * angle(b, c), retain=True)

# A physical non-collinear elastic configuration and independent spinor rephasings.
cm = {k: np.array(v) for k, v in CM.items()}
assert np.array_equal(cm["p"] + cm["k"], cm["pprime"] + cm["kprime"])
zcm = {k: phi(p) for k, p in cm.items()}
direct = direct_amplitudes(cm, zcm)
brackets = bracket_amplitudes(zcm)
for helicities in direct:
    compare("massless_tree_" + helicities, brackets[helicities],
            direct[helicities], retain=True)
s_inv = -dot(cm["p"] + cm["k"], cm["p"] + cm["k"])
u_inv = -dot(cm["p"] - cm["kprime"], cm["p"] - cm["kprime"])
t_inv = -dot(cm["p"] - cm["pprime"], cm["p"] - cm["pprime"])
spin_average = .5 * sum(abs(v)**2 for v in direct.values())
compare("massless_spin_average", spin_average,
        COUPLING**4 * (2 - u_inv/s_inv - s_inv/u_inv), retain=True)
zrot = {k: phi(p, PHASES[k]) for k, p in cm.items()}
direct_rot = direct_amplitudes(cm, zrot)
brackets_rot = bracket_amplitudes(zrot)
for helicities in direct_rot:
    compare("rephased_tree_" + helicities, brackets_rot[helicities],
            direct_rot[helicities], retain=True)
phase_delta = PHASES["pprime"] - PHASES["p"]
compare("external_phase_weight_plus", brackets_rot["++"],
        np.exp(1j*phase_delta) * brackets["++"], retain=True)
compare("external_phase_weight_minus", brackets_rot["--"],
        np.exp(-1j*phase_delta) * brackets["--"], retain=True)

status = all(x["pass"] for x in records) and wrong_epsilon_rejected
result = {
    "status": "pass" if status else "fail",
    "executed_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    "python_version": sys.version, "numpy_version": np.__version__,
    "platform": platform.platform(), "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "random_seed": None, "sampling": "Two specified finite configurations; no random draws.",
    "conventions": {"metric": "(-,+,+,+)", "gamma_anticommutator": "-2g",
        "gamma5": "diag(-1,-1,+1,+1)", "E_lower": [[0,-1],[1,0]],
        "phi": "sqrt(2omega)*(-sin(theta/2)exp(-i azimuth),cos(theta/2))",
        "brackets": "[pq]=(U phi_p)^T phi_q; <pq>=phi_p^dagger U phi_q^*; U=-E",
        "epsilon": "epsilon_upper0123=+1; contract lowered momenta"},
    "future_null_inputs": POINTS,
    "source_phase_phi_values": {k: packed(v) for k,v in zs.items()},
    "Schouten_three_terms": [packed(v) for v in schouten_terms],
    "four_bracket_product": packed(four_brackets), "epsilon_contraction_lowered": eps,
    "wrong_epsilon_control": {"wrong_value": packed(wrong_epsilon_value), "rejected": wrong_epsilon_rejected},
    "physical_massless_elastic_inputs": CM, "mandelstam": {"s":s_inv,"t":t_inv,"u":u_inv},
    "g": COUPLING, "independent_rephasing_angles_radians": PHASES,
    "tolerance": TOL, "comparisons":len(records),
    "maximum_normalized_error":max(x["normalized_error"] for x in records),
    "checks":records,
    "limitations":"Finite examples support the specified source-phase identities, epsilon sign and amplitude conversion. No old program rerun; no proof of general analytic crossing, global spinor phase section, collinear limits or loop/IR behavior.",
}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:result[k] for k in ["status","comparisons","maximum_normalized_error","four_bracket_product","epsilon_contraction_lowered"]}))
raise SystemExit(0 if status else 1)
