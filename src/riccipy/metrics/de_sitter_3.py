"""
de Sitter space with a non-zero cosmological constant
"""
from sympy import diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("Lambda", constant=True)
functions = ()
t, r, th, ph = coords
La = variables
expr = 1 - La * r ** 2 / 3
metric = diag(-expr, 1 / expr, r ** 2, r ** 2 * sin(th) ** 2)
del expr, t, r, th, ph, La
