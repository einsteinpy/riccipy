# The Bondi metric
_coords = symbols('r u theta phi', real=True)
_vars = ()
_funs = symbols('Q U V gamma', cls=Function)
r, u, th, ph = _coords
Q, U, V, ga = _funs
_metric = zeros(4)
_metric[1,1] = -exp(2*Q(r,u,th)+2*ga(r,u,th))*(V(r,u,th)*exp(-2*ga(r,u,th))-exp(-2*Q(r,u,th))*U(r,u,th)**2*r**3)/r
_metric[2,2] = r**2*exp(2*ga(r,u,th))
_metric[3,3] = r**2*exp(-2*ga(r,u,th))*sin(th)**2
_metric[0,1] = _metric[1,0] = -exp(2*Q(r,u,th))
_metric[1,2] = _metric[2,1] = -U(r,u,th)*r**2*exp(2*ga(r,u,th))
del r, u, th, ph, Q, U, V, ga
