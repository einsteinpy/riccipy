"""
Griffiths' metric
Griffiths, Math. Proc. Camb. Phil. Soc., v77, p559, (1975)
"""
from sympy import Rational, symbols, zeros

coords = symbols("u v x y", real=True)
variables = symbols("a", constant=True)
functions = ()
u, v, x, y = coords
a = variables
metric = zeros(4)
metric[2, 2] = (
    Rational(3, 2)
    + 4 * a ** 2 * v * u
    + 6 * a ** 2 * v ** 2
    + 6 * a ** 2 * u ** 2
    + 4 * a ** 2 * y * u
    + 2 * a ** 2 * y ** 2
    + 4 * a ** 2 * v * y
)
metric[3, 3] = -Rational(1, 2)
metric[0, 1] = metric[1, 0] = -1
metric[0, 2] = metric[2, 0] = -a * (2 * v - y)
metric[0, 3] = metric[3, 0] = -1
metric[1, 2] = metric[2, 1] = -a * (2 * u - y)
metric[1, 3] = metric[3, 1] = -1
metric[2, 3] = metric[3, 2] = a * (v + u + 2 * y)
