"""
Buchdahl and Land's static spherically symmetric stiff perfect fluid with rhob=2
Tolman, Phys. Rev., v55, p363-373, (1939)
Buchdahl et al., J. Austr. Math. Soc., v8, p6-16, (1968)
Ibanez et al., J. Math. Phys., v23, p1363-1364, (1982)
Stephani (11.16) p128
"""
from sympy import Rational, diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = ()
functions = ()
t, r, th, ph = coords
metric = diag(
    -Rational(2, 3) * r ** 2,
    1 / (Rational(1, 2) - r ** 2 / 3),
    r ** 2,
    r ** 2 * sin(th) ** 2,
)
del t, r, th, ph
