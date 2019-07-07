# Heintzmann's static spherically symmetric perfect fluid solution
_coords = symbols('t r theta phi', real=True)
_vars = symbols('A a K', constant=True)
_funs = ()
t, r, th, ph = _coords
A, a, K = _vars
_metric = diag(-A**2*(1+a*r**2)**3, (1+a*r**2)/K, r**2, r**2*sin(th)**2)
del t, r, th, ph, A, a, K
