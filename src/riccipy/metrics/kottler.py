# Kottler's generalization of the Schwarzschild metric with non-zero cosmological constant. Aka Schwarzschild-de Sitter.
_coords = symbols('t r theta phi', real=True)
_vars = symbols('M Lambda', constant=True)
_funs = ()
t, r, th, ph = _coords
M, La = _vars
expr = 1-2*M/r-La*r**2/3
_metric = diag(-expr, 1/expr, r**2, r**2*sin(th)**2)
del t, r, th, ph, M, La, expr
