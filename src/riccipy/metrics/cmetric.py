# The C-metric
_coords = symbols('t x y phi', real=True)
_vars = ()
_funs = symbols('f h', cls=Function)
t, x, y, ph = _coords
f, h = _funs
_metric = diag(-h(y)/(x+y)**2, 1/((x+y)**2*f(x)), 1/((x+y)**2*h(y)), f(x)/(x+y)**2)
del t, x, y, ph, f, h
