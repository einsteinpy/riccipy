from functools import partial
from itertools import starmap
from types import FunctionType

import numpy as np
from sympy import Array, lambdify
from sympy.tensor.tensor import TensExpr

from .tensor import expand_tensor


class NumericalArray(object):
    """
    Class for representing an array of symbolic expressions as lambdified functions.

    Calling instances of this class will result in the evaluation of a lambda function
    that returns a numerically valued array representing the results of the individual
    component expressions.

    Furthermore, instances may also be used to access specific components in a manner
    identical to accessing the components of an numpy array.

    """

    def __init__(self, args, array, **kwargs):
        """
        Create a new NumericalArray.

        Parameters
        ----------
        args : (list, tuple)
            Iterable of ~sympy.Symbol objects that specifcy the order of the arguments
            for the lambda functions that will be generated.
        array : (list, tuple, ~sympy.Matrix, ~sympy.Array)
            The array of symbolic expressions to be lambdified.

        """
        array = Array(array)
        self._vars = args
        self._objstr = str(array)
        self._array = array
        self._modules = kwargs.pop("modules", None)
        self._lambda = lambdify(self._vars, self._array, modules=self._modules)
        self._generator = self._build_generator()

    def _build_generator(self):
        shape = self._array.shape
        ndarr = np.ndarray(shape, dtype=FunctionType)
        lfunc = partial(lambdify, modules=self._modules)
        generator = starmap(lfunc, [(self._vars, elem) for elem in self._array])
        ndarr.put(range(len(self._array)), list(generator))
        return ndarr

    def __getitem__(self, key):
        return self._generator.__getitem__(key)

    def __call__(self, *args):
        return np.asarray(self._lambda(*args))

    def __getattr__(self, attr):
        if hasattr(self._array, attr):
            return getattr(self._array, attr)
        raise AttributeError("%s has no attribute: %s", self.__class__.__name__, attr)

    def __repr__(self):
        return "NumericalArray(%s)" % self._objstr

    def __str__(self):
        return self.__repr__()


def lambdify_tensor(args, expr, idxs=None, **kwargs):
    """
    Generate a numerical array representation for the result of a tensor expression.

    When the tensor expression passed results in an instance of ~sympy.Array, a
    NumericalArray object is returned.
    A NumericalArray can be used to access lambda functions for either the array
    as a whole or for individual components. See the example below.

    Parameters
    ----------
    args : (list, tuple)
        Iterable of ~sympy.Symbol objects that specifcy the order of the arguments
        for the lambda functions that will be generated.
    expr : (~sympy.tensor.tensor.TensExpr, ~sympy.Expr)
        The tensor expression to be lambdified. If this is an ordinary expression
        this function defaults to ~sympy.lambdify.
    idxs : (list, tuple)
        Iterable of Index objects to specify the indices for the result of ``expr``.

    Examples
    --------
    >>> t, r, th, ph = symbols('t r theta phi', real=True)
    >>> schw = diag(1-1/r, -1/(1-1/r), -r**2, -r**2*sin(th)**2)
    >>> g = Metric('g', (t, r, th, ph), schw)
    >>> narr = lambdify_tensor((r, th), g(-mu,-nu))
    >>> narr(2, 0)
    array([[ 0.5,  0. ,  0. ,  0. ],
            [ 0. , -2. ,  0. ,  0. ],
            [ 0. ,  0. , -4. ,  0. ],
            [ 0. ,  0. ,  0. , -0. ]])
    >>> narr[0,0]
    <function _lambdifygenerated(r, theta)>
    >>> narr[0,0](2, 0)
    0.5

    """
    if isinstance(expr, TensExpr):
        expr = expand_tensor(expr, idxs)
    if isinstance(expr, Array):
        return NumericalArray(args, expr, **kwargs)
    return lambdify(args, expr, **kwargs)
