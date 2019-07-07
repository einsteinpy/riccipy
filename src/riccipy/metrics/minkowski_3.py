# Minkowski space in null coordinates
_coords = symbols('u v theta phi', real=True)
_vars = symbols('a b', constant=True)
_funs = ()
u, v, th, ph = _coords
a, b = _vars
_metric = zeros(4)
_metric[2,2] = (a*u-Rational(1,2)*v/a+c)**2
_metric[3,3] = (a*u-Rational(1,2)*v/a+c)**2*sin(th)**2
_metric[0,1] = _metric[1,0] = -1
del u, v, th, ph, a, b
