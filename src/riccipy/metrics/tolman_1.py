# Tolman's type IV solution
_coords = symbols('t r theta phi', real=True)
_vars = symbols('A B R', constant=True)
_funs = ()
t, r, th, ph = _coords
A, B, R = _vars
_metric = diag(-B**2*(1+r**2/A**2), (1+2*r**2/A**2)/((1+r**2/A**2)*(1-r**2/R**2)), r**2, r**2*sin(th)**2)
del t, r, th, ph, A, B, R
