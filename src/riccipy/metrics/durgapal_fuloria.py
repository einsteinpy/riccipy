# Durgapal and Fuloria's static spherically symmetric perfect fluid
_coords = symbols('t r theta phi', real=True)
_vars = symbols('B C', constant=True)
_funs = ()
t, r, th, ph = _coords
B, C = _vars
expr = 1 + C*r**2
_metric = diag(-B*expr**4, 7*expr**2/(-expr**2-8*expr+16), r**2, r**2*sin(th)**2)
del expr, t, r, th, ph, B, C
