"""
Beckers, Sinzinkayo, and Demaret solution
Beckers et al., Phys. Rev. D, v30, p1846, (1984)
"""
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = symbols("k d m", constant=True)
functions = ()
t, x, y, z = coords
k, d, m = variables
expr = (k * x + d) ** (2 * m)
metric = diag(-expr, expr, expr, expr)
