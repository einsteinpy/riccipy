# Einstein's static universe. Polar coordinates
from sympy import diag, sin, symbols

coords = symbols("t chi theta phi", real=True)
variables = symbols("Lambda", constant=True)
functions = ()
t, ch, th, ph = coords
La = variables
metric = diag(-1 / La, 1 / La, sin(ch) ** 2 / La, sin(ch) ** 2 * sin(th) ** 2 / La)
del t, ch, th, ph, La
