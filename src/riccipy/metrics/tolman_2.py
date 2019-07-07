# Tolman's type VI solution
_coords = symbols('t r theta phi', real=True)
_vars = symbols('A B n', constant=True)
_funs = ()
t, r, th, ph = _coords
A, B, n = _vars
_metric = diag(-(A*r**(1-n)-B*r**(1+n))**2, 2-n**2, r**2, r**2*sin(th)**2)
del t, r, th, ph, A, B, n
