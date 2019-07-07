# Schwarzschild interior solution in curvature coordinates
_coords = symbols('t r theta phi', real=True)
_vars = symbols('A B R', constant=True)
_funs = ()
t, r, th, ph = _coords
A, B, R = _vars
_metric = diag(-(A-B*sqrt(1-r**2/R**2))**2, 1/(1-r**2/R**2), r**2, r**2*sin(th)**2)
del t, r, th, ph, A, B, R
