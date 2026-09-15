"""Exact finite Grassmann integration versus source differentiation for section 43."""
from itertools import permutations
from pathlib import Path
import json
from fractions import Fraction

class Q:
    """Complex rational coefficient; no floating point arithmetic."""
    def __init__(self, real=0, imag=0):
        if isinstance(real, Q):
            self.real, self.imag = real.real, real.imag
        else:
            self.real, self.imag = Fraction(real), Fraction(imag)
    def __add__(self, other):
        other = Q(other)
        return Q(self.real+other.real, self.imag+other.imag)
    __radd__ = __add__
    def __neg__(self):
        return Q(-self.real, -self.imag)
    def __sub__(self, other):
        return self + -Q(other)
    def __rsub__(self, other):
        return Q(other) + -self
    def __mul__(self, other):
        other = Q(other)
        return Q(self.real*other.real-self.imag*other.imag,
                 self.real*other.imag+self.imag*other.real)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = Q(other)
        denominator = other.real**2 + other.imag**2
        return self * Q(other.real/denominator, -other.imag/denominator)
    def __rtruediv__(self, other):
        return Q(other) / self
    def __eq__(self, other):
        other = Q(other)
        return self.real == other.real and self.imag == other.imag
    def __str__(self):
        return str(self.real) if not self.imag else f'({self.real})+({self.imag})i'

I = Q(0, 1)

def tidy(a):
    return {m: Q(c) for m, c in a.items() if Q(c) != 0}

def add(*args):
    r = {}
    for a in args:
        for m, c in a.items():
            r[m] = r.get(m, 0) + c
    return tidy(r)

def scale(a, c):
    return tidy({m: c*v for m, v in a.items()})

def mul(a, b):
    r = {}
    for x, c in a.items():
        for y, d in b.items():
            if x & y:
                continue
            inversions = sum((y & ((1 << j)-1)).bit_count() for j in range(8) if x & (1 << j))
            r[x | y] = r.get(x | y, 0) + (-1)**inversions*c*d
    return tidy(r)

def gen(j):
    return {1 << j: Q(1)}

def exponential(q):
    result, term = {0: Q(1)}, {0: Q(1)}
    for n in range(1, 5):
        term = scale(mul(term, q), Fraction(1, n))
        result = add(result, term)
    assert not mul(term, q)
    return result

def derivative(p, j):
    return tidy({m ^ (1 << j): (-1)**((m & ((1 << j)-1)).bit_count())*c
                 for m, c in p.items() if m & (1 << j)})

def integrate(p):
    return {m >> 4: c for m, c in p.items() if m & 15 == 15}

D = [[2, 1], [3, 2]]
M = [[0, 2, 1, -1], [-2, 0, 3, 2], [-1, -3, 0, 4], [1, -2, -4, 0]]
results = []
for kind in ('Dirac', 'Majorana'):
    q0, source = {}, {}
    if kind == 'Dirac':
        for a in range(2):
            for b in range(2):
                q0 = add(q0, scale(mul(gen(a), gen(b+2)), -I*D[a][b]))
            source = add(source, scale(mul(gen(a+4), gen(a+2)), I),
                         scale(mul(gen(a), gen(a+6)), I))
        expected = {0:1, 5:2*I, 9:-I, 6:-3*I, 10:2*I, 15:1}
    else:
        for a in range(4):
            for b in range(4):
                q0 = add(q0, scale(mul(gen(a), gen(b)), -I*M[a][b]/2))
            source = add(source, scale(mul(gen(a+4), gen(a)), I))
        expected = {0:1, 3:4*I/3, 5:-2*I/3, 9:I, 6:-I/3, 10:-I/3, 12:2*I/3, 15:Fraction(-1,3)}
    e0 = exponential(q0)
    norm = integrate(e0)[0]
    z = scale(integrate(exponential(add(q0, source))), 1/norm)
    assert z == tidy(expected), (kind, z)
    checked = 0
    for n in range(5):
        for order in permutations(range(4), n):
            insertion = {0:Q(1)}
            for field in order:
                insertion = mul(insertion, gen(field))
            direct = Q(integrate(mul(insertion, e0)).get(0,0)/norm)
            differentiated = z
            for field in reversed(order):
                if kind == 'Dirac':
                    j, prefactor = (field+2, I) if field < 2 else (field-2, 1/I)
                else:
                    j, prefactor = field, 1/I
                differentiated = scale(derivative(differentiated, j), prefactor)
            from_source = differentiated.get(0,0)
            assert Q(direct-from_source) == 0, (kind, order, direct, from_source)
            checked += 1
    results.append({'case':kind, 'zero_source_integral':str(norm), 'source_polynomial_matches':True,
                    'ordered_insertions_checked':checked, 'arithmetic':'exact complex rational coefficients using Python fractions'})
report = {'passed':True, 'checks':results}
Path('checks/srednicki/fermion-gaussians43-check.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
