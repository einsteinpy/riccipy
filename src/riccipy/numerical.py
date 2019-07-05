from functools import partial
from itertools import starmap
from types import FunctionType

import numpy as np
from sympy import lambdify
from sympy.tensor.tensor import TensExpr

from .tensor import expand_tensor


class NumericalArray(object):
    def __init__(self, args, expr, idxs=None, **kwargs):
        self._vars = args
        self._objstr = str(expr)
        self._array = (
            expand_tensor(expr, idxs=idxs) if isinstance(expr, TensExpr) else expr
        )
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
    return NumericalArray(args, expr, idxs, **kwargs)
