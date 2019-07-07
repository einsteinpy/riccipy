# Closed Friedman-Robertson-Walker metric. Dust
_coords = symbols('nu chi theta phi', real=True)
_vars = symbols('A_0', constant=True)
_funs = ()
nu, ch, th, ph = _coords
A0 = _vars
expr = A0**2*(1-cos(nu))**2
_metric = diag(-expr, expr, expr*sin(ch)**2, expr*sin(ch)**2*sin(th)**2)
del expr, nu, ch, th, ph, A0
