# Schwarzschild exterior metric in curvature coordinates
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("M", constant=True)
functions = ()
t, r, th, ph = coords
M = variables
metric = diag(-(1 - 2 * M / r), 1 / (1 - 2 * M / r), r ** 2, r ** 2 * sin(th) ** 2)
del t, r, th, ph, M
