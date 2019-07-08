# Koutras-McIntosh metric (no symmetries or invariants)
# Koutras et al., Class. Quantum Grav., v13, pL47, (1996)
from sympy import Function, symbols, zeros

coords = symbols("w u x y", real=True)
variables = symbols("a b", constant=True)
functions = symbols("f", cls=Function)
w, u, x, y = coords
a, b = variables
f = functions
metric = zeros(4)
metric[1, 1] = -(2 * f(u) * (a * x + b) * (x ** 2 + y ** 2) - a ** 2 * w ** 2)
metric[2, 2] = 1
metric[3, 3] = 1
metric[0, 1] = metric[1, 0] = -(a * x + b)
metric[1, 2] = metric[2, 1] = a * w
del w, u, x, y, a, b, f
