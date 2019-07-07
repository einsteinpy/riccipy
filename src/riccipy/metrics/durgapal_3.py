# Durgapal's static spherically symmetric perfect fluid with n=5
_coords = symbols('t r theta phi', real=True)
_vars = symbols('A C K', constant=True)
_funs = ()
t, r, th, ph = _coords
A, C, K = _vars
_metric = zeros(4)
_metric[0,0] = -A**2*(1+C*r**2)**5
_metric[1,1] = (1+C*r**2)**3/(1-C*r**2*(309+54*C*r**2+8*C**2*r**4)/112+K*C*r**2/(1+6*C*r**2)**Rational(1,3))
_metric[2,2] = r**2
_metric[3,3] = r**2*sin(th)**2
del t, r, th, ph, A, C, K
