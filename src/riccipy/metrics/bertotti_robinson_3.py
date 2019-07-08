"""
The Bertotti-Robinson solution
Bertotti, Phys. Rev., v116, p1331, (1959)
Lovelock, Commun. Math. Phys., v5, p257, (1967)
Dolan, Commun. Math. Phys., v9, p161, (1968)
Stephani (10.19) p120
"""
from sympy import diag, sin, sinh, symbols

coords = symbols("t x theta phi", real=True)
variables = symbols("k", constant=True)
functions = ()
t, x, th, ph = coords
k = variables
metric = diag(-k ** 2 * sinh(x) ** 2, k ** 2, k ** 2, k ** 2 * sin(th) ** 2)
del t, x, th, ph, k
