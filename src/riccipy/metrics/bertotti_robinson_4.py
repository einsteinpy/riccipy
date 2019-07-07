# The Bertotti-Robinson solution
_coords = symbols('t z x y', real=True)
_vars = symbols('omega', constant=True)
_funs = ()
t, x, y, z = _coords
om = _vars
_metric = diag(-1, 1, cos(om*x)**2, cos(om*t)**2)
del t, x, y, z, om
