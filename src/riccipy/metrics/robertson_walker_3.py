# Closed Friedman-Robertson-Walker metric. Dust
from sympy import cos, diag, sin, symbols

coords = symbols("nu chi theta phi", real=True)
variables = symbols("A_0", constant=True)
functions = ()
nu, ch, th, ph = coords
A0 = variables
expr = A0 ** 2 * (1 - cos(nu)) ** 2
metric = diag(-expr, expr, expr * sin(ch) ** 2, expr * sin(ch) ** 2 * sin(th) ** 2)
del expr, nu, ch, th, ph, A0
