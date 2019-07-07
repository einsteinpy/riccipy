# Spherical Bondi metric in advanced (ingoing) coordinates
_coords = symbols('r v theta phi', real=True)
_vars = ()
_funs = symbols('C M', cls=Function)
r, v, th, ph = _coords
C, M = _funs
_metric = diag(0,-C(r,v)**2*(1-2*M(r,v)/r),r**2,r**2*sin(th)**2)
_metric[0,1] = _metric[1,0] = C(r,v)
del r, v, th, ph, C, M
