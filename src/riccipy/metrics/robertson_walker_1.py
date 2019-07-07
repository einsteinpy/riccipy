# Closed Friedman-Robertson-Walker metric. Perfect fluid
_coords = symbols('t r theta phi', real=True)
_vars = ()
_funs = symbols('a', cls=Function)
t, r, th, ph = _coords
a = _funs
_metric = diag(-1, a(t)**2, a(t)**2*sin(r)**2, a(t)**2*sin(r)**2*sin(th)**2)
del t, r, th, ph, a
