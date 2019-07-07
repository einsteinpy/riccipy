# Datta's Einstein-Maxwell solution
_coords = symbols('t x y z', real=True)
_vars = symbols('a b', constant=True)
_funs = ()
t, x, y, z = _coords
a, b = _vars
_metric = diag(-1/(b/t - a/t**2), b/t - a/t**2, t**2, t**2)
del t, x, y, z, a, b
