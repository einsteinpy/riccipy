"""
Nariai vacuum metric
Nariai, Sci. Rep. Tohoku Univ., v35, p62, (1951)
"""
from sympy import Function, cos, diag, log, sin, sqrt, symbols

coords = symbols("t x y z", real=True)
variables = symbols("lambda", constant=True)
functions = symbols("a b", cls=Function)
t, x, y, z = coords
la = variables
a, b = functions
expr1 = x ** 2 + y ** 2 + z ** 2
expr2 = a(t) * cos(log(sqrt(expr1) / la)) + b(t) * sin(log(sqrt(expr1) / la))
metric = diag(-expr2, la ** 2 / expr1, la ** 2 / expr1, la ** 2 / expr1)
del expr1, expr2, t, x, y, z, la, a, b
