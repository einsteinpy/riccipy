# LRS stiff perfect fluid cosmological solution with G4 on S3
# Stephani (12.11) p146
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = symbols("k", constant=True)
functions = ()
t, x, y, z = coords
k = variables
metric = diag(-1, t ** (2 / k), t ** (1 - 1 / k), t ** (1 - 1 / k))
del t, x, y, z, k
