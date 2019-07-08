# Kerr metric in Cartesian coordinates
# Allen, Gen. Rel. Grav., v26, p21, (1994)
from sympy import symbols, zeros

coords = symbols("t x y z", real=True)
variables = symbols("a M", constant=True)
functions = ()
t, x, y, z = coords
a, M = variables
expr = x ** 2 + a ** 2 * y ** 2
metric = zeros(4)
metric[0, 0] = -(a ** 2 * y ** 2 + x ** 2 - 2 * M * x) / expr
metric[1, 1] = expr / (x ** 2 - 2 * M * x + a ** 2)
metric[2, 2] = -expr / (y ** 2 - 1)
metric[3, 3] = (
    -(
        x ** 4
        + x ** 2 * a ** 2
        + 2 * a ** 2 * M * x
        + a ** 2 * y ** 2 * x ** 2
        - 2 * a * y ** 2 * M * x
        + a ** 4 * y ** 2
    )
    * (y ** 2 - 1)
    / expr
)
metric[0, 3] = metric[3, 0] = 2 * a * M * x * (y ** 2 - 1) / expr
del expr, t, x, y, z, a, M
