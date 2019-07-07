# Harrison III-12(b). Petrov type I
from sympy import Rational, cosh, symbols, zeros

coords = symbols("x_0:4", real=True)
variables = symbols("a", constant=True)
functions = ()
x0, x1, x2, x3 = coords
a = variables
expr = x1 ** 2 * cosh(x3) ** Rational(3, 2)
metric = zeros(4)
metric[0, 0] = x0 ** Rational(3, 2) * expr
metric[1, 1] = a ** 2 * x0 ** 3 * x1 * cosh(x3) ** 3
metric[2, 2] = 1 / (x0 * x1 * cosh(x3))
metric[3, 3] = x0 ** Rational(7, 2) * expr
del expr, x0, x1, x2, x3, a
