"""
Beckers, Sinzinkayo, and Demaret solution
Beckers et al., Phys. Rev. D, v30, p1846, (1984)
"""
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = symbols("m", constant=True)
functions = ()
t, x, y, z = coords
m = variables
expr = x ** (2 * m)
metric = diag(-expr, expr, expr, expr)
del expr, t, x, y, z, m
