"""
Kasner power-law vacuum solution. Axisymmetric flat case
"""
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = ()
t, x, y, z = coords
metric = diag(-1, t ** 2, 1, 1)
del t, x, y, z
