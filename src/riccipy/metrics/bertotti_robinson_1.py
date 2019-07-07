# The Bertotti-Robinson solution
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = ()
t, x, y, z = coords
metric = diag(-(1 + z ** 2), 1 - y ** 2, 1 / (1 - y ** 2), 1 / (1 + z ** 2))
del t, x, y, z
