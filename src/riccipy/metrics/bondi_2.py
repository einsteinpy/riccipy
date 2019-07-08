# Spherical Bondi metric in advanced (ingoing) coordinates
# Bondi, Proc. Roy. Soc. Lond. A, v282, p303, (1964)
from sympy import Function, diag, sin, symbols

coords = symbols("r v theta phi", real=True)
variables = ()
functions = symbols("C M", cls=Function)
r, v, th, ph = coords
C, M = functions
metric = diag(0, -C(t, v) ** 2 * (1 - 2 * M(t, v) / t), t ** 2, t ** 2 * sin(th) ** 2)
metric[0, 1] = metric[1, 0] = -C(r, v)
del r, v, th, ph, C, M
