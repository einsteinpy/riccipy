# Levi-Civita solution, Class BII
_coords = symbols('t z r phi', real=True)
_vars = symbols('M', constant=True)
_funs = ()
t, z, r, ph = _coords
M = _vars
_metric = diag(-z**2*sinh(r)**2, 1/(2*M/z-1), z**2, 2*M/z-1)
del t, z, r, ph, M
