# McLenaghan Tariq Tupper metric
_coords = symbols('t x y phi', real=True)
_vars = symbols('a', constant=True)
_funs = ()
t, x, y, ph = _coords
_metric = diag(-1, a**2/x**2, a**2/x**2, x**2-4*y**2)
_metric[0,3] = _metric[3,0] = 2*y
del t, x, y, ph
