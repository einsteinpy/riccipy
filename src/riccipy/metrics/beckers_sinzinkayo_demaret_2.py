# Beckers, Sinzinkayo, and Demaret solution
_coords = symbols('t x y z', real=True)
_vars = symbols('m', constant=True)
_funs = ()
t, x, y, z = _coords
m = _vars
expr = x**(2*m)
_metric = diag(-expr, expr, expr, expr)
del expr, t, x, y, z, m
