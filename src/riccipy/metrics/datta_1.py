# Datta's Einstein-Maxwell solution
# Datta, Nuovo Cim., v36, p109
# Stephani (11.60) p137
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = symbols("a b", constant=True)
functions = ()
t, x, y, z = coords
a, b = variables
metric = diag(-1 / (b / t - a / t ** 2), b / t - a / t ** 2, t ** 2, t ** 2)
del t, x, y, z, a, b
