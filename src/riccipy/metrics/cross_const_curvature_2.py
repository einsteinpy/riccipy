# Cross product of two 2-dimensional subspaces of constant curvature
_coords = symbols('t x y z', real=True)
_vars = symbols('A B', constant=True)
_funs = ()
t, x, y, z = _coords
A, B = _vars
_metric = diag(-B**2*sin(z)**2, A**2, A**2*sinh(x)**2, B**2)
del t, x, y, z, A, B
