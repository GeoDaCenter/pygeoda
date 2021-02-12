from ..libgeoda import gda_queen_weights 
from .weight import Weight

__author__ = "Xun Li <lixun910@gmail.com>"

def queen_weights(geoda_obj, **kwargs): 
    """Queen Contiguity Spatial Weights
    Create a Queen contiguity weights with options of "order", "include lower order" and "precision threshold"
    
    Args:
        geoda_obj (geoda): An instance of Geoda object
        order (int, optional): An integer value of order of contiguity
        include_lower_order (bool, optional):  A bool flag indicates whether or not the lower order neighbors should be 
            included in the weights structure. Defaults to False.
        precision_threshold  (float, optional):  A float value represents the precision of the underlying shape file is insufficient 
            to allow for an exact match of coordinates to determine 
            which polygons are neighbors. Defaults to 0.0.

    Returns:
        Weight: An instance of Weight class 
    """
    order = 1 if 'order' not in kwargs else kwargs['order']
    include_lower_order = False if 'include_lower_order' not in kwargs else kwargs['include_lower_order']
    precision_threshold = 0.0 if 'precision_threshold' not in kwargs else kwargs['precision_threshold']

    gda_w = gda_queen_weights(geoda_obj.gda, order, include_lower_order, precision_threshold)

    return Weight(gda_w)

