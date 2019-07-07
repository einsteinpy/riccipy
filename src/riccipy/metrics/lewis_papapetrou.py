# Lewis Papapetrou metric
from sympy import Function, Rational, exp, symbols, zeros

coords = symbols("t x y z", real=True)
variables = ()
functions = symbols("k r s w", cls=Function)
t, x, y, z = coords
k, r, s, w = functions
metric = zeros(4)
metric[0, 0] = -exp(2 * s(x, y))
metric[3, 3] = (exp(-s(x, y)) * r(x, y) - w(x, y) * exp(s(x, y))) * (
    exp(-s(x, y)) * r(x, y) + w(x, y) * exp(s(x, y))
)
metric[0, 3] = metric[3, 0] = -w(x, y) * exp(2 * s(x, y))
metric[1, 2] = metric[2, 1] = Rational(1, 2) * exp(2 * k(x, y) - 2 * s(x, y))
del t, x, y, z, k, r, s, w
