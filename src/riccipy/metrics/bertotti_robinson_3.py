# The Bertotti-Robinson solution
_coords = symbols('t x theta phi', real=True)
_vars = symbols('k', constant=True)
_funs = ()
t, x, th, ph = _coords
k = _vars
_metric = diag(-k**2*sinh(x)**2, k**2, k**2, k**2*sin(th)**2)
del t, x, th, ph, k
