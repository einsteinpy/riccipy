# de Sitter space
_coords = symbols('t x y z', real=True)
_vars = (symbols('alpha', constant=True),)
_funs = ()
t, x, y, z = _coords
al = _vars
expr = exp(2*t/al)
_metric = diag(-1, expr, expr, expr)
del expr, t, x, y, z, al
