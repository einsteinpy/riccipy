# Spatially flat Friedman-Robertson-Walker metric. Perfect fluid
<<<<<<< HEAD
# Robertson, Astrophys. J., v82, p284, (1935)
# Robertson, Astrophys. J., v83, p137, (1936)
# Stephani (10.9) p118
from sympy import Function, diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = ()
functions = symbols("a", cls=Function)
t, r, th, ph = coords
a = functions
metric = diag(-1, a(t) ** 2, a(t) ** 2 * r ** 2, a(t) ** 2 * r ** 2 * sin(th) ** 2)
=======
_coords = symbols('t r theta phi', real=True)
_vars = ()
_funs = symbols('a', cls=Function)
t, r, th, ph = _coords
a = _funs
_metric = diag(-1, a(t)**2, a(t)**2*r**2, a(t)**2*r**2*sin(th)**2)
>>>>>>> added first metrics
del t, r, th, ph, a
