"""
Harrison III-7(a) Petrov type D, Kinnersley class IV.B (C=1/2)
Harrison, Phys. Rev., v116, p1285, (1959)
d'Inverno et al., J. Math. Phys., v12, p1258, (1971)
"""
from sympy import diag, sinh, symbols

coords = symbols("x_0:4", real=True)
variables = ()
functions = ()
x0, x1, x2, x3 = coords
metric = diag(
    -1 / (1 - x3 ** 2) ** 2,
    sinh(2 * x0) ** 2 / (1 - x3 ** 2) ** 2,
    x3 ** 2,
    1 / (1 - x3 ** 2) ** 4,
)
