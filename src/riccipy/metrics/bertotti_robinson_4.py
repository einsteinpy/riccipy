# The Bertotti-Robinson solution
# Bertotti, Phys. Rev., v116, p1331, (1959)
# Lovelock, Commun. Math. Phys., v5, p257, (1967)
# Dolan, Commun. Math. Phys., v9, p161, (1968)
# Stephani (32.95) p372
from sympy import cos, diag, symbols

coords = symbols("t z x y", real=True)
variables = symbols("omega", constant=True)
functions = ()
t, x, y, z = coords
om = variables
metric = diag(-1, 1, cos(om * x) ** 2, cos(om * t) ** 2)
del t, x, y, z, om
