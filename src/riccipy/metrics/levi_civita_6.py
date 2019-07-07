# Levi-Civita solution, Class BIII
_coords = symbols('t z r phi', real=True)
_vars = ()
_funs = ()
t, z, r, ph = _coords
_metric = diag(-r**2*z**2, z, z**2, 1/z)
del t, z, r, ph
