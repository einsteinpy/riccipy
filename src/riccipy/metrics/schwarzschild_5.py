"""
Schwarzschild exterior metric in Cartesian isotropic coordinates
"""
from sympy import Rational, diag, sqrt, symbols

coords = symbols("t x y z", real=True)
variables = symbols("M", constant=True)
functions = ()
t, x, y, z = coords
M = variables
expr1 = sqrt(x ** 2 + y ** 2 + z ** 2)
expr2 = (1 + Rational(1, 2) * M / expr1) ** 4
metric = diag(
    -(1 - Rational(1, 2) * M / expr1) ** 2 / (1 + Rational(1, 2) * M / expr1) ** 2,
    expr2,
    expr2,
    expr2,
)
