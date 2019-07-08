"""
de Sitter space
Hawking and Ellis p125
"""
from sympy import diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = symbols("alpha", constant=True)
functions = ()
t, x, y, z = coords
al = variables
expr = exp(2 * t / al)
metric = diag(-1, expr, expr, expr)
del expr, t, x, y, z, al
