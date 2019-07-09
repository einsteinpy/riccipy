"""
Metric for spacetime with domain wall
"""
from sympy import diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = (symbols("k", constant=True),)
functions = ()
t, x, y, z = coords
k = variables
expr1 = (1 - k * z) ** 2
expr2 = exp(2 * k * t)
metric = diag(-expr1, expr1 * expr2, expr1 * expr2, 1)
