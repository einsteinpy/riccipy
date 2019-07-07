# Levi-Civita solution, Class AII
from sympy import diag, sinh, symbols

coords = symbols("t z r phi", real=True)
variables = symbols("M", constant=True)
functions = ()
t, z, r, ph = coords
M = variables
metric = diag(-(2 * M / z - 1), 1 / (2 * M / z - 1), z ** 2, z ** 2 * sinh(r) ** 2)
del t, z, r, ph, M
