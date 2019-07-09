"""
Levi-Civita solution, Class AI. Aka the exterior Schwarzschild metric.
Stephani (Table 16.2) p188
"""
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("M", constant=True)
functions = ()
t, r, th, ph = coords
M = variables
metric = diag(-(1 - 2 * M / r), 1 / (1 - 2 * M / r), r ** 2, r ** 2 * sin(th) ** 2)
