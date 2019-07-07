# Harrison III-3 Petrov type D, Kinnersley class IV.B (C=0)
_coords = symbols('x_0:4', real=True)
_vars = ()
_funs = ()
x0, x1, x2, x3 = _coords
_metric = diag(-x1*sin(x3), 1/(sqrt(x1*sin(x3))), x1*sin(x3), x1**Rational(3,2)/sqrt(sin(x3)))
del x0, x1, x2, x3
