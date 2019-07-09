"""
General metric from Bianchi IV automorphisms
"""
from sympy import Function, diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = symbols("alpha beta gamma", cls=Function)
t, x, y, z = coords
al, be, ga = functions
metric = diag(1, exp(al(t)), exp(be(t)), exp(ga(t)))
