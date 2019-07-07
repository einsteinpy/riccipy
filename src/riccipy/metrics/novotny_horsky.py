# Novotny and Horsky plane symmetric vacuum metric
_coords = symbols('t x y z', real=True)
_vars = symbols('a', constant=True)
_funs = ()
t, x, y, z = _coords
a = _vars
_metric = diag(-cos(z)/sin(z)**Rational(2,3), sin(z)**Rational(4,3), sin(z)**Rational(4,3), 1/a**2)
del t, x, y, z, a
