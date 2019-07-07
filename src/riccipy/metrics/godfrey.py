# A vacuum metric admitting a nontrivial homothety which is non-null, not hypersurface-orthogonal, and whose homothetic bivector is null
_coords = symbols('t r z phi', real=True)
_vars = symbols('a C')
_funs = ()
t, r, z, ph = _coords
a, C = _vars
expr = r**(2*a*(a-1))*exp(2*(2*a*z-z-r**2/2+C))
_metric = diag(-r**(2*a)*exp(2*z), expr, expr, r**(2*(1-a))/exp(2*z))
del expr, t, r, z, ph, a, C
