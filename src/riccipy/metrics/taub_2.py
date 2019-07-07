# Taub's plane symmetric vacuum solution
from sympy import diag, sqrt, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = ()
t, x, y, z = coords
metric = diag(-1 / sqrt(z), z, z, 1 / sqrt(z))
del t, x, y, z
