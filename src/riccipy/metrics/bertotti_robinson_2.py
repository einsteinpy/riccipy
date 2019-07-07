# The Bertotti-Robinson solution
from sympy import diag, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("q", constant=True)
functions = ()
t, r, th, ph = coords
q = variables
metric = diag(-q ** 2 / r ** 2, q ** 2 / r ** 2, q ** 2, q ** 2 * sin(th) ** 2)
del t, r, th, ph, q
