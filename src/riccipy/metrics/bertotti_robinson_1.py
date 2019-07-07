# The Bertotti-Robinson solution
_coords = symbols('t x y z')
_vars = ()
_funs = ()
t, x, y, z = _coords
_metric = diag(-(1+z**2), 1-y**2, 1/(1-y**2), 1/(1+z**2))
del t, x, y, z
