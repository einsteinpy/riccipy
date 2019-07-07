# Schwarzschild metric in outgoing Eddington-Finkelstein coordinates
_coords = symbols('r u theta phi', real=True)
_vars = symbols('M', constant=True)
_funs = ()
r, u, th, ph = _coords
M = _vars
_metric = diag(0, -(1-2*M/r), r**2, r**2*sin(th)**2)
_metric[0,1] = _metric[1,0] = -1
del r, u, th, ph, M
