"""Direct matrix sums and ribbon contractions for section 80."""
from pathlib import Path
from itertools import permutations
from hashlib import sha256
from datetime import datetime, timezone
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]

def basis(n):
    out = []
    for i in range(n):
        for j in range(i+1,n):
            t=np.zeros((n,n),complex);t[i,j]=t[j,i]=1/np.sqrt(2);out.append(t)
            t=np.zeros((n,n),complex);t[i,j]=-1j/np.sqrt(2);t[j,i]=1j/np.sqrt(2);out.append(t)
    for k in range(1,n):
        t=np.diag([1]*k+[-k]+[0]*(n-k-1))/np.sqrt(k*(k+1))
        out.append(t)
    out.append(np.eye(n)/np.sqrt(n))
    return np.array(out)

def cycles(p):
    todo=set(range(len(p)));out=[]
    while todo:
        x=min(todo);c=[]
        while x in todo:
            c.append(x);todo.remove(x);x=p[x]
        out.append(c)
    return out

def pairings(items):
    if not items:
        yield []
    else:
        a=items[0]
        for j in range(1,len(items)):
            for rest in pairings(items[1:j]+items[j+1:]):
                yield [(a,items[j])]+rest

def main():
    records=[]
    orders=[(0,1,2,3),(0,2,3,1),(0,3,1,2),(0,1,3,2),(0,3,2,1),(0,2,1,3)]
    for n in range(1,5):
        t=basis(n)
        prod=np.einsum('aij,bjk->abik',t,t)
        traces=np.einsum('abij,cdji->abcd',prod,prod)
        vectors=np.array([traces.transpose(np.argsort(w)).ravel() for w in orders])
        gram=vectors@vectors.conj().T
        expected=(n**4-n**2)*np.eye(6)+n**2*np.ones((6,6))
        coefficients=np.array([2+1j,-3+2j,1-4j])
        weights=coefficients[[0,1,2,1,0,2]]
        amplitude=weights@vectors
        color_sum=np.vdot(amplitude,amplitude).real
        expected_sum=(2*n**4-2*n**2)*np.vdot(coefficients,coefficients).real+4*n**2*abs(sum(coefficients))**2
        restricted=traces[:-1,:-1,:-1,:-1]
        norm=np.vdot(restricted,restricted).real
        expected_norm=(n*n-1)*(n**4-3*n*n+3)/(n*n)
        # Recover all four-point component amplitudes directly from the
        # symmetrized vertices, independently of the trace decomposition.
        cubic=np.einsum('abij,cji->abc',prod,t)
        v3=cubic+cubic.transpose(0,2,1)
        v4=sum(traces.transpose(np.argsort(w)) for w in orders)
        denominators=[-20.,6.,14.]
        g2=2.;lam=.75
        component=(g2*np.einsum('abe,ecd->abcd',v3,v3)/denominators[0]
                   +g2*np.einsum('ace,ebd->abcd',v3,v3)/denominators[1]
                   +g2*np.einsum('ade,ebc->abcd',v3,v3)/denominators[2]-lam*v4)
        partial=[]
        channel={frozenset((0,1)):0,frozenset((2,3)):0,
                 frozenset((0,2)):1,frozenset((1,3)):1,
                 frozenset((0,3)):2,frozenset((1,2)):2}
        for w in orders:
            partial.append(g2/denominators[channel[frozenset(w[:2])]]
                           +g2/denominators[channel[frozenset((w[0],w[-1]))]]-lam)
        decomposed=(np.array(partial)@vectors).reshape(traces.shape)
        errors=dict(gram=float(np.max(np.abs(gram-expected))),
                    color_sum=float(abs(color_sum-expected_sum)),
                    traceless_norm=float(abs(norm-expected_norm)),
                    component_amplitude=float(np.max(np.abs(component-decomposed))))
        records.append(dict(N=n,color_assignments=n**8,gram_elements=36,
                            traceless_norm=float(norm),expected_traceless_norm=expected_norm,
                            residuals=errors,passed=max(errors.values())<1e-9))
    # A cyclic four-valent vertex with its four slots paired into two edges.
    # Face permutation is vertex successor after crossing the paired edge.
    sigma=[1,2,3,0];ribbons=[]
    for pairs in pairings(list(range(4))):
        alpha=[None]*4
        for a,b in pairs:alpha[a]=b;alpha[b]=a
        faces=cycles([sigma[alpha[i]] for i in range(4)])
        F=len(faces);chi=1-2+F;genus=(2-chi)//2
        ribbons.append(dict(pairs=pairs,faces=faces,V=1,E=2,F=F,
                            genus=genus,N_power=F-1,
                            passed=F-1==2-2*genus))
    report=dict(task="S80: full Hermitian matrix sums and quartic ribbon pairings",
                utc_time=datetime.now(timezone.utc).isoformat(),
                command="python3 scripts/srednicki/check_matrix80.py",
                script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                scope="N=1,2,3,4 explicit matrices; finite complex kinematic sample; three exact ribbon pairings",
                matrix_checks=records,ribbon_checks=ribbons,
                all_passed=all(r['passed'] for r in records+ribbons))
    (ROOT/'checks/srednicki/matrix80-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    raise SystemExit(not report['all_passed'])

if __name__=="__main__":main()
