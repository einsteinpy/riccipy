# Schwarzschild metric as the rho->0 limit of Tolman-Bondi dust
from sympy import Rational, diag, sin, symbols

coords = symbols("t r theta phi", real=True)
variables = symbols("M", constant=True)
functions = ()
t, r, th, ph = coords
M = variables
expr = M * (r - t) ** 2
metric = diag(
    -1,
    Rational(4, 9) * M / expr ** Rational(1, 3),
    expr ** Rational(2, 3),
    expr ** Rational(2, 3) * sin(th) ** 2,
)
del expr, t, r, th, ph, M
