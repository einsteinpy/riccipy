# The Bertotti-Robinson solution
_coords = symbols('t r theta phi', real=True)
_vars = symbols('q', constant=True)
_funs = ()
t, r, th, ph = _coords
q = _vars
_metric = diag(-q**2/r**2, q**2/r**2, q**2, q**2*sin(th)**2)
del t, r, th, ph, q
