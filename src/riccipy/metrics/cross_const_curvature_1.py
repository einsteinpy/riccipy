"""
Cross product of two 2-dimensional subspaces of constant curvature
Stephani (10.8) p118
"""
from sympy import diag, sin, symbols

coords = symbols("t x y z", real=True)
variables = symbols("A B", constant=True)
functions = ()
t, x, y, z = coords
A, B = variables
metric = diag(-B ** 2 * sin(z) ** 2, A ** 2, A ** 2 * sin(x) ** 2, B ** 2)
