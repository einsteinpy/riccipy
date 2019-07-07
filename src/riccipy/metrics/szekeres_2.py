# Szekeres solution for a special stiff perfect fluid in Abelian type coordinates
_coords = symbols('t x y z', real=True)
_vars = ()
_funs = ()
t, x, y, z = _coords
_metric = diag(-exp(6*x)/cosh(2*t)**2, exp(6*x)/cosh(2*t)**2, exp(2*x)*cosh(2*t), exp(2*x)*cosh(2*t))
del t, x, y, z
