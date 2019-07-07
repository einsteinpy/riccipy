# Levi-Civita solution, Class BIII
from sympy import diag, symbols

coords = symbols("t z r phi", real=True)
variables = ()
functions = ()
t, z, r, ph = coords
metric = diag(-r ** 2 * z ** 2, z, z ** 2, 1 / z)
del t, z, r, ph
