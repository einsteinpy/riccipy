# Static cylindrically symmetric Einstein-Maxwell field (iii) radial electric field (caused by an axial charge distribution)
_coords = symbols('t phi rho z', real=True)
_vars = symbols('a b m', constant=True)
_funs = ()
t, ph, rh, z = _coords
a, b, m = _vars
expr1 = cosh(log(a*rh**m))**2
expr2 = rh**(2*m**2)*b**2*expr1
_metric = diag(-1/(b**2*expr1), rh**2*b**2*expr1, expr2, expr2)
del expr1, expr2, t, ph, rh, z, a, b, m
