"""
Durgapal's static spherically symmetric perfect fluid with n=3
Durgapal, J. Phys. A, v15, p2637-2644, (1982)
"""
from sympy import sin, sqrt, symbols, zeros

coords = symbols("t r theta phi", real=True)
variables = symbols("A C K", constant=True)
functions = ()
t, r, th, ph = coords
A, C, K = variables
metric = zeros(4)
metric[0, 0] = -A ** 2 * (1 + C * r ** 2) ** 3
metric[1, 1] = (
    2
    * (1 + C * r ** 2)
    * sqrt(1 + 4 * C * r ** 2)
    / ((2 - C * r ** 2) * sqrt(1 + 4 * C * r ** 2) + 2 * K * C * r ** 2)
)
metric[2, 2] = r ** 2
metric[3, 3] = r ** 2 * sin(th) ** 2
del t, r, th, ph, A, C, K
