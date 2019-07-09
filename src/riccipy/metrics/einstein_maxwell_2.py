"""
Static cylindrically symmetric Einstein-Maxwell field (ii) longitudinal magnetic field (caused by an angular current)
Stephani (20.9b) p221
"""
from sympy import cosh, diag, log, symbols

coords = symbols("t rho z phi", real=True)
variables = symbols("a b m", constant=True)
functions = ()
t, rh, z, ph = coords
a, b, m = variables
expr1 = cosh(log(a * rh ** m)) ** 2
expr2 = rh ** (2 * m ** 2) * b ** 2 * expr1
metric = diag(-expr2, expr2, rh ** 2 * b ** 2 * expr1, 1 / (b ** 2 * expr1))
