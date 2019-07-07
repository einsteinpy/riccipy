# Schwarzschild exterior metric in isotropic coordinates
from sympy import Rational, diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("M", constant=True)
functions = ()
t, r, th, ph = coords
M = variables
expr = (1 + Rational(1, 2) * M / r) ** 4
metric = diag(
    -(1 - Rational(1, 2) * M / r) ** 2 / (1 + Rational(1, 2) * M / r) ** 2,
    expr,
    expr * r ** 2,
    expr * r ** 2 * sin(th) ** 2,
)
del expr, t, r, th, ph, M
