# Datta's Einstein-Maxwell solution
_coords = symbols('t x y z', real=True)
_vars = symbols('C_1 C_2 mu', constant=True)
_funs = ()
t, x, y, z = _coords
C_1, C_2, mu = _vars
expr = (C_1*t**mu + C_2/t**mu)**2
_metric = diag(-expr*t**(2*mu**2), 1/expr, expr*t**(2*mu**2), t**2*expr)
del expr, t, x, y, z, C_1, C_2, mu
