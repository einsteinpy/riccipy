"""
Bianchi I plane symmetric model
Stephani (13.49) p162
"""
from sympy import Function, diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = symbols("alpha beta", cls=Function)
t, x, y, z = coords
al, be = functions
metric = diag(-1, exp(2 * be(t)), exp(2 * be(t)), exp(2 * al(t)))
