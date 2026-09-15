#!/usr/bin/env python3
"""Independent finite-matrix checks for the section 38 spinor conventions."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm

I = np.eye(2, dtype=complex)
Z = np.zeros((2, 2), dtype=complex)
pauli = [np.array(a, complex) for a in (
    [[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]
gamma = [np.block([[Z, I], [I, Z]])] + [np.block([[Z, s], [-s, Z]]) for s in pauli]
beta = gamma[0]
g5 = np.diag([-1, -1, 1, 1])
E = np.array([[0, -1], [1, 0]], complex)
C = np.block([[E, Z], [Z, -E]])
metric = np.array([-1, 1, 1, 1])
spin = [[1j * (a @ b - b @ a) / 4 for b in gamma] for a in gamma]

def slash(p):
    return sum(metric[i] * p[i] * gamma[i] for i in range(4))

def bars(x):
    return x.conj().T @ beta

def spinors(m, p):
    p = np.array(p, float)
    w = float(np.sqrt(p @ p + m*m))
    r, pm, pp = w+m, p[0]-1j*p[1], p[0]+1j*p[1]
    u = np.array([[r-p[2], -pm], [-pp, r+p[2]],
                  [r+p[2], pm], [pp, r-p[2]]], complex) / np.sqrt(2*r)
    v = np.array([[-pm, -r+p[2]], [r+p[2], pp],
                  [-pm, r+p[2]], [-r+p[2], pp]], complex) / np.sqrt(2*r)
    return np.r_[w, p], u, v

errors = {}
def check(label, actual, expected, tol=3e-12):
    actual, expected = np.asarray(actual), np.asarray(expected)
    scale = max(1.0, float(np.linalg.norm(actual)), float(np.linalg.norm(expected)))
    error = float(np.linalg.norm(actual-expected)) / scale
    errors[label] = max(errors.get(label, 0.0), error)
    assert error < tol, (label, error)

cases = [(1.3, [0, 0, 0]), (1.3, [.7, -.4, 1.1]),
         (.8, [-2.3, 1.7, -.6]), (.05, [3, -4, 2])]
for m, spatial in cases:
    p, u, v = spinors(m, spatial)
    _, un, vn = spinors(m, -np.array(spatial))
    _, u0, v0 = spinors(m, [0, 0, 0])
    k = float(np.linalg.norm(spatial))
    boost = np.eye(4) if k == 0 else expm(
        1j*np.arcsinh(k/m)*sum(spatial[i]*spin[i+1][0] for i in range(3))/k)
    check('explicit_u_vs_generator_exponential', u, boost @ u0)
    check('explicit_v_vs_generator_exponential', v, boost @ v0)
    check('u_mass_shell', (slash(p)+m*np.eye(4)) @ u, 0)
    check('v_mass_shell', (slash(p)-m*np.eye(4)) @ v, 0)
    check('u_scalar_norm', bars(u) @ u, 2*m*I)
    check('v_scalar_norm', bars(v) @ v, -2*m*I)
    check('same_momentum_scalar_cross', bars(u) @ v, 0)
    check('opposite_momentum_cross', u.conj().T @ vn, 0)
    check('u_spin_sum', u @ bars(u), -slash(p)+m*np.eye(4))
    check('v_spin_sum', v @ bars(v), -slash(p)-m*np.eye(4))
    check('charge_pairing', C @ bars(u).T, v)
    check('reverse_u', un, beta @ u)
    check('reverse_v', vn, -beta @ v)
    z = np.r_[p[3]/m, np.array([0., 0., 1.]) + p[3]*p[1:]/(m*(p[0]+m))]
    check('axis_norm', (metric*z) @ z, 1)
    check('axis_orthogonality', (metric*z) @ p, 0)
    for j, s in enumerate([1, -1]):
        projection = (np.eye(4)-s*g5 @ slash(z))/2
        check('polarized_u', np.outer(u[:, j], bars(u)[j]), projection @ (-slash(p)+m*np.eye(4)))
        check('polarized_v', np.outer(v[:, j], bars(v)[j]), projection @ (-slash(p)-m*np.eye(4)))
        check('gamma5_u_pair', g5 @ u[:, j], s*v[:, 1-j])
        check('time_reverse_u', un[:, 1-j].conj(), -s*C @ g5 @ u[:, j])
        check('time_reverse_v', vn[:, 1-j].conj(), -s*C @ g5 @ v[:, j])
    for mu in range(4):
        check('u_vector_norm', bars(u) @ gamma[mu] @ u, 2*p[mu]*I)
        check('v_vector_norm', bars(v) @ gamma[mu] @ v, 2*p[mu]*I)
    p2, u2, v2 = spinors(m, [.2, 1.3, -.9])
    for mu in range(4):
        G = (p2[mu]+p[mu])*np.eye(4)-2j*sum(spin[mu][nu]*metric[nu]*(p2[nu]-p[nu]) for nu in range(4))
        check('gordon_u_cross_momentum', 2*m*bars(u2) @ gamma[mu] @ u, bars(u2) @ G @ u)
        check('gordon_v_cross_momentum', -2*m*bars(v2) @ gamma[mu] @ v, bars(v2) @ G @ v)
        check('gordon_axial_u', bars(u2) @ G @ g5 @ u, 0)

p, u, v = spinors(0, [0, 0, 2])
for j, s in enumerate([1, -1]):
    check('massless_u_helicity', np.outer(u[:, j], bars(u)[j]), (np.eye(4)+s*g5) @ (-slash(p))/2)
    check('massless_v_helicity', np.outer(v[:, j], bars(v)[j]), (np.eye(4)-s*g5) @ (-slash(p))/2)

report = {'scope': 'Finite numerical matrix checks at four massive momenta and one nonzero massless axial momentum; not a replacement for the written proofs.',
          'massive_cases': [{'m': m, 'p': p} for m, p in cases],
          'max_scaled_errors': errors, 'pass': True}
Path('checks/srednicki/spinors38-check.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'pass': True, 'checks': len(errors), 'max_scaled_error': max(errors.values())}))
