"""
Metric with G4 on T3 and boost isotropy (flat case k=1)
Stephani (11.16) p128
"""
from sympy import Function, diag, symbols

coords = symbols("t x y w", real=True)
variables = ()
functions = symbols("alpha beta", cls=Function)
t, x, y, w = coords
al, be = functions
metric = diag(-be(w) ** 2 * sin(y) ** 2, al(w) ** 2, be(w) ** 2, 1)
