# General static, spherically symmetric metric in curvature coordinates
_coords = symbols('t r theta phi', real=True)
_vars = ()
_funs = symbolic('alpha beta', cls=Function)
t, r, th, ph = _coords
al, be = _funs
_metric = diag(-exp(2*al(r)), exp(2*be(r)), exp(2*be(r))*r**2, exp(2*be(r))*r**2*sin(th)**2)
del t, r, th, ph, al, be
