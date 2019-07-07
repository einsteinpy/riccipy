# Einstein's static universe. Euclidean coordinates
_coords = symbols('t x y z', real=True)
_vars = symbols('K', constant=True)
_funs = ()
t, x, y, z = _coords
K = _vars
expr = 1/(1+sqrt(x**2+y**2+z**2)/(4*K**2))**2
_metric = diag(-1, expr, expr, expr)
del expr, t, x, y, z, K
