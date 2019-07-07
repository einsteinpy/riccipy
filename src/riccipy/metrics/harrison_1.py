# Harrison III-12(b). Petrov type I
_coords = symbols('x_0:4', real=True)
_vars = symbols('a', constant=True)
_funs = ()
x0, x1, x2, x3 = _coords
a = _vars
expr = x1**2*cosh(x3)**Rational(3,2)
_metric = zeros(4)
_metric[0,0] = x0**Rational(3,2)*expr
_metric[1,1] = a**2*x0**3*x1*cosh(x3)**3
_metric[2,2] = 1/(x0*x1*cosh(x3))
_metric[3,3] = x0**Rational(7,2)*expr
del expr, x0, x1, x2, x3, a
