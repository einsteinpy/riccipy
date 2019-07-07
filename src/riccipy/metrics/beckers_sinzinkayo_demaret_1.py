# Beckers, Sinzinkayo, and Demaret solution
_coords = symbols('t x y z', real=True)
_vars = symbols('k d m', constant=True)
_funs = ()
t, x, y, z = _coords
k, d, m = _vars
expr = (k*x+d)**(2*m)
_metric = diag(-expr, expr, expr, expr)
del expr, t, x, y, z, k, d, m
