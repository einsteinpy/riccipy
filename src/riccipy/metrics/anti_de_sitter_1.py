# anti-de Sitter space
_coords = symbols('t chi theta phi', real=True)
_vars = ()
_funs = ()
t, ch, th, ph = _coords
_metric = diag(-1, cos(t)**2, cos(t)**2*sinh(ch)**2, cos(t)**2*sinh(ch)**2*sin(th)**2)
del t, ch, th, ph
