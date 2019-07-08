"""
de Sitter space
Hawking and Ellis p125
"""
from sympy import cosh, diag, sin, symbols

coords = symbols("t chi theta phi", real=True)
variables = symbols("alpha", constant=True)
functions = ()
t, ch, th, ph = coords
al = variables
expr = al ** 2 * cosh(t / al) ** 2
metric = diag(-1, expr, expr * sin(ch) ** 2, expr * sin(ch) ** 2 * sin(th) ** 2)
