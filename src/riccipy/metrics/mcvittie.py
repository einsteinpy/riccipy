# McVittie's plane Einstein-Maxwell field with Lambda=0
_coords = symbols('t x y z', real=True)
_vars = symbols('M Q', constant=True)
_funs = ()
t, x, y, z = _coords
M, Q = _vars
_metric = diag(-(M/z+Q**2/z**2), z**2, z**2, 1/(M/z+Q**2/z**2))
del t, x, y, z, M, Q
