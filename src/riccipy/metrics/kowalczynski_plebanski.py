# Kowalczynski and Plebanski metric
_coords = symbols('t x y z', real=True)
_vars = symbols('a b c d', constant=True)
_funs = ()
t, x, y, z = _coords
a, b, c, d = _vars
expr1 = a*z**2+b
expr2 = -2*d**2*x**2+c*x-a
_metric = diag(-2*expr1/x**2, 2/(expr2*x**4), 2*expr2, 2/(expr1*x**2))
del t, x, y, z, a, b, c, d, expr1, expr2
