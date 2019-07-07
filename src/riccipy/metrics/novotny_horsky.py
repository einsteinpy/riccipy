# Novotny and Horsky plane symmetric vacuum metric
from sympy import Rational, cos, diag, sin, symbols

coords = symbols("t x y z", real=True)
variables = symbols("a", constant=True)
functions = ()
t, x, y, z = coords
a = variables
metric = diag(
    -cos(z) / sin(z) ** Rational(2, 3),
    sin(z) ** Rational(4, 3),
    sin(z) ** Rational(4, 3),
    1 / a ** 2,
)
del t, x, y, z, a
