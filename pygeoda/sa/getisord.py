__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import gda_localg, gda_localgstar
from .lisa import lisa

def local_g(w, data):
    """Apply local Getis-Ord G statistics.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A 1d tuple of float type values of selected variable

    Returns:
        lisa: An instance of lisa class represents the results of local geary computations 
    """
    if w == None:
        raise("Weights is None.")

    lisa_obj =  gda_localg(w.gda_w, data)
    return lisa(lisa_obj)

def local_gstar(w, data):
    """Apply local Getis-Ord G* statistics.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A 1d tuple of float type values of selected variable

    Returns:
        lisa: An instance of lisa class represents the results of local geary computations 
    """
    if w == None:
        raise("Weights is None.")

    lisa_obj =  gda_localgstar(w.gda_w, data)
    return lisa(lisa_obj)