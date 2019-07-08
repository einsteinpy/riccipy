# Heintzmann's static spherically symmetric perfect fluid solution
# Heintzmann, Z. Phys., v228, p489-493, (1969)
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("A a K", constant=True)
functions = ()
t, r, th, ph = coords
A, a, K = variables
metric = diag(
    -A ** 2 * (1 + a * r ** 2) ** 3, (1 + a * r ** 2) / K, r ** 2, r ** 2 * sin(th) ** 2
)
del t, r, th, ph, A, a, K
