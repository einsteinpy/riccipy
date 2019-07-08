# Ellis and MacCallum's G3VIo dust solution
# Ellis et al., Commun. Math. Phys., v12, p108, (1969)
# Dunn et al., Astrophys. J., v204, p322, (1976)
# Evans, Mon. Not. R. Ast. Soc., v183, p727, (1978)
# Stephani (12.25) p150
from sympy import diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = ()
t, x, y, z = coords
metric = diag(-1, 16 * t ** 2, t * exp(-4 * x), t * exp(4 * x))
del t, x, y, z
