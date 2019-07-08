"""
Minkowski space in null coordinates
"""
from sympy import Rational, sin, symbols, zeros

coords = symbols("u v theta phi", real=True)
variables = symbols("a b", constant=True)
functions = ()
u, v, th, ph = coords
a, b = variables
metric = zeros(4)
metric[2, 2] = (a * u - Rational(1, 2) * v / a + c) ** 2
metric[3, 3] = (a * u - Rational(1, 2) * v / a + c) ** 2 * sin(th) ** 2
metric[0, 1] = metric[1, 0] = -1
del u, v, th, ph, a, b
