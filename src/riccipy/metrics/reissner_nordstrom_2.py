# Reissner-Nordstrom spherically symmetric electro-vacuum solution with non-zero cosmological constant
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("M Q Lambda", constant=True)
functions = ()
t, r, th, ph = coords
M, Q, La = variables
expr = 1 - 2 * M / r + Q ** 2 / r ** 2 - La * r ** 2 / 3
metric = diag(-expr, 1 / expr, r ** 2, r ** 2 * sin(th) ** 2)
del expr, t, r, th, ph, M, Q
