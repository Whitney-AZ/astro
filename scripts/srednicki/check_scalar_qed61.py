import json,sys,numpy as np
m,E,c,e=1.0,2.0,1.0/3.0,-0.37
z=np.sqrt(E*E-m*m);sn=np.sqrt(1-c*c)
g=np.diag([-1.0,1.0,1.0,1.0])
p1=np.array([E,0,0,z]);p2=np.array([E,0,0,-z])
K1=np.array([E,E*sn,0,E*c]);K2=np.array([E,-E*sn,0,-E*c])
dot=lambda a,b:float(a@g@b)
r=m*m;s=-dot(p1+p2,p1+p2)
dt=dot(p1-K1,p1-K1)+r;du=dot(p1-K2,p1-K2)+r
p1l,p2l,K1l,K2l=[g@v for v in (p1,p2,K1,K2)]
A=e*e*(np.outer(2*p1l-K1l,K2l-2*p2l)/dt+np.outer(K1l-2*p2l,2*p1l-K2l)/du-2*g)
B=-e*e*(4*np.outer(p1l,p2l)/dt+4*np.outer(p2l,p1l)/du+2*g)
pol=np.array([[0,c,0,-sn],[0,0,1,0]])
physical_A=float(np.sum(np.abs(pol@A@pol.T)**2))
physical_B=float(np.sum(np.abs(pol@B@pol.T)**2))
contract=lambda T:float(np.einsum('mr,ns,mn,rs->',g,g,T,T))
x=r*s/(dt*du);pred=8*e**4*(1-2*x+2*x*x)
res={'python':sys.version.split()[0],'numpy':np.__version__,'input':{'m':m,'E':E,'cos_theta':c,'e':e},'invariants':{'s':s,'dt':dt,'du':du,'rho':x},'full_Ward_max':[float(np.max(np.abs(K1@A))),float(np.max(np.abs(A@K2)))],'reduced_Ward_max':[float(np.max(np.abs(K1@B))),float(np.max(np.abs(B@K2)))],'physical_full':physical_A,'physical_reduced':physical_B,'full_metric_square':contract(A),'reduced_metric_square':contract(B),'analytic_physical_square':pred,'spurious_difference':contract(B)-physical_A,'expected_spurious_difference':8*e**4,'amplitude_matrix':(pol@A@pol.T).tolist()}
assert np.max(np.abs(K1@A))<1e-13 and np.max(np.abs(A@K2))<1e-13
assert abs(physical_A-physical_B)<1e-13 and abs(physical_A-contract(A))<1e-13
assert abs(physical_A-pred)<1e-13 and abs(contract(B)-physical_A-8*e**4)<1e-13
print(json.dumps(res,indent=2))
