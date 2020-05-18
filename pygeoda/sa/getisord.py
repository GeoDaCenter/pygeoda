__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import gda_localg, gda_localgstar, VecBool
from .lisa import lisa
import multiprocessing

def local_g(w, data, **kwargs):
    """Apply local Getis-Ord G statistics.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A 1d tuple of float type values of selected variable

    Returns:
        lisa: An instance of lisa class represents the results of local geary computations 
    """
    if w == None:
        raise("Weights is None.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    nCPUs =  multiprocessing.cpu_count() if 'nCPUs' not in kwargs else kwargs['nCPUs']
    perm =  999 if 'perm' not in kwargs else kwargs['perm']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj =  gda_localg(w.gda_w, data, undefs, nCPUs, perm, seed)
    return lisa(lisa_obj)

def local_gstar(w, data, **kwargs):
    """Apply local Getis-Ord G* statistics.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A 1d tuple of float type values of selected variable

    Returns:
        lisa: An instance of lisa class represents the results of local geary computations 
    """
    if w == None:
        raise("Weights is None.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    nCPUs =  multiprocessing.cpu_count() if 'nCPUs' not in kwargs else kwargs['nCPUs']
    perm =  999 if 'perm' not in kwargs else kwargs['perm']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj =  gda_localgstar(w.gda_w, data, undefs, nCPUs, perm, seed)
    return lisa(lisa_obj)