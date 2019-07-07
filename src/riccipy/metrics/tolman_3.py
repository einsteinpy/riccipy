# Tolman's type VII static spherically symmetric perfect fluid solution
from sympy import Rational, diag, log, sin, sqrt, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("A B C R", constant=True)
functions = ()
t, r, th, ph = coords
A, B, C, R = variables
expr1 = 1 - r ** 2 / R ** 2 + 4 * r ** 4 / A ** 4
expr2 = sin(
    log(
        sqrt((sqrt(expr1) + 2 * r ** 2 / A ** 2 - Rational(1, 4) * A ** 2 / R ** 2) / C)
    )
)
metric = diag(-B ** 2 * expr2 ** 2, 1 / expr1, r ** 2, r ** 2 * sin(th) ** 2)
del expr1, expr2, t, r, th, ph, A, B, C, R
