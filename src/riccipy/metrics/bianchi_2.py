# General metric from Bianchi IV automorphisms
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = symbols('alpha beta gamma', cls=Function)
t, x, y, z = _coords
al, be, ga = _funs
_metric = diag(1, exp(al(t)), exp(be(t)), exp(ga(t)))
del t, x, y, z, al, be, ga
