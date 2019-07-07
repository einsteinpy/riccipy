# Kasner power-law vacuum solution. Axisymmetric flat case
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = ()
t, x, y, z = _coords
_metric = diag(-1, t**2, 1, 1)
del t, x, y, z
