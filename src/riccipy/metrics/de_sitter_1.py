# de Sitter space
_coords = symbols('t chi theta phi', real=True)
_vars = (symbols('alpha', constant=True),)
_funs = ()
t, ch, th, ph = _coords
al = _vars
expr = al**2*cosh(t/al)**2
_metric = diag(-1, expr, expr*sin(ch)**2, expr*sin(ch)**2*sin(th)**2)
del expr, t, ch, th, ph
