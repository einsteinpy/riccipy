# Ellis and MacCallum's G3VIo dust solution
from sympy import diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = ()
t, x, y, z = coords
metric = diag(-1, 16 * t ** 2, t * exp(-4 * x), t * exp(4 * x))
del t, x, y, z
