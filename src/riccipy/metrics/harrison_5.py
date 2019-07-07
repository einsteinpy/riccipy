# Harrison III-7(a) Petrov type D, Kinnersley class IV.B (C=1/2)
_coords = symbols('x_0:4', real=True)
_vars = ()
_funs = ()
x0, x1, x2, x3 = _coords
_metric = diag(-1/(1-x3**2)**2, exp(4*x0)**2/(1-x3**2)**2, x3**2, 1/(1-x3**2)**4)
del x0, x1, x2, x3
