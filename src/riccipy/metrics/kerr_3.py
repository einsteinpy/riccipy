"""
Kerr metric in outgoing Eddington Finkelstein form
"""
from sympy import cos, sin, symbols, zeros

coords = symbols("u r theta phi", real=True)
variables = symbols("a M", constant=True)
functions = ()
u, r, th, ph = coords
a, M = variables
expr = r ** 2 + a ** 2 * cos(th) ** 2
metric = zeros(4)
metric[0, 0] = -(a ** 2 - sin(th) ** 2 * a ** 2 + r ** 2 - 2 * M * r) / expr
metric[2, 2] = expr
metric[3, 3] = (
    sin(th) ** 2
    * (
        2 * a ** 2 * M * r * sin(th) ** 2
        + a ** 4
        - a ** 4 * sin(th) ** 2
        + 2 * r ** 2 * a ** 2
        - a ** 2 * sin(th) ** 2 * r ** 2
        + r ** 4
    )
    / expr
)
metric[0, 1] = metric[1, 0] = -1
metric[0, 3] = metric[3, 0] = -2 * a * sin(th) ** 2 * M * r / expr
metric[1, 3] = metric[3, 1] = a * sin(th) ** 2
del expr, u, r, th, ph, a, M
