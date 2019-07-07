# Schwarzschild metric in outgoing Eddington-Finkelstein coordinates
from sympy import diag, sin, symbols

coords = symbols("r u theta phi", real=True)
variables = symbols("M", constant=True)
functions = ()
r, u, th, ph = coords
M = variables
metric = diag(0, -(1 - 2 * M / r), r ** 2, r ** 2 * sin(th) ** 2)
metric[0, 1] = metric[1, 0] = -1
del r, u, th, ph, M
