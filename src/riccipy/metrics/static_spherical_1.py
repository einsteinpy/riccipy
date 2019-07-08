"""
General static, spherically symmetric metric in curvature coordinates
Stephani (14.1) p163
"""
from sympy import Function, diag, exp, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = ()
functions = symbolic("alpha beta", cls=Function)
t, r, th, ph = coords
al, be = functions
metric = diag(-exp(2 * al(r)), exp(2 * be(r)), r ** 2, r ** 2 * sin(th) ** 2)
del t, r, th, ph, al, be
