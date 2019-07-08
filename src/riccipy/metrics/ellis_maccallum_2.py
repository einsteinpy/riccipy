# Ellis and MacCallum Bianchi VIo vacuum solution
# Ellis et al., Commun. Math. Phys., v12, p108, (1969)
# Stephani (11.56) p136
from sympy import diag, exp, sqrt, symbols

coords = symbols("t x y z", real=True)
variables = symbols("n", constant=True)
functions = ()
t, x, y, z = coords
n = variables
metric = diag(
    -sqrt(t) * exp(n ** 2 * t ** 2),
    sqrt(t) * exp(n ** 2 * t ** 2),
    t * exp(2 * n * x),
    t * exp(-2 * n * x),
)
del t, x, y, z, n
