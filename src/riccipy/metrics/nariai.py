# Nariai vacuum metric
_coords = symbols('t x y z', real=True)
_vars = symbols('lambda', constant=True)
_funs = symbols('a b', cls=Function)
t, x, y, z = _coords
la = _vars
a, b = _funs
expr1 = x**2+y**2+z**2
expr2 = a(t)*cos(log(sqrt(expr1)/la)) + b(t)*sin(log(sqrt(expr1)/la))
_metric = diag(-expr2, la**2/expr1, la**2/expr1, la**2/expr1)
del expr1, expr2, t, x, y, z, la, a, b
