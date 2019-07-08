"""
Schwarzschild exterior metric in Israel coordinates
"""
from sympy import Rational, diag, sin, symbols

coords = symbols("u w theta phi", real=True)
variables = symbols("M", constant=True)
functions = ()
u, w, th, ph = coords
M = variables
expr = 2 * M + Rational(1, 4) * u * w / M
metric = diag(
    Rational(1, 2) * w ** 2 / (M * expr), 0, expr ** 2, expr ** 2 * sin(th) ** 2
)
metric[0, 1] = metric[1, 0] = 1
