"""
A module for spatial weights
"""
from .queen import queen_weights
from .rook import rook_weights
from .distance import distance_weights, min_distthreshold, knn_weights
from .kernel import kernel_weights, kernel_knn_weights
from .weight import Weight, read_gal, read_gwt, read_swm