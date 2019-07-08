"""
Davidson's cylindrically symmetric radiation perfect fluid universe
Davidson, J. Math. Phys., v32, p1560, (1991)
"""
from sympy import Rational, diag, symbols

coords = symbols("t r z phi", real=True)
variables = ()
functions = ()
t, r, z, phi = coords
expr = (1 + r ** 2) ** Rational(2, 5)
metric = diag(
    -expr ** 3,
    t ** Rational(4, 3) * expr,
    t ** Rational(-2, 3) / expr,
    t ** Rational(4, 3) * r ** 2 / expr,
)
del expr, t, r, z, phi
