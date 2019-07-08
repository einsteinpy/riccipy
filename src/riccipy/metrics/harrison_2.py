"""
Harrison III-3 Petrov type D, Kinnersley class IV.B (C=0)
Harrison, Phys. Rev., v116, p1285, (1959)
d'Inverno et al., J. Math. Phys., v12, p1258, (1971)
"""
from sympy import Rational, diag, sin, sqrt, symbols

coords = symbols("x_0:4", real=True)
variables = ()
functions = ()
x0, x1, x2, x3 = coords
metric = diag(
    -x1 * sin(x3),
    1 / (sqrt(x1 * sin(x3))),
    x1 * sin(x3),
    x1 ** Rational(3, 2) / sqrt(sin(x3)),
)
