# Tolman's type VI solution
# Tolman, Phys. Rev., v55, p363-373, (1939)
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("A B n", constant=True)
functions = ()
t, r, th, ph = coords
A, B, n = variables
metric = diag(
    -(A * r ** (1 - n) - B * r ** (1 + n)) ** 2,
    2 - n ** 2,
    r ** 2,
    r ** 2 * sin(th) ** 2,
)
del t, r, th, ph, A, B, n
