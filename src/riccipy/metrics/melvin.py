"""
Melvin's magnetic universe
Bonnor, Prog. Roy. Soc. Lond., vA67, p225, (1954)
Melvin, Phys. Lett., v8, p65, (1964)
Stephani (20.10) p222
"""
from sympy import diag, symbols

coords = symbols("t rho z phi", real=True)
variables = symbols("B_0", constant=True)
functions = ()
t, rh, z, ph = coords
B0 = variables
expr = (1 + B0 ** 2 * rh ** 2 / 4) ** 2
metric = diag(-expr, expr, expr, rh ** 2 / expr)
del expr, t, rh, z, ph, B0
