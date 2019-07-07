# Einstein's static universe. Polar coordinates
_coords = symbols('t chi theta phi', real=True)
_vars = symbols('Lambda', constant=True)
_funs = ()
t, ch, th, ph = _coords
La = _vars
_metric = diag(-1/La, 1/La, sin(ch)**2/La, sin(ch)**2*sin(th)**2/La)
del t, ch, th, ph, La
