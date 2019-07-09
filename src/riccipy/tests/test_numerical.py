import numpy as np
from types import FunctionType
from riccipy.tensor import *
from riccipy.metric import *
from riccipy.numerical import *

from sympy import diag, sin, symbols

def _generate_schwarzschild():
    coords = symbols("t r theta phi", real=True)
    t, r, th, ph = coords
    schw = diag(1 - 1 / r, -1 / (1 - 1 / r), -r ** 2, -r ** 2 * sin(th) ** 2)
    g = Metric("g", coords, schw)
    mu, nu = indices("mu nu", g)
    return (coords, t, r, th, ph, schw, g, mu, nu)

def test_NumericalArray():
    (coords, t, r, th, ph, schw, g, mu, nu) = _generate_schwarzschild()
    narr = NumericalArray((r, th), g.as_array())
    expect = [[0.5, 0, 0, 0], [0, -2, 0, 0], [0, 0, -4, 0], [0, 0, 0, 0]]
    assert isinstance(narr(2,0), np.ndarray)
    assert (narr(2, 0) == expect).all()
    assert isinstance(narr[0,0], FunctionType)
    assert narr[0,0](2,0) == 0.5

def test_lambdify_tensor():
    (coords, t, r, th, ph, schw, g, mu, nu) = _generate_schwarzschild()
    narr = lambdify_tensor((r, th), g(-mu,-nu))
    assert isinstance(narr, NumericalArray)
