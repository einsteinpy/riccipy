# Taub metric for plane symmetric, static perfect fluid.
_coords = symbols('t x y z', real=True)
_vars = symbols('mu', constant=True)
_funs = ()
t, x, y, z = _coords
mu = _vars
_metric = diag(-(z-3)**2, z**2, z**2, 3/(mu*z**2))
del t, x, y, z, mu
