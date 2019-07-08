# The Bertotti-Robinson solution
# Bertotti, Phys. Rev., v116, p1331, (1959)
# Lovelock, Commun. Math. Phys., v5, p257, (1967)
# Dolan, Commun. Math. Phys., v9, p161, (1968)
# Stephani (10.18) p121
from sympy import diag, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("q", constant=True)
functions = ()
t, r, th, ph = coords
q = variables
metric = diag(-q ** 2 / r ** 2, q ** 2 / r ** 2, q ** 2, q ** 2 * sin(th) ** 2)
del t, r, th, ph, q
