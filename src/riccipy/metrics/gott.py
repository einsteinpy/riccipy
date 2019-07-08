"""
Gott's interior solution for a cosmic string.
Gott, Astrophys. J., v288, p422-427, (1985)
"""
from sympy import diag, sin, symbols

coords = symbols("t r phi z", real=True)
variables = symbols("r_0", constant=True)
functions = ()
t, r, ph, z = coords
r0 = variables
metric = diag(-1, 1, r0 ** 2 * sin(r / r0) ** 2, 1)
