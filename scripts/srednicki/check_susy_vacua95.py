"""Full tree spectra on both O'Raifeartaigh branches and FI minima."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
rng = np.random.default_rng(950915)
records = []


def check(name, actual, expected, tol=1e-10):
    err = float(np.max(np.abs(np.asarray(actual)-expected)))
    scale = max(1., float(np.max(np.abs(expected))))
    records.append(dict(name=name, scaled_residual=err/scale, passed=err < tol*scale))


def ora_potential(z, m, k, v):
    a, b, c = z
    return k*k*abs(c*c-v*v)**2+m*m*abs(c)**2+abs(m*b+2*k*a*c)**2


def real_hessian(z, m, k, v, step):
    # x_i and y_i are canonically normalized real fields: delta z=(x+iy)/sqrt2.
    directions = np.concatenate([np.eye(3), 1j*np.eye(3)])/np.sqrt(2)
    fun = lambda dz: ora_potential(z+dz, m, k, v)
    hessian = np.zeros((6, 6))
    for i, ei in enumerate(directions):
        for j, ej in enumerate(directions):
            hessian[i, j] = (fun(step*(ei+ej))-fun(step*(ei-ej))
                             -fun(step*(-ei+ej))+fun(-step*(ei+ej)))/(4*step*step)
    return hessian


k, v = .8, 1.1
for ratio in [.55, 1., 1.6]:
    m = np.sqrt(2)*k*v*ratio
    cs = [np.sqrt(v*v-m*m/(2*k*k)), -np.sqrt(v*v-m*m/(2*k*k))] if ratio < 1 else [0.]
    for c in cs:
        for amplitude in [0., .5, 2.]:
            for phase in [0., 1.2]:
                a = amplitude*np.exp(1j*phase)
                b = -2*k*a*c/m
                z = np.array([a, b, c], complex)
                name = f'{ratio,c,amplitude,phase}'
                gradW = np.array([k*(c*c-v*v), m*c, m*b+2*k*a*c])
                W2 = np.array([[0., 0., 2*k*c], [0., 0., m], [2*k*c, m, 2*k*a]], complex)
                check('stationarity and goldstino '+name, W2@gradW.conj(), np.zeros(3))
                M = np.sqrt(m*m+4*k*k*c*c)
                h, B = 2*k*amplitude, 2*k*k*(v*v-c*c)
                fm = [(np.sqrt(h*h+4*M*M)-h)/2, (np.sqrt(h*h+4*M*M)+h)/2]
                check('full complex fermion singular values '+name,
                      np.sort(np.linalg.svd(W2, compute_uv=False)), np.array([0., *fm]))
                K = W2.conj().T@W2
                hol = np.zeros((3, 3), complex)
                hol[2, 2] = 2*k*gradW[0].conj()
                hol[0, 2] = hol[2, 0] = 2*k*gradW[2].conj()
                full = np.block([[K.real+hol.real, -K.imag-hol.imag],
                                 [K.imag-hol.imag, K.real-hol.real]])
                # Richardson removes all h^2 error exactly for this quartic potential.
                direct = (4*real_hessian(z, m, k, v, .015)
                          -real_hessian(z, m, k, v, .03))/3
                check('Hessian of original polynomial potential '+name, full, direct, 2e-9)
                masses = [0., 0.]
                for eta in [-1, 1]:
                    middle = M*M+(h*h+eta*B)/2
                    gap = np.sqrt((h*h+eta*B)**2+4*h*h*M*M)/2
                    masses.extend([middle-gap, middle+gap])
                check('all six scalar eigenvalues '+name, np.linalg.eigvalsh(full), np.sort(masses))
                gold = gradW.conj()/np.linalg.norm(gradW)
                flat = np.array([m, -2*k*c, 0.])/M
                check('goldstino equals flat complex direction '+name,
                      np.outer(gold, gold.conj()), np.outer(flat, flat))
                expectedE = k*k*v**4 if ratio >= 1 else m*m*v*v-m**4/(4*k*k)
                check('vacuum energy '+name, ora_potential(z, m, k, v), expectedE)

e, mass = .7, .9
threshold = mass*mass/e**2
for xi in [-2*threshold, -threshold, -.4*threshold, 0., .4*threshold, threshold, 2*threshold]:
    z = np.sign(xi)*max(abs(xi)-threshold, 0.)
    ap, am = np.sqrt(max(z, 0.)), np.sqrt(max(-z, 0.))
    D = e*(ap*ap-am*am-xi)
    Fs = -mass*np.array([am, ap])
    E = np.sum(abs(Fs)**2)+D*D/2
    expected = e*e*xi*xi/2 if abs(xi) <= threshold else mass*mass*abs(xi)-mass**4/(2*e*e)
    check(f'FI energy from all auxiliary fields xi={xi}', E, expected)
    check(f'FI scalar stationarity xi={xi}',
          [ap*(mass*mass+e*D), am*(mass*mass-e*D)], [0., 0.])
    samples = rng.random((100, 2))*(abs(xi)+threshold+1.)
    raw = mass*mass*samples.sum(axis=1)+e*e*(samples[:, 0]-samples[:, 1]-xi)**2/2
    check(f'FI full quadrant comparison xi={xi}', float(np.min(raw) >= E-1e-12), 1.)
for xi in [-2., 0., 1.3]:
    ap2, am2 = max(xi, 0.)+1.1, max(-xi, 0.)+1.1
    check(f'massless SQED FI exact zero xi={xi}', e*(ap2-am2-xi), 0.)

result = dict(checks=len(records), all_passed=all(r["passed"] for r in records),
              max_scaled_residual=max(r["scaled_residual"] for r in records),
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(), records=records)
(ROOT/"checks/srednicki/susy-vacua95-check.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k != "records"}, indent=2))
if not result["all_passed"]:
    print(json.dumps([r for r in records if not r["passed"]], indent=2))
    raise SystemExit(1)
