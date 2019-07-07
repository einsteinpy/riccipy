# Static form of anti-de Sitter space
_coords = symbols('t r theta phi', real=True)
_vars = ()
_funs = ()
t, r, th, ph = _coords
_metric = diag(-cosh(r)**2, 1, sinh(r)**2, sinh(r)**2*sin(th)**2)
