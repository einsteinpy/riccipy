"""
Dunn and Tupper's G3VI0 perfect fluid solution
"""
from sympy import diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = symbols("b", constant=True)
functions = ()
t, x, y, z = coords
metric = diag(
    -1,
    4 * t ** 2 / (-b * (1 + b)),
    t ** (-2 * b) * exp(-4 * x),
    t ** (-2 * b) * exp(4 * x),
)
del t, x, y, z
