# Minkowski space in polar coordinates
_coords = symbols('t r theta phi', real=True)
_vars = ()
_funs = ()
t, r, th, ph = _coords
_metric = diag(-1, 1, r**2, r**2*sin(th)**2)
del t, r, th, ph
