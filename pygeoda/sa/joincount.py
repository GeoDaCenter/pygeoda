from ..libgeoda import gda_joincount
from .lisa import lisa

__author__ = "Xun Li <lixun910@gmail.com>"

def local_joincount(w, data):
    """Apply local join count statistics.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A 1d tuple of float type values of selected variable

    Returns:
        lisa: An instance of lisa class represents the results of local geary computations 
    """
    if w == None:
        raise("Weights is None.")

    lisa_obj = gda_joincount(w.gda_w, data)
    return lisa(lisa_obj)