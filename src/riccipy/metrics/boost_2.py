# Metric with G4 on T3 and boost isotropy (flat case k=1)
_coords = symbols('t x y w', real=True)
_vars = ()
_funs = symbols('alpha beta', cls=Function)
t, x, y, w = _coords
al, be = _funs
_metric = diag(-be(w)**2*sinh(y)**2, al(w)**2, be(w)**2, 1)
del t, x, y, w, al, be
