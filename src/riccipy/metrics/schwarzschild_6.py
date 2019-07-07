# Schwarzschild exterior metric  in Israel coordinates
_coords = symbols('u w theta phi', real=True)
_vars = symbols('M', constant=True)
_funs = ()
u, w, th, ph = _coords
M = _vars
expr = 2*M+Rational(1,4)*u*w/M
_metric = diag(Rational(1,2)*w**2/(M*expr), 0, expr**2, expr**2*sin(th)**2)
_metric[0,1] = _metric[1,0] = 1
del expr, u, w, th, ph, M
