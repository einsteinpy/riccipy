# Faulkes' non-static spherically symmetric perfect fluid solution
_coords = symbols('t r theta phi', real=True)
_vars = symbols('k', constant=True)
_funs = symbols('E', cls=Function)
t, r, th, ph = _coords
k = _vars
E = _funs
expr = (E(t)-(r/(2*k)))**2
_metric = diag(-E(t)**2/expr, expr**2, expr**2*r**2, expr**2*r**2*sin(th)**2)
del expr, t, r, th, ph, k, E
