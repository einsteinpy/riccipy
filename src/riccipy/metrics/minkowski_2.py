# Minkowski space in polar coordinates
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = ()
functions = ()
t, r, th, ph = coords
metric = diag(-1, 1, r ** 2, r ** 2 * sin(th) ** 2)
del t, r, th, ph
