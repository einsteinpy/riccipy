"""
Closed Friedman-Robertson-Walker metric. Perfect fluid
Robertson, Astrophys. J., v82, p284, (1935)
Robertson, Astrophys. J., v83, p137, (1936)
Stephani (10.9) p118
"""
from sympy import Function, diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = ()
functions = symbols("a", cls=Function)
t, r, th, ph = coords
a = functions
metric = diag(
    -1, a(t) ** 2, a(t) ** 2 * sin(r) ** 2, a(t) ** 2 * sin(r) ** 2 * sin(th) ** 2
)
