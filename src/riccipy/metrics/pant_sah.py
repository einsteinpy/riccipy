"""
Pant and Sah charged static spherically symmetric solution
Pant et al., J. Math. Phys., v20, p2537-2539, (1979)
"""
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("A n", constant=True)
functions = ()
t, r, th, ph = coords
A, n = variables
metric = diag(-A * r ** (2 * n), n ** 2 + 1, r ** 2, r ** 2 * sin(th) ** 2)
del t, r, th, ph, A, n
