# Levi-Civita static vacuum solution
_coords = symbols('t rho z phi', real=True)
_vars = symbols('m', constant=True)
_funs = ()
t, rh, z, ph = _coords
m = _vars
_metric = diag(-rh**(2*m), rh**(2*(m**2-m)), rh**(2*(m**2-m)), rh**(2*(1-m)))
del t, rh, z, ph, m
