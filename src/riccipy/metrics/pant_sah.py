# Pant and Sah charged static spherically symmetric solution
_coords = symbols('t r theta phi', real=True)
_vars = symbols('A n', constant=True)
_funs = ()
t, r, th, ph = _coords
A, n = _vars
_metric = diag(-A*r**(2*n), n**2+1, r**2, r**2*sin(th)**2)
del t, r, th, ph, A, n
