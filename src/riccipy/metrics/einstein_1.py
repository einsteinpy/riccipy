"""
Einstein's static universe. Cartesian coordinates
Stephani (10.23a) p122
"""
from sympy import diag, sqrt, symbols

coords = symbols("t x y z", real=True)
variables = symbols("K", constant=True)
functions = ()
t, x, y, z = coords
K = variables
expr = 1 / (1 + sqrt(x ** 2 + y ** 2 + z ** 2) / (4 * K ** 2)) ** 2
metric = diag(-1, expr, expr, expr)
