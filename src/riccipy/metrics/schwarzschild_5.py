# Schwarzschild exterior metric in Cartesian isotropic coordinates
_coords = symbols('t x y z', real=True)
_vars = symbols('M', constant=True)
_funs = ()
t, x, y, z = _coords
M = _vars
expr1 = sqrt(x**2+y**2+z**2)
expr2 = (1+Rational(1,2)*M/expr1)**4
_metric = diag(-(1-Rational(1,2)*M/expr1)**2/(1+Rational(1,2)*M/expr1)**2, expr2, expr2, expr2)
del expr1, expr2, t, x, y, z, M
