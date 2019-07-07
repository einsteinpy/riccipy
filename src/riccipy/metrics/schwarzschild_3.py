# Schwarzschild metric in ingoing Eddington-Finkelstein coordinates
from sympy import diag, sin, symbols

coords = symbols("r v theta phi", real=True)
variables = symbols("M", constant=True)
functions = ()
r, v, th, ph = coords
M = variables
metric = diag(0, -(1 - 2 * M / r), r ** 2, r ** 2 * sin(th) ** 2)
metric[0, 1] = metric[1, 0] = 1
del r, v, th, ph, M
