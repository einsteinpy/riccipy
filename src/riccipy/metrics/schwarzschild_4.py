# Schwarzschild exterior metric in isotropic coordinates
_coords = symbols('t r theta phi', real=True)
_vars = symbols('M', constant=True)
_funs = ()
t, r, th, ph = _coords
M = _vars
expr = (1+Rational(1,2)*M/r)**4
_metric = diag(-(1-Rational(1,2)*M/r)**2/(1+Rational(1,2)*M/r)**2, expr, expr*r**2, expr*r**2*sin(th)**2)
del expr, t, r, th, ph, M
