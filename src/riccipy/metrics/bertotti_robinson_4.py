# The Bertotti-Robinson solution
from sympy import cos, diag, symbols

coords = symbols("t z x y", real=True)
variables = symbols("omega", constant=True)
functions = ()
t, x, y, z = coords
om = variables
metric = diag(-1, 1, cos(om * x) ** 2, cos(om * t) ** 2)
del t, x, y, z, om
