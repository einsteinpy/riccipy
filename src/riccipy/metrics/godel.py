# Godel metric
# Rev. Mod. Phys., v21, p447, (1949)
# Stephani (10.25) 122
from sympy import Rational, diag, exp, sqrt, symbols

coords = symbols("t x y z", real=True)
variables = symbols("omega", constant=True)
functions = ()
t, x, y, z = coords
om = variables
metric = diag(-1, 1, -Rational(1, 2) * exp(2 * sqrt(2) * om * x), 1)
metric[0, 2] = metric[2, 0] = -exp(sqrt(2) * om * x)
del t, x, y, z, om
