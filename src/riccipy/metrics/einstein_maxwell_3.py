# Static cylindrically symmetric Einstein-Maxwell field (iii) radial electric field (caused by an axial charge distribution)
from sympy import cosh, diag, log, symbols

coords = symbols("t phi rho z", real=True)
variables = symbols("a b m", constant=True)
functions = ()
t, ph, rh, z = coords
a, b, m = variables
expr1 = cosh(log(a * rh ** m)) ** 2
expr2 = rh ** (2 * m ** 2) * b ** 2 * expr1
metric = diag(-1 / (b ** 2 * expr1), rh ** 2 * b ** 2 * expr1, expr2, expr2)
del expr1, expr2, t, ph, rh, z, a, b, m
