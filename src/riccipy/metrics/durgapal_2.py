"""
Durgapal's static spherically symmetric perfect fluid with n=4
Durgapal, J. Phys. A, v15, p2637-2644, (1982)
"""
from sympy import Rational, sin, symbols, zeros

coords = symbols("t r theta phi", real=True)
variables = symbols("A C K", constant=True)
functions = ()
t, r, th, ph = coords
A, C, K = variables
metric = zeros(4)
metric[0, 0] = -A ** 2 * (1 + C * r ** 2) ** 4
metric[1, 1] = (
    7
    * (1 + C * r ** 2) ** 2
    * (1 + 5 * C * r ** 2) ** Rational(2, 5)
    / (
        (7 - 10 * C * r ** 2 - C ** 2 * r ** 4) * (1 + 5 * C * r ** 2) ** Rational(2, 5)
        + 7 * K * C * r ** 2
    )
)
metric[2, 2] = r ** 2
metric[3, 3] = r ** 2 * sin(th) ** 2
