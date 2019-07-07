# LRS stiff perfect fluid cosmological solution with G4 on S3
_coords = symbols('t x y z', real=True)
_vars = symbols('k', constant=True)
_funs = ()
t, x, y, z = _coords
k = _vars
_metric = diag(-1, t**(2/k), t**(1-1/k), t**(1-1/k))
del t, x, y, z, k
