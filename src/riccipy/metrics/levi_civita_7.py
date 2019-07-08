"""
Levi-Civita static vacuum solution. Special case m=2, Petrov D
Stephani (20.8) p221
"""
from sympy import diag, symbols

coords = symbols("t rho z phi", real=True)
variables = ()
functions = ()
t, rh, z, ph = coords
metric = diag(-rh ** 4, rh ** 4, rh ** 4, 1 / rh ** 2)
