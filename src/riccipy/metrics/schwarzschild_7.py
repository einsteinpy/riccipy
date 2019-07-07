# Schwarzschild metric as the rho->0 limit of Tolman-Bondi dust
_coords = symbols('t r theta phi', real=True)
_vars = symbols('M', constant=True)
_funs = ()
t, r, th, ph = _coords
M = _vars
expr = M*(r-t)**2
_metric = diag(-1, Rational(4,9)*M/expr**Rational(1,3), expr**Rational(2,3), expr**Rational(2,3)*sin(th)**2)
del expr, t, r, th, ph, M
