# Harrison III-7(a) Petrov type D, Kinnersley class IV.B (C=1/2)
from sympy import diag, exp, symbols

coords = symbols("x_0:4", real=True)
variables = ()
functions = ()
x0, x1, x2, x3 = coords
metric = diag(
    -1 / (1 - x3 ** 2) ** 2,
    exp(4 * x0) ** 2 / (1 - x3 ** 2) ** 2,
    x3 ** 2,
    1 / (1 - x3 ** 2) ** 4,
)
del x0, x1, x2, x3
