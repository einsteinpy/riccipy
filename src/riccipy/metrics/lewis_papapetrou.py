# Lewis Papapetrou metric
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = symbols('k r s w', cls=Function)
t, x, y, z = _coords
k, r, s, w = _funs
_metric = zeros(4)
_metric[0,0] = -exp(2*s(x,y))
_metric[3,3] = (exp(-s(x,y))*r(x,y)-w(x,y)*exp(s(x,y)))*(exp(-s(x,y))*r(x,y)+w(x,y)*exp(s(x,y)))
_metric[0,3] = _metric[3,0] = -w(x,y)*exp(2*s(x,y))
_metric[1,2] = _metric[2,1] = Rational(1,2)*exp(2*k(x,y)-2*s(x,y))
del t, x, y, z, k, r, s, w
