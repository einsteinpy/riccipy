# Levi-Civita solution, Class AIII
_coords = symbols('t z r phi', real=True)
_vars = ()
_funs = ()
t, z, r, ph = _coords
_metric = diag(-1/z, z, z**2, z**2*r**2)
del t, z, r, ph
