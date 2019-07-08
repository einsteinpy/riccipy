"""
Kerr metric in Boyer Lindquist coordinates
Boyer, J. Math. Phys., v8, p265, (1967)
Stephani (18.25) p205
"""
from sympy import cos, sin, symbols, zeros

coords = symbols("t r theta phi", real=True)
variables = symbols("a M", constant=True)
functions = ()
t, r, th, ph = coords
a, M = variables
expr = a ** 2 * cos(th) ** 2 + r ** 2
metric = zeros(4)
metric[0, 0] = -(a ** 2 - sin(th) ** 2 * a ** 2 + r ** 2 - 2 * M * r) / expr
metric[1, 1] = expr / (r ** 2 - 2 * M * r + a ** 2)
metric[2, 2] = expr
metric[3, 3] = (
    (
        -a ** 4 * sin(th) ** 2
        + a ** 4
        + 2 * r ** 2 * a ** 2
        - a ** 2 * sin(th) ** 2 * r ** 2
        + 2 * a ** 2 * sin(th) ** 2 * M * r
        + r ** 4
    )
    * sin(th) ** 2
    / expr
)
metric[0, 3] = metric[3, 0] = -2 * M * r * a * sin(th) ** 2 / expr
del expr, t, r, th, ph, a, M
