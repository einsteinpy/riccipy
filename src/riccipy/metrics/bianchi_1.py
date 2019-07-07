# General metric from Bianchi II automorphisms
from sympy import Function, diag, exp, symbols

coords = symbols("t x y z", real=True)
variables = ()
functions = symbols("alpha", cls=Function)
t, x, y, z = coords
al = functions
metric = diag(1, exp(-2 * al(t)), exp(al(t)), exp(al(t)))
del t, x, y, z, al
