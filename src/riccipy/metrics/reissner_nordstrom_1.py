# Reissner-Nordstrom spherically symmetric electro-vacuum solution
# Reissner, Ann. Phys., v50, p106, (1916)
# Stephani (13.21) p158
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("M Q", constant=True)
functions = ()
t, r, th, ph = coords
M, Q = variables
expr = 1 - 2 * M / r + Q ** 2 / r ** 2
metric = diag(-expr, 1 / expr, r ** 2, r ** 2 * sin(th) ** 2)
del expr, t, r, th, ph, M, Q
