# Bianchi I plane symmetric model
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = symbols('alpha beta', cls=Function)
t, x, y, z = _coords
al, be = _funs
_metric = diag(-1, exp(2*be(t)), exp(2*be(t)), exp(2*al(t)))
del t, x, y, z, al, be
