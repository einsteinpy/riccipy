# Static form of anti-de Sitter space
from sympy import cosh, diag, sin, sinh, symbols

coords = symbols("t r theta phi", real=True)
variables = ()
functions = ()
t, r, th, ph = coords
metric = diag(-cosh(r) ** 2, 1, sinh(r) ** 2, sinh(r) ** 2 * sin(th) ** 2)
del t, r, th, ph
