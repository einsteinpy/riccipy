# Reissner-Nordstrom spherically symmetric electro-vacuum solution with non-zero cosmological constant
_coords = symbols('t r theta phi', real=True)
_vars = symbols('M Q Lambda', constant=True)
_funs = ()
t, r, th, ph = _coords
M, Q, La = _vars
expr = 1-2*M/r+Q**2/r**2-La*r**2/3
_metric = diag(-expr, 1/expr, r**2, r**2*sin(th)**2)
del expr, t, r, th, ph, M, Q
