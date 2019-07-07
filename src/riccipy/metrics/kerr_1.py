# Kerr metric in Cartesian coordinates
_coords = symbols('t x y z', real=True)
_vars = symbols('a M', constant=True)
_funs = ()
expr = _coords[1]**2+_vars[0]**2*_coords[2]**2
t, x, y, z = _coords
a, M = _vars
_metric = zeros(4)
_metric[0,0] = -(a**2*y**2+x**2-2*M*x)/expr
_metric[1,1] = expr/(x**2-2*M*x+a**2)
_metric[2,2] = -expr/(y**2-1)
_metric[3,3] = -(x**4+x**2*a**2+2*a**2*M*x+a**2*y**2*x**2-2*a*y**2*M*x+a**4*y**2)*(y**2-1)/expr
_metric[0,3] = _metric[3,0] = 2*a*M*x*(y**2-1)/expr
del expr, t, x, y, z, a, M
