# General metric from Bianchi II automorphisms
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = symbols('alpha', cls=Function)
t, x, y, z = _coords
al = _funs
_metric = diag(1, exp(-2*al(t)), exp(al(t)), exp(al(t)))
del t, x, y, z, al
