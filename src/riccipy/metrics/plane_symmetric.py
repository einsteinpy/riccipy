# Bianchi I plane symmetric model
<<<<<<< HEAD
# Stephani (13.49) p162
from sympy import Function, diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = symbols("alpha beta", cls=Function)
t, x, y, z = coords
al, be = functions
metric = diag(-1, exp(2 * be(t)), exp(2 * be(t)), exp(2 * al(t)))
=======
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = symbols('alpha beta', cls=Function)
t, x, y, z = _coords
al, be = _funs
_metric = diag(-1, exp(2*be(t)), exp(2*be(t)), exp(2*al(t)))
>>>>>>> added first metrics
del t, x, y, z, al, be
