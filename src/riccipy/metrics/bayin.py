# Bayin's spherically symmetric static perfect fluid solution II
from sympy import Rational, asin, sin, symbols, zeros

coords = symbols("t r theta phi", real=True)
variables = symbols("w_0 C_0 C_1", constant=True)
functions = ()
t, r, th, ph = coords
w0, C0, C1 = variables
metric = zeros(4)
metric[0, 0] = -C0 ** 2 * exp(
    -asin((-2 * r ** 2 + C1) / (C1 ** 2 + 4 * w0 ** 2) ** (Rational(1, 2)))
)
metric[1, 1] = w0 ** 2 / (-r ** 4 + C1 * r ** 2 + w0 ** 2)
metric[2, 2] = r ** 2
metric[3, 3] = r ** 2 * sin(th) ** 2
del t, r, th, ph, w0, C0, C1
