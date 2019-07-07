# de Sitter space
_coords = symbols('t r theta phi', real=True)
_vars = (symbols('lambda', constant=True),)
_funs = ()
t, r, th, ph = _coords
la = _vars
expr = 1 - la*r**2/3
_metric = diag(-expr, 1/expr, r**2, r**2*sin(th)**2)
del expr, t, r, th, ph, la
