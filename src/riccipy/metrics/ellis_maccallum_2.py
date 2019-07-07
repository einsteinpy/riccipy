# Ellis and MacCallum Bianchi VIo vacuum solution
_coords = symbols('t x y z', real=True)
_vars = symbols('n', constant=True)
_funs = ()
t, x, y, z = _coords
n = _vars
_metric = diag(-sqrt(t)*exp(n**2*t**2), sqrt(t)*exp(n**2*t**2), t*exp(2*n*x), t*exp(-2*n*x))
del t, x, y, z, n
