"""
Closed Friedman-Robertson-Walker metric. Dust
Landau-Lifshitz (112.4), (112.9), (112.10)
Stephani (12.3a) p122
Hawking and Ellis ch5.3
"""
from sympy import cos, diag, sin, symbols

coords = symbols("nu chi theta phi", real=True)
variables = symbols("A_0", constant=True)
functions = ()
nu, ch, th, ph = coords
A0 = variables
expr = A0 ** 2 * (1 - cos(nu)) ** 2
metric = diag(-expr, expr, expr * sin(ch) ** 2, expr * sin(ch) ** 2 * sin(th) ** 2)
