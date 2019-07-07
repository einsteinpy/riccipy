# Levi-Civita solution, Class AII
_coords = symbols('t z r phi', real=True)
_vars = symbols('M', constant=True)
_funs = ()
t, z, r, ph = _coords
M = _vars
_metric = diag(-(2*M/z-1), 1/(2*M/z-1), z**2, z**2*sinh(r)**2)
del t, z, r, ph, M
