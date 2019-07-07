# Vaidya metric in ingoing Eddington-Finkelstein coordinates
_coords = symbols('r v theta phi', real=True)
_vars = ()
_funs = symbols('M', cls=Function)
r, v, th, ph = _coords
M = _funs
_metric = diag(0, -(1-2*M(v)/r), r**2, r**2*sin(th)**2)
_metric[0,1] = _metric[1,0] = 1
del r, v, th, ph, M
