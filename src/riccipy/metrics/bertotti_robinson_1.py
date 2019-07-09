"""
The Bertotti-Robinson solution
Bertotti, Phys. Rev., v116, p1331, (1959)
Bertotti, Commun. Math. Phys., v5, p257, (1967)
Robinson, Commun. Math. Phys., v9, p161, (1968)
Stephani (10.16) p120
"""
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = ()
t, x, y, z = coords
metric = diag(-(1 + z ** 2), 1 - y ** 2, 1 / (1 - y ** 2), 1 / (1 + z ** 2))
