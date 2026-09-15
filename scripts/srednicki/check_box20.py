#!/usr/bin/env python3
"""Quadrature of the two-parameter box integral, without its logarithmic reduction."""
import json
import math
from pathlib import Path


def nodes(n):
    result = []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(30):
            p, previous = 1.0, 0.0
            for k in range(1, n + 1):
                p, previous = ((2*k-1)*x*p-(k-1)*previous)/k, p
            derivative = n*(x*p-previous)/(x*x-1)
            change = p / derivative
            x -= change
            if abs(change) < 2e-15:
                break
        weight = 1 / ((1-x*x)*derivative*derivative)
        v = (x + 1) / 2
        # The sine substitution softens both endpoint corners.
        z = math.sin(math.pi*v/2)**2
        jacobian = math.pi*math.sin(math.pi*v)/2
        result.append((z, weight*jacobian))
    return result


def integral(a, b, grid):
    return 6*math.fsum(wz*wy/(a*z*y+b*(1-z)*(1-y))
                       for z, wz in grid for y, wy in grid)


rows = []
coarse, fine = nodes(128), nodes(256)
for a, b in ((1, 1), (0.1, 1), (1, 10), (0.01, 1), (3, 7), (100, 1)):
    low, high = integral(a, b, coarse), integral(a, b, fine)
    expected = 3*(math.pi**2+math.log(a/b)**2)/(a+b)
    error = abs(high/expected-1)
    assert error < 2e-7, (a, b, error)
    rows.append({'A':a, 'B':b, 'quadrature128':low, 'quadrature256':high,
                 'closed_form':expected, 'relative_error':error})

constant = (6*math.pi**2+math.pi*math.sqrt(3)-39)/11
amplitude_rows = []
for s, alpha in ((100, 0.001), (1000, 0.01), (1e6, 0.001)):
    values = [s, -s/2, -s/2]
    logs = [complex(math.log(s), -math.pi), complex(math.log(s/2)), complex(math.log(s/2))]
    # Assemble separately the propagator, the two vertex corrections, and box.
    total = 0j
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        exchange = -(1-alpha*(logs[i]-3)+alpha*(logs[i]+3-math.pi*math.sqrt(3))/12)/values[i]
        box = alpha*(math.pi**2+(logs[j]-logs[k])**2)/(2*values[i])
        total += exchange+box
    r90 = -11*(math.log(s)+constant)/4+11*math.log(2)/3-2*math.log(2)**2+2*math.pi**2
    expected = (3+alpha*r90+1j*math.pi*alpha*(4*math.log(2)-11/12))/s
    error = abs(total-expected)/abs(expected)
    assert error < 1e-12, (s, error)
    amplitude_rows.append({'s_over_m2':s, 'alpha':alpha, 'relative_error':error})

result = {'scope':'Euclidean massless box double integral and right-angle one-loop amplitude assembly',
          'passed':True, 'box_cases':rows, 'right_angle_cases':amplitude_rows}
Path('checks/srednicki/box20-check.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
