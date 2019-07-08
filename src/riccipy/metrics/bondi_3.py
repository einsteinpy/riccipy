# The Bondi metric
# Bondi, Proc. Roy. Soc. Lond. A, v269, p21, (1962)
from sympy import Function, exp, sin, symbols, zeros

coords = symbols("r u theta phi", real=True)
variables = ()
functions = symbols("Q U V gamma", cls=Function)
r, u, th, ph = coords
Q, U, V, ga = functions
metric = zeros(4)
metric[1, 1] = (
    -exp(2 * Q(r, u, th) + 2 * ga(r, u, th))
    * (
        V(r, u, th) * exp(-2 * ga(r, u, th))
        - exp(-2 * Q(r, u, th)) * U(r, u, th) ** 2 * r ** 3
    )
    / r
)
metric[2, 2] = r ** 2 * exp(2 * ga(r, u, th))
metric[3, 3] = r ** 2 * exp(-2 * ga(r, u, th)) * sin(th) ** 2
metric[0, 1] = metric[1, 0] = -exp(2 * Q(r, u, th))
metric[1, 2] = metric[2, 1] = -U(r, u, th) * r ** 2 * exp(2 * ga(r, u, th))
del r, u, th, ph, Q, U, V, ga
