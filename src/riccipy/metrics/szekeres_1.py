# Szekeres solution for a special stiff perfect fluid
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = ()
t, x, y, z = _coords
_metric = diag(-x**6, x**4*cos(2*t)**2, x**2/cos(2*t), x**2/cos(2*t))
del t, x, y, z
