# Kowalczynski and Plebanski metric
from sympy import diag, symbols

coords = symbols("t x y z", real=True)
variables = symbols("a b c d", constant=True)
functions = ()
t, x, y, z = coords
a, b, c, d = variables
expr1 = a * z ** 2 + b
expr2 = -2 * d ** 2 * x ** 2 + c * x - a
metric = diag(
    -2 * expr1 / x ** 2, 2 / (expr2 * x ** 4), 2 * expr2, 2 / (expr1 * x ** 2)
)
del t, x, y, z, a, b, c, d, expr1, expr2
