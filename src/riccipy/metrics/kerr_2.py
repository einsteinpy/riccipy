# Kerr metric in Boyer Lindquist coordinates
_coords = symbols('t r theta phi', real=True)
_vars = symbols('a M', constant=True)
_funs = ()
t, r, th, ph = _coords
a, M = _vars
expr = a**2*cos(th)**2+r**2
_metric = zeros(4)
_metric[0,0] = -(a**2-sin(th)**2*a**2+r**2-2*M*r)/expr
_metric[1,1] = expr/(r**2-2*M*r+a**2)
_metric[2,2] = expr
_metric[3,3] = (-a**4*sin(th)**2+a**4+2*r**2*a**2-a**2*sin(th)**2*r**2+2*a**2*sin(th)**2*M*r+r**4)*sin(th)**2/expr
_metric[0,3] = _metric[3,0] = -2*M*r*a*sin(th)**2/expr
del expr, t, r, th, ph, a, M
