from riccipy.metric import *
from riccipy.partial import *
from riccipy.tensor import *
from sympy import diag, sin, symbols


def _generate_schwarzschild():
    coords = symbols("t r theta phi", real=True)
    t, r, th, ph = coords
    schw = diag(1 - 1 / r, -1 / (1 - 1 / r), -r ** 2, -r ** 2 * sin(th) ** 2)
    g = SpacetimeMetric("g", coords, schw, timelike=True)
    mu, nu = indices("mu nu", g)
    return (coords, t, r, th, ph, schw, g, mu, nu)


def test_DiffOperator():
    x, y = symbols("x y")
    dx = DiffOperator(x)
    assert (0 * dx) == 0
    expr = dx * (1 - 1 / x)
    assert expr == 1 / x ** 2
    expr = (1 - 1 / x) * dx
    assert isinstance(expr, DiffOperator)
    assert (expr * (x ** 3 / 3)).equals(x * (x - 1))
    dy = DiffOperator(y)
    res = dx * dy
    assert res.args == (x, y)


def test_PartialDerivative():
    (coords, t, r, th, ph, schw, g, mu, nu) = _generate_schwarzschild()
    d = g.partial
    assert isinstance(d, PartialDerivative)
    assert isinstance(d, Tensor)
    assert d.commutes_with(d) == 0
    assert d.covar == (-1,)
    assert all([isinstance(dx, DiffOperator) for dx in d.as_array()])
