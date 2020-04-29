"""
A module for spatial weights
"""
from .queen import queen
from .rook import rook
from .distance import distance, min_threshold, knn
from .kernel import kernel, kernel_bandwidth
from .weight import Weight