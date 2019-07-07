# Tariq and Tupper metric admitting a G3VIo on S3
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = ()
t, x, y, z = _coords
_metric = diag(-1, 4*t**2/3, t/exp(2*x), t*exp(2*x))
del t, x, y, z
