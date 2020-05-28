from ..libgeoda import gda_joincount, gda_multijoincount, VecBool, VecVecBool
from .lisa import lisa
import multiprocessing

__author__ = "Xun Li <lixun910@gmail.com>"

def local_joincount(w, data, **kwargs):
    """Apply local join count statistics on one select variable after we already have a weight.

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

    lisa_obj = gda_joincount(w.gda_w, data, undefs, nCPUs, perm, seed)
    return lisa(lisa_obj)

def local_multijoincount(w, data, **kwargs):
    """Apply multivariate local join count statistics on multi-variables, at least two variables, after we alreadt have a weight.

    Args:
        w (Weight): An instance of Weight class
        data (list): A 2d numeric list with values of selected variables

    Rrturns:
        lisa: An instance of lisa class represents the results of multivariate local join count
    """
    if w == None:
        raise("Weights is None.")

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    nCPUs =  multiprocessing.cpu_count() if 'nCPUs' not in kwargs else kwargs['nCPUs']
    perm =  999 if 'perm' not in kwargs else kwargs['perm']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_multijoincount(w.gda_w, data, undefs, nCPUs, perm, seed)
    return lisa(lisa_obj)