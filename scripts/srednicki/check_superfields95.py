"""Exterior-polynomial calculations retaining odd coefficients and matrix order."""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
rng = np.random.default_rng(950916)
I = np.eye(2, dtype=complex)
sigma = np.array([I, [[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
barsigma = sigma*np.array([1, -1, -1, -1])[:, None, None]
metric = np.array([-1, 1, 1, 1])
SL = np.array([[.25j*(sigma[i]@barsigma[j]-sigma[j]@barsigma[i])
                for j in range(4)] for i in range(4)])
epsilon = np.zeros((4,4,4,4))
for p in permutations(range(4)):
    epsilon[p] = (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))
zero = (0, 0, 0, 0)
records = []


def term(mask=0, k=zero, c=I):
    c = np.asarray(c, complex)
    if c.ndim == 0:
        c = c*I
    return {(mask, tuple(k)): c.copy()}


def add(*args):
    out = {}
    for p in args:
        for key, c in p.items():
            out[key] = out.get(key, np.zeros((2, 2), complex))+c
    return {key:c for key,c in out.items() if np.any(c != 0)}


def scale(p, a):
    return {key:a*c for key,c in p.items() if np.any(a*c != 0)}


def mul(p, q):
    out = {}
    for (mask, k), c in p.items():
        for (other, l), d in q.items():
            if mask & other:
                continue
            inv = sum((other & ((1 << j)-1)).bit_count()
                      for j in range(mask.bit_length()) if mask & (1 << j))
            key = (mask | other, tuple(a+b for a,b in zip(k,l)))
            out[key] = out.get(key, np.zeros((2, 2), complex))+(-1)**inv*(c@d)
    return {key:c for key,c in out.items() if np.any(c != 0)}


def product(*ps):
    out = term()
    for p in ps:
        out = mul(out, p)
    return out


def d(p, j):
    return {(mask ^ (1 << j), k):(-1)**((mask & ((1 << j)-1)).bit_count())*c
            for (mask,k),c in p.items() if mask & (1 << j)}


def dx(p, mu):
    return {key:1j*key[1][mu]*c for key,c in p.items() if key[1][mu] != 0}


def dagger(p):
    pairing = [2, 3, 0, 1, 6, 7, 4, 5, 10, 11, 8, 9]
    result = {}
    for (mask,k),c in p.items():
        mapped = [pairing[j] for j in reversed(range(12)) if mask & (1 << j)]
        inv = sum(mapped[i] > mapped[j] for i in range(len(mapped)) for j in range(i+1, len(mapped)))
        key = (sum(1 << j for j in mapped), tuple(-v for v in k))
        result = add(result, {key:(-1)**inv*c.conj().T})
    return result


theta = [term(1 << j) for j in range(2)]
bt = [term(1 << j) for j in range(2,4)]
tlower = [scale(theta[1], -1), theta[0]]
blower = [scale(bt[1], -1), bt[0]]
t = scale(mul(theta[0],theta[1]), -2)
tb = scale(mul(bt[0],bt[1]), 2)
B = [add(*(scale(mul(theta[a],bt[b]),sigma[mu,a,b])
           for a in range(2) for b in range(2))) for mu in range(4)]


def field(a, k, fermion=None):
    return term(0 if fermion is None else 1 << fermion, k, a)


def shift(p):  # f(x-i theta sigma bartheta), represented by Fourier modes
    out = {}
    for (mask,k),c in p.items():
        exponent = add(*(scale(B[mu],k[mu]) for mu in range(4)))
        exponential = add(term(),exponent,scale(mul(exponent,exponent),.5))
        out = add(out,mul(exponential,term(mask,k,c)))
    return out


def op(p, a, kind):
    if kind in ['Q','D']:
        sign = 1 if kind == 'Q' else -1
        return add(d(p,a),*(scale(mul(bt[b],dx(p,mu)),sign*1j*sigma[mu,a,b])
                            for mu in range(4) for b in range(2)))
    sign = -1 if kind == 'Qb' else 1
    return add(scale(d(p,a+2),-1),*(scale(mul(theta[b],dx(p,mu)),sign*1j*sigma[mu,b,a])
                                   for mu in range(4) for b in range(2)))


def Dc(p, a):
    return add(d(p,a),*(scale(mul(bt[b],dx(p,mu)),-2j*sigma[mu,a,b])
                       for mu in range(4) for b in range(2)))


def projection(p):
    return scale(d(d(p,3),2),2)


def top(p):
    return {(mask ^ 15,k):-c/4 for (mask,k),c in p.items() if mask & 15 == 15}


def norm(p):
    return max((float(np.max(abs(c))) for c in p.values()), default=0.)


def check(name, actual, expected, tol=5e-11):
    err = norm(add(actual,scale(expected,-1)))/max(1.,norm(expected))
    records.append(dict(name=name,scaled_residual=err,passed=err < tol))


for mu in range(4):
    for nu in range(4):
        check(f'theta-vector Fierz {mu,nu}',mul(B[mu],B[nu]),
              scale(mul(t,tb),-.5*metric[mu]*(mu == nu)))
check('left antitheta projection sign',projection(tb),term(c=-4))

for ki,k in enumerate([(1,2,-1,3),(-2,1,3,0)]):
    for mask in range(16):
        p = term(mask,k)
        for a in range(2):
            for b in range(2):
                check(f'Q algebra full exterior basis {ki,mask,a,b}',
                      add(op(op(p,b,'Qb'),a,'Q'),op(op(p,a,'Q'),b,'Qb')),
                      add(*(scale(dx(p,mu),-2j*sigma[mu,a,b]) for mu in range(4))))
                check(f'D algebra full exterior basis {ki,mask,a,b}',
                      add(op(op(p,b,'Db'),a,'D'),op(op(p,a,'D'),b,'Db')),
                      add(*(scale(dx(p,mu),2j*sigma[mu,a,b]) for mu in range(4))))
                check(f'Q-D mixed full exterior basis {ki,mask,a,b}',
                      add(op(op(p,b,'Db'),a,'Q'),op(op(p,a,'Q'),b,'Db')), {})

for sample in range(3):
    A = field(1.2+.3j, (1,-1,2,0))
    aux = field(.7-.2j,(-1,0,1,2))
    psi = [field(.4+.1j,(0,2,-1,1),8),field(-.3+.8j,(1,0,2,-1),9)]
    pd = [dagger(p) for p in psi]
    phi = add(shift(A),*(scale(mul(theta[a],shift(psi[a])),np.sqrt(2)) for a in range(2)),
              mul(t,shift(aux)))
    for a in range(2):
        check(f'chiral Fourier polynomial {sample,a}',op(phi,a,'Db'),{})
    free = add(product(dagger(aux),aux),
               *(scale(product(dx(dagger(A),mu),dx(A,mu)),-.5*metric[mu]) for mu in range(4)),
               *(scale(add(product(A,dx(dx(dagger(A),mu),mu)),
                            product(dagger(A),dx(dx(A,mu),mu))),.25*metric[mu]) for mu in range(4)),
               *(scale(add(product(pd[a],dx(psi[b],mu)),
                            scale(product(dx(pd[a],mu),psi[b]),-1)),.5j*barsigma[mu,a,b])
                 for mu in range(4) for a in range(2) for b in range(2)))
    check(f'complete kinetic D component {sample}',top(product(dagger(phi),phi)),free)
    # General noncommuting Hermitian gauge potentials with nonzero spacetime jets.
    vs = []
    for mu in range(4):
        mat = rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        wave = field(mat,(mu%2,1,-1,mu-1))
        vs.append(add(wave,dagger(wave)))
    lams = [field(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)),(1,2,0,-1),4+a)
            for a in range(2)]
    ld = [dagger(p) for p in lams]
    ldup = [ld[1],scale(ld[0],-1)]
    lamup = [lams[1],scale(lams[0],-1)]
    auxD = field(np.diag([.4,-.7]),zero)
    V2 = add(*(mul(B[mu],vs[mu]) for mu in range(4)))
    V3 = add(*(product(t,blower[a],ldup[a]) for a in range(2)),
             *(product(tb,theta[a],lams[a]) for a in range(2)))
    Vx = add(V2,V3,scale(product(t,tb,auxD),.5))
    g = .4+.1*sample
    Hx = add(term(),scale(Vx,-2*g),scale(mul(Vx,Vx),2*g*g))
    interaction = add(
        *(scale(add(product(dagger(A),vs[mu],dx(A,mu)),
                     scale(product(dx(dagger(A),mu),vs[mu],A),-1)),-1j*g*metric[mu]) for mu in range(4)),
        *(scale(product(dagger(A),vs[mu],vs[mu],A),-g*g*metric[mu]) for mu in range(4)),
        *(scale(product(pd[a],vs[mu],psi[b]),g*barsigma[mu,a,b])
          for mu in range(4) for a in range(2) for b in range(2)),
        *(scale(add(product(dagger(A),lamup[a],psi[a]),
                     product(pd[a],ldup[a],A)),np.sqrt(2)*g) for a in range(2)),
        scale(product(dagger(A),auxD,A),-g))
    check(f'full charged matter exponential D term {sample}',
          top(product(dagger(phi),Hx,phi)),add(free,interaction))
    # In y coordinates, the coordinate shift adds the divergence to V's top term.
    div = add(*(scale(dx(vs[mu],mu),metric[mu]) for mu in range(4)))
    V = add(Vx,scale(product(t,tb,div),-.5j))
    H = add(term(),scale(V,-2*g),scale(mul(V,V),2*g*g))
    Hi = add(term(),scale(V,2*g),scale(mul(V,V),2*g*g))
    check(f'full nilpotent gauge inverse {sample}',mul(Hi,H),term())
    Fs = [[add(dx(vs[nu],mu),scale(dx(vs[mu],nu),-1),
               scale(add(mul(vs[mu],vs[nu]),scale(mul(vs[nu],vs[mu]),-1)),-1j*g))
           for nu in range(4)] for mu in range(4)]
    calculated = []
    for a in range(2):
        computed = scale(projection(mul(Hi,Dc(H,a))),1/(8*g))
        calculated.append(computed)
        expected = add(lams[a],mul(tlower[a],auxD),
                       *(scale(mul(tlower[c],Fs[mu][nu]),-SL[mu,nu,a,c])
                         for mu in range(4) for nu in range(4) for c in range(2)),
                       *(scale(mul(t,add(dx(ldup[b],mu),
                            scale(add(mul(vs[mu],ldup[b]),scale(mul(ldup[b],vs[mu]),-1)),-1j*g))),
                               1j*sigma[mu,a,b]) for mu in range(4) for b in range(2)))
        check(f'full nonabelian projected field strength {sample,a}',computed,expected)
    Wsquare = add(mul(calculated[1],calculated[0]),scale(mul(calculated[0],calculated[1]),-1))
    Fcomponent = {(mask ^ 3,k):-c/2 for (mask,k),c in Wsquare.items() if mask & 3 == 3}
    expectedF = add(
        mul(auxD,auxD),
        *(scale(mul(Fs[mu][nu],Fs[mu][nu]),-.5*metric[mu]*metric[nu])
          for mu in range(4) for nu in range(4)),
        *(scale(mul(Fs[mu][nu],Fs[rho][tau]),.25j*epsilon[mu,nu,rho,tau])
          for mu,nu,rho,tau in permutations(range(4))),
        *(scale(mul(lamup[a],add(dx(ldup[b],mu),
                  scale(add(mul(vs[mu],ldup[b]),scale(mul(ldup[b],vs[mu]),-1)),-1j*g))),
                2j*sigma[mu,a,b]) for mu in range(4) for a in range(2) for b in range(2)))
    group_trace = lambda p: {key:np.trace(c)*I for key,c in p.items()}
    check(f'full projected W square gauge kinetic coefficient {sample}',
          group_trace(Fcomponent),group_trace(expectedF))

result = dict(checks=len(records),all_passed=all(r['passed'] for r in records),
              max_scaled_residual=max(r['scaled_residual'] for r in records),
              script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),records=records)
(ROOT/'checks/srednicki/superfields95-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'records'},indent=2))
if not result['all_passed']:
    print(json.dumps([r for r in records if not r['passed']],indent=2))
    raise SystemExit(1)
