# The Bertotti-Robinson solution
from sympy import diag, sin, sinh, symbols

coords = symbols("t x theta phi", real=True)
variables = symbols("k", constant=True)
functions = ()
t, x, th, ph = coords
k = variables
metric = diag(-k ** 2 * sinh(x) ** 2, k ** 2, k ** 2, k ** 2 * sin(th) ** 2)
del t, x, th, ph, k
