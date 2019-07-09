"""
Kasner power-law vacuum solution. Axisymmetric case
"""
from sympy import Rational, diag, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = ()
t, x, y, z = coords
metric = diag(-1, t ** Rational(4, 3), t ** Rational(4, 3), t ** Rational(-2, 3))
