# Melvin's magnetic universe
_coords = symbols('t rho z phi', real=True)
_vars = symbols('B_0', constant=True)
_funs = ()
t, rh, z, ph = _coords
B0 = _vars
expr = (1+B0**2*rh**2/4)**2
_metric = diag(-expr, expr, expr, rh**2/expr)
del expr, t, rh, z, ph, B0
