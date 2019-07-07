# Schwarzschild exterior metric in curvature coordinates
_coords = symbols('t r theta phi', real=True)
_vars = symbols('M', constant=True)
_funs = ()
t, r, th, ph = _coords
M = _vars
_metric = diag(-(1-2*M/r), 1/(1-2*M/r), r**2, r**2*sin(th)**2)
del t, r, th, ph, M
