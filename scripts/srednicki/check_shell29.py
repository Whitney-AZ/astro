"""Integrate the exact intersection of two sharp shells in sections 29.44--46.

The angular/radial domains are computed from both propagator momenta. The
finite-difference slopes are then compared with the derived boundary term.
This checks finite-shell integrals, not the existence of a continuum QFT.
"""
import json
import math
import warnings

import scipy
from scipy.integrate import IntegrationWarning, quad


def integrate(fun, a, b, points=None):
    return quad(fun, a, b, points=points, epsabs=2e-13,
                epsrel=2e-10, limit=150)[0]


def bubble(d, mass, a, b, q, strict):
    area = 2 * math.pi ** ((d - 1) / 2) / math.gamma((d - 1) / 2)

    def angular(z):
        lo, hi = a, b
        if strict:
            lo = max(a, -q*z + math.sqrt(a*a-q*q*(1-z*z)))
            hi = min(b, -q*z + math.sqrt(b*b-q*q*(1-z*z)))
        radial = integrate(
            lambda r: r**(d-1) / ((r*r+mass*mass)
                                  * (r*r+2*r*q*z+q*q+mass*mass)), lo, hi)
        return (1-z*z)**((d-3)/2) * radial

    # At these angles, the second shell starts excluding either boundary.
    cuts = [-q/(2*a), -q/(2*b)] if strict and q else None
    return area / (2*math.pi)**d * integrate(angular, -1, 1, cuts)


def cusp_coefficient(d, mass, a, b):
    hemisphere = (2*math.pi**((d-1)/2) / math.gamma((d-1)/2)) / (d-1)
    return -hemisphere / (2*math.pi)**d * sum(
        r**(d-1) / (r*r+mass*mass)**2 for r in (a, b))


rows = []
with warnings.catch_warnings():
    warnings.simplefilter('error', IntegrationWarning)
    for d, mass in ((4, 0.0), (4, 0.7), (6, 0.0)):
        a, b = 1.0, 3.0
        zero = bubble(d, mass, a, b, 0.0, True)
        predicted = cusp_coefficient(d, mass, a, b)
        samples = []
        for q in (0.03, 0.01, 0.003, 0.001, 0.0003, 0.0001):
            value = bubble(d, mass, a, b, q, True)
            slope = (value-zero)/q
            relative = abs(slope/predicted-1)
            samples.append({'q': q, 'bubble': value, 'slope': slope,
                            'relative_slope_error': relative})
        assert samples[-1]['relative_slope_error'] < 1e-4
        assert samples[-1]['relative_slope_error'] < samples[0]['relative_slope_error']
        rows.append({'dimension': d, 'mass': mass, 'inner': a, 'outer': b,
                     'bubble_at_zero': zero, 'boundary_slope': predicted,
                     'samples': samples})

    # In six dimensions the fixed-domain angular average has an analytic q^2
    # coefficient. This uses a different domain from the strict-shell checks.
    a, b = 1.0, 3.0
    zero = bubble(6, 0.0, a, b, 0.0, False)
    expected = -math.log(b/a)/(3*(4*math.pi)**3)
    fixed_domain = []
    for q in (0.1, 0.03, 0.01):
        coefficient = (bubble(6, 0.0, a, b, q, False)-zero)/(q*q)
        assert abs(coefficient/expected-1) < 2e-6
        fixed_domain.append({'q': q, 'q_squared_coefficient': coefficient})

print(json.dumps({'scipy': scipy.__version__, 'strict_shells': rows,
                  'fixed_domain_expected_q_squared': expected,
                  'fixed_domain_samples': fixed_domain,
                  'scope': 'Finite four- and six-dimensional bubble integrals; '
                           'no UV-limit or nonperturbative claim.',
                  'result': 'All assertions passed; integration warnings treated as errors.'},
                 indent=2))
