__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import gda_geary, gda_multigeary
from .lisa import lisa

def local_multigeary(w, data):
    '''Apply local multi-variates geary statistics 

    Args:

    Returns:
    
    '''
    # input check
    lisa_obj = gda_multigeary(w.gda_w, data)
    return lisa(lisa_obj)

def local_geary(w, data):
    '''Apply local geary statistics.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A 1d tuple of float type values of selected variable

    Returns:
        lisa: An instance of lisa class represents the results of local geary computations 
    '''
    if w == None:
        raise("Weights is None.")

    if w.num_obs != len(data):
        raise("The size of data doesnt not match the number of observations.")

    lisa_obj = gda_geary(w.gda_w, data)
    return lisa(lisa_obj)