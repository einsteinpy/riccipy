"""
RicciPy
=======

Python library for Tensor Manipulation in General Relativity

"""

__version__ = "0.1.dev0"
from .metric import Metric, SpacetimeMetric, load_metric
from .tensor import Index, Tensor, expand_tensor, indices
