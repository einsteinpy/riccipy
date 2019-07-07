# Buchdahl and Land's static spherically symmetric stiff perfect fluid with rhob=2
_coords = symbols('t r theta phi', real=True)
_vars = ()
_funs = ()
t, r, th, ph = _coords
_metric = diag(-Rational(2,3)*r**2, 1/(Rational(1,2)-r**2/3), r**2, r**2*sin(th)**2)
del t, r, th, ph
