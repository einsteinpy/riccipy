# Dunn and Tupper's G3VI0 perfect fluid solution
_coords = symbols('t x y z', real=True)
_vars = (symbols('b', constant=True),)
_funs = ()
t, x, y, z = _coords
_metric = diag(-1, 4*t**2/(-b*(1 + b)), t**(-2*b)*exp(-4*x), t**(-2*b)*exp(4*x))
del t, x, y, z
