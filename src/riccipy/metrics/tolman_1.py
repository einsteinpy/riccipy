"""
Tolman's type IV solution
Tolman, Phys. Rev., v55, p363-373, (1939)
"""
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("A B R", constant=True)
functions = ()
t, r, th, ph = coords
A, B, R = variables
metric = diag(
    -B ** 2 * (1 + r ** 2 / A ** 2),
    (1 + 2 * r ** 2 / A ** 2) / ((1 + r ** 2 / A ** 2) * (1 - r ** 2 / R ** 2)),
    r ** 2,
    r ** 2 * sin(th) ** 2,
)
