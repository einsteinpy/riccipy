"""
Schwarzschild interior solution in curvature coordinates
"""
from sympy import diag, sin, sqrt, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("A B R", constant=True)
functions = ()
t, r, th, ph = coords
A, B, R = variables
metric = diag(
    -(A - B * sqrt(1 - r ** 2 / R ** 2)) ** 2,
    1 / (1 - r ** 2 / R ** 2),
    r ** 2,
    r ** 2 * sin(th) ** 2,
)
del t, r, th, ph, A, B, R
