# Spatially flat Friedman-Robertson-Walker metric. Perfect fluid
from sympy import Function, diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = ()
functions = symbols("a", cls=Function)
t, r, th, ph = coords
a = functions
metric = diag(-1, a(t) ** 2, a(t) ** 2 * r ** 2, a(t) ** 2 * r ** 2 * sin(th) ** 2)
del t, r, th, ph, a
