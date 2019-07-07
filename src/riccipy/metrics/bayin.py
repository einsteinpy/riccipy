# Bayin's spherically symmetric static perfect fluid solution II
_coords = symbols('t r theta phi', real=True)
_vars = symbols('w_0 C_0 C_1', constant=True)
_funs = ()
t, r, th, ph = _coords
w_0, C_0, C_1 = _vars
_metric = zeros(4)
_metric[0,0] = -C_0**2*exp(-asin((-2*r**2 + C_1)/(C_1**2 + 4*w_0**2)**(Rational(1,2))))
_metric[1,1] = w_0**2/(-r**4 + C_1*r**2 + w_0**2)
_metric[2,2] = r**2
_metric[3,3] = r**2*sin(th)**2
del t, r, th, ph, w_0, C_0, C_1
