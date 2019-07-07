# Godel metric
_coords = symbols('t x y z', real=True)
_vars = (symbols('omega', constant=True),)
_funs = ()
t, x, y, z = _coords
om = _vars
_metric = diag(-1, 1, -Rational(1,2)*exp(2*sqrt(2)*om*x), 1)
_metric[0,2] = _metric[2,0] = -exp(sqrt(2)*om*x)
del t, x, y, z, om
