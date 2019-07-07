# Metric for spacetime with domain wall
_coords = symbols('t x y z', real=True)
_vars = (symbols('k', constant=True),)
_funs = ()
t, x, y, z = _coords
k = _vars
expr1 = (1 - k*z)**2
expr2 = exp(2*k*t)
_metric = diag(-expr1, expr1*expr2, expr1*expr2, 1)
del expr1, expr2, t, x, y, z, k
