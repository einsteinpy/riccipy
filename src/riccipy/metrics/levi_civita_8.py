# Levi-Civita static vacuum solution
from sympy import diag, symbols

coords = symbols("t rho z phi", real=True)
variables = symbols("m", constant=True)
functions = ()
t, rh, z, ph = coords
m = variables
metric = diag(
    -rh ** (2 * m),
    rh ** (2 * (m ** 2 - m)),
    rh ** (2 * (m ** 2 - m)),
    rh ** (2 * (1 - m)),
)
del t, rh, z, ph, m
