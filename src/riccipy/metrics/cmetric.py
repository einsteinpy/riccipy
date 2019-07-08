"""
The C-metric
Stephani (Table 16.2) p188
"""
from sympy import Function, diag, symbols

coords = symbols("t x y phi", real=True)
variables = ()
functions = symbols("f h", cls=Function)
t, x, y, ph = coords
f, h = functions
metric = diag(
    -h(y) / (x + y) ** 2,
    1 / ((x + y) ** 2 * f(x)),
    1 / ((x + y) ** 2 * h(y)),
    f(x) / (x + y) ** 2,
)
del t, x, y, ph, f, h
