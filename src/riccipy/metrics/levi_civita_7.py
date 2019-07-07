# Levi-Civita static vacuum solution. Special case m=2, Petrov D
_coords = symbols('t rho z phi', real=True)
_vars = ()
_funs = ()
t, rh, z, ph = _coords
_metric = diag(-rh**4, rh**4, rh**4, 1/rh**2)
del t, rh, z, ph
