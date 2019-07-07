# Harrison III-9(c) Petrov type D, Kinnersley class II.D (a=l=0)
from sympy import diag, exp, symbols

coords = symbols("x_0:4", real=True)
variables = ()
functions = ()
x0, x1, x2, x3 = coords
metric = diag(
    -x3 ** 2,
    exp(4 * x2) ** 2 / (1 + x3 ** 2) ** 2,
    1 / (1 + x3 ** 2) ** 2,
    1 / (1 + x3 ** 2) ** 4,
)
del x0, x1, x2, x3
