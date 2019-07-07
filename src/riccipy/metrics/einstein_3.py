# Einstein's static universe. Curvature coordinates
_coords = symbols('t r theta phi', real=True)
_vars = symbols('Lambda', constant=True)
_funs = ()
t, r, th, ph = _coords
La = _vars
_metric = diag(-1, 1/(1-La*r**2), r**2, r**2*sin(th)**2)
del t, r, th, ph, La
