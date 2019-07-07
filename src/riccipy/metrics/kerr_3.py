# Kerr metric in outgoing Eddington Finkelstein form
_coords = symbols('u r theta phi', real=True)
_vars = symbols('a M', constant=True)
_funs = ()
u, r, th, ph = _coords
a, M = _vars
expr = r**2 + a**2*cos(th)**2
_metric = zeros(4)
_metric[0,0] = -(a**2-sin(th)**2*a**2+r**2-2*M*r)/expr
_metric[2,2] = expr
_metric[3,3] = sin(th)**2*(2*a**2*M*r*sin(th)**2+a**4-a**4*sin(th)**2+2*r**2*a**2-a**2*sin(th)**2*r**2+r**4)/expr
_metric[0,1] = _metric[1,0] = -1
_metric[0,3] = _metric[3,0] = -2*a*sin(th)**2*M*r/expr
_metric[1,3] = _metric[3,1] = a*sin(th)**2
del expr, u, r, th, ph, a, M
