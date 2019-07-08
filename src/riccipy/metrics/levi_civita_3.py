# Levi-Civita solution, Class AIII
# Stephani (Table 16.2) p188
from sympy import diag, symbols

coords = symbols("t z r phi", real=True)
variables = ()
functions = ()
t, z, r, ph = coords
metric = diag(-1 / z, z, z ** 2, z ** 2 * r ** 2)
del t, z, r, ph
