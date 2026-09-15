"""Four-point Lorentz/Dirac trees, independent color sums, and reference choices."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from itertools import product
import json
import numpy as np
from check_helicity60 import (dot,slash,endpoints,angle,square,polarization,
                             null_vector,direction,GAMMA)
from check_matrix80 import basis

ROOT=Path(__file__).resolve().parents[2]
records=[]

def check(name,actual,expected):
    actual,expected=np.asarray(actual),np.asarray(expected)
    residual=float(np.max(np.abs(actual-expected)))
    scale=max(1.,float(np.max(np.abs(actual))),float(np.max(np.abs(expected))))
    records.append(dict(name=name,residual=residual,scaled_residual=residual/scale,
                        passed=residual<2e-10*scale))

def current(p,q,r,e,f,gauge):
    if gauge=='GN':
        return dot(e,f)*p+f*dot(q,e)+e*dot(r,f)
    return dot(e,f)*(p-q)+f*dot(q-r,e)+e*dot(r-p,f)

def gluon_graphs(k,e,gauge='GN'):
    out=[]
    for a,b,c,d in [(0,1,2,3),(1,2,3,0)]:
        P=k[a]+k[b]
        left=current(k[a],k[b],-P,e[a],e[b],gauge)
        right=current(k[c],k[d],P,e[c],e[d],gauge)
        out.append((2 if gauge=='GN' else .5)*dot(left,right)/dot(P,P))
    contact=dot(e[0],e[2])*dot(e[1],e[3])
    if gauge=='F':
        contact-=.5*(dot(e[0],e[1])*dot(e[2],e[3])+dot(e[0],e[3])*dot(e[1],e[2]))
    return np.array(out+[contact])

def gluon_target(ep,h):
    neg=[i for i,v in enumerate(h) if v=='-']
    if len(neg)!=2:return 0j
    return angle(ep[neg[0]],ep[neg[1]])**4/np.prod([angle(ep[i],ep[(i+1)%4]) for i in range(4)])

def quark_graphs(k,h,refs):
    ep=list(map(endpoints,k))
    col=ep[0]['angle_ket' if h[0]=='-' else 'square_ket']
    row=ep[1]['square_bra' if h[1]=='+' else 'angle_bra']
    e,f=polarization(k[2],h[2],refs[0]),polarization(k[3],h[3],refs[1])
    s12=-dot(k[0]+k[1],k[0]+k[1]);s14=-dot(k[0]+k[3],k[0]+k[3])
    J=np.array([row@g@col for g in GAMMA])
    aq=-(row@slash(e)@slash(k[0]+k[3])@slash(f)@col)/(2*s14)
    ag=(dot(e,f)*dot(J,k[2])+dot(J,f)*dot(k[3],e)+dot(J,e)*dot(k[0]+k[1],f))/s12
    return np.array([aq,ag])

def quark_target(ep,h):
    if h[:2] not in ('-+','+-') or h[2]==h[3]:return 0j
    b=angle if h[:2]=='-+' else square
    leg=next(i for i in (2,3) if h[i]==('-' if h[:2]=='-+' else '+'))
    return b(ep[0],ep[leg])**3*b(ep[1],ep[leg])/np.prod([b(ep[i],ep[(i+1)%4]) for i in range(4)])

def main():
    orders=[(0,1,2,3),(0,2,3,1),(0,3,1,2),(0,1,3,2),(0,3,2,1),(0,2,1,3)]
    refs=[null_vector(1.,a,b) for a,b in [(1.05,2.),(2.2,-1.7),(.45,1.3),(1.9,.2)]]
    for point,(energy,theta,azimuth) in enumerate([(1.,1.,.4),(2.3,1.7,-.8),(5.,.6,1.1)],1):
        n=direction(.7,.2);v=direction(theta,azimuth)
        k=[np.r_[-energy,-energy*n],np.r_[-energy,energy*n],
           np.r_[energy,energy*v],np.r_[energy,-energy*v]]
        ep=list(map(endpoints,k));s,t,u=[-dot(k[0]+k[i],k[0]+k[i]).real for i in (1,2,3)]
        all_gluon=[];all_quark=[]
        for helicities in product('+-',repeat=4):
            h=''.join(helicities)
            e=[polarization(k[i],h[i],refs[i]) for i in range(4)]
            gn=sum(gluon_graphs(k,e));f=sum(gluon_graphs(k,e,'F'))
            target=gluon_target(ep,h)
            check(f'p{point}:g:{h}:GN',gn,target);check(f'p{point}:g:{h}:F',f,target)
            e_alt=[polarization(k[i],h[i],refs[(i+1)%4]) for i in range(4)]
            check(f'p{point}:g:{h}:reference',sum(gluon_graphs(k,e_alt)),gn)
            ward=e.copy();ward[0]=k[0]
            check(f'p{point}:g:{h}:Ward',sum(gluon_graphs(k,ward)),0)
            all_gluon.append([sum(gluon_graphs([k[i] for i in w],[e[i] for i in w])) for w in orders])
            targetq=quark_target(ep,h)
            q=quark_graphs(k,h,refs[2:])
            check(f'p{point}:q:{h}:generic',sum(q),targetq)
            mutual=quark_graphs(k,h,[k[3],k[2]])
            check(f'p{point}:q:{h}:mutual',sum(mutual),targetq)
            alternate=quark_graphs(k,h,[k[3],k[0]])
            check(f'p{point}:q:{h}:alternate',sum(alternate),targetq)
            if h in ('-++-','-+-+'):
                check(f'p{point}:q:{h}:mutual_gluon_zero',mutual[1],0)
                check(f'p{point}:q:{h}:alternate_quark_zero',alternate[0],0)
            perm=[0,1,3,2];hs=''.join(h[i] for i in perm)
            q2=sum(quark_graphs([k[i] for i in perm],hs,[refs[3],refs[2]]))
            all_quark.append([sum(q),q2])
        # The additional direct nonadjacent example has only the 23 graph.
        h='-+-+';special=[k[1],k[0],k[1],k[0]]
        e=[polarization(k[i],h[i],special[i]) for i in range(4)]
        graphs=gluon_graphs(k,e)
        check(f'p{point}:nonadjacent:12_and_contact',graphs[[0,2]],[0,0])
        check(f'p{point}:nonadjacent:23',graphs[1],gluon_target(ep,h))
        for N in (2,3):
            T=basis(N)[:-1];prodT=np.einsum('aij,bjk->abik',T,T)
            traces=np.einsum('abij,cdji->abcd',prodT,prodT)
            vectors=np.array([traces.transpose(np.argsort(w)).ravel() for w in orders])
            amps=np.array(all_gluon)@vectors
            direct_g=np.vdot(amps,amps).real/(4*(N*N-1)**2)
            expected_g=N*N/(N*N-1)*(s**4+t**4+u**4)*(1/s**2/t**2+1/t**2/u**2+1/u**2/s**2)
            check(f'p{point}:SU{N}:g_color_hel_average',direct_g,expected_g)
            chains=np.array([prodT.ravel(),prodT.transpose(1,0,2,3).ravel()])
            ampsq=np.array(all_quark)@chains
            direct_q=np.vdot(ampsq,ampsq).real/(4*N*N)
            expected_q=(N*N-1)**2/(2*N**3)*(t/u+u/t)-(N*N-1)/N*(t*t+u*u)/(s*s)
            check(f'p{point}:SU{N}:q_color_hel_average',direct_q,expected_q)
    paths=[Path(__file__),Path(__file__).with_name('check_helicity60.py'),
           Path(__file__).with_name('check_matrix80.py')]
    report=dict(task='S81 four-point tree amplitudes at three nondegenerate physical configurations',
                utc_time=datetime.now(timezone.utc).isoformat(),
                command='python3 scripts/srednicki/check_qcd81.py',
                scripts={p.name:sha256(p.read_bytes()).hexdigest() for p in paths},
                scope='Finite Lorentz and Dirac trees, explicit SU2/SU3 sums; not an all-order factorization proof',
                check_count=len(records),checks=records,all_passed=all(r['passed'] for r in records))
    (ROOT/'checks/srednicki/qcd81-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(check_count=len(records),failures=[r for r in records if not r['passed']],
                          max_scaled_residual=max(r['scaled_residual'] for r in records)),indent=2))
    raise SystemExit(not report['all_passed'])

if __name__=='__main__':main()
