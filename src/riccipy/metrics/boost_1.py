# Metric with G4 on T3 and boost isotropy (flat case, k=0)
from sympy import Function, diag, symbols

coords = symbols("t x y w", real=True)
variables = ()
functions = symbols("alpha beta", cls=Function)
t, x, y, w = coords
al, be = functions
metric = diag(-be(w) ** 2 * y ** 2, al(w) ** 2, be(w) ** 2, 1)
del t, x, y, w, al, be
