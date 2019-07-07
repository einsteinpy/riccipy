# Taub's plane symmetric vacuum solution
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = ()
t, x, y, z = _coords
_metric = diag(-1/sqrt(z), z, z, 1/sqrt(z))
del t, x, y, z
