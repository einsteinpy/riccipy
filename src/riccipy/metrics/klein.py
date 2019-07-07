# Klein's static spherically symmetric radiation perfect fluid solution
_coords = symbols('t r theta phi', real=True)
_vars = symbols('p_0', constant=True)
_funs = ()
t, r, th, ph = _coords
p_0 = _vars
_metric = diag(-sqrt(7*p_0)*r, Rational(7,4), r**2, r**2*sin(th)**2)
del t, r, th, ph, p_0
