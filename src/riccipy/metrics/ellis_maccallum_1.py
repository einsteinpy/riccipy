# Ellis and MacCallum's G3VIo dust solution
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = ()
t, x, y, z = _coords
_metric = diag(-1, 16*t**2, t*exp(-4*x), t*exp(4*x))
del t, x, y, z
