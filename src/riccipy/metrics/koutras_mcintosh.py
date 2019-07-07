# Koutras-McIntosh metric (no symmetries or invariants)
_coords = symbols('w u x y', real=True)
_vars = symbols('a b', constant=True)
_funs = symbols('f', cls=Function)
w, u, x, y = _coords
a, b = _vars
f = _funs
_metric = zeros(4)
_metric[1,1] = -(2*f(u)*(a*x+b)*(x**2+y**2)-a**2*w**2)
_metric[2,2] = 1
_metric[3,3] = 1
_metric[0,1] = _metric[1,0] = -(a*x+b)
_metric[1,2] = _metric[2,1] = a*w
del w, u, x, y, a, b, f
