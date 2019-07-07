# Faulkes' non-static spherically symmetric perfect fluid solution
from sympy import Function, diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("k", constant=True)
functions = symbols("E", cls=Function)
t, r, th, ph = coords
k = variables
E = functions
expr = (E(t) - (r / (2 * k))) ** 2
metric = diag(
    -E(t) ** 2 / expr, expr ** 2, expr ** 2 * r ** 2, expr ** 2 * r ** 2 * sin(th) ** 2
)
del expr, t, r, th, ph, k, E
