# Kasner power-law vacuum solution. Axisymmetric case
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = ()
t, x, y, z = _coords
_metric = diag(-1, t**Rational(4,3), t**Rational(4,3), t**Rational(-2,3))
del t, x, y, z
