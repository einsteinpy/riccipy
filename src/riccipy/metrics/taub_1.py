# Taub metric for plane symmetric, static perfect fluid.
# Taub, Phys. Rev., v103, p454, (1956)
# Stephani (13.44) p161
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = symbols("mu", constant=True)
functions = ()
t, x, y, z = coords
mu = variables
metric = diag(-(z - 3) ** 2, z ** 2, z ** 2, 3 / (mu * z ** 2))
del t, x, y, z, mu
