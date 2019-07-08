# McLenaghan Tariq Tupper metric
# McLenaghan, J. Math. Phys., v16, p11, (1975)
# Tupper, Gen. Rel. Grav., v7, p479, (1976)
# Stephani (10.21) p121
from sympy import diag, symbols

coords = symbols("t x y phi", real=True)
variables = symbols("a", constant=True)
functions = ()
t, x, y, ph = coords
metric = diag(-1, a ** 2 / x ** 2, a ** 2 / x ** 2, x ** 2 - 4 * y ** 2)
metric[0, 3] = metric[3, 0] = 2 * y
del t, x, y, ph
