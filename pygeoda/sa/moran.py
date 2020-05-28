from ..libgeoda import gda_localmoran, VecBool, gda_batchlocalmoran, VecVecBool
from .lisa import lisa, batchlisa
import multiprocessing

__author__ = "Xun Li <lixun910@gmail.com>"

def local_moran(w, data, **kwargs):
    """Apply local moran statistics on one select variable after we already have a weight.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A 1d tuple of float type values of selected variable

    Returns:
        lisa: An instance of lisa class represents the results of local geary computations
    """
    if w == None:
        raise("Weights is None.")

    if w.num_obs != len(data):
        raise("The size of data doesnt not match the number of observations.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    nCPUs =  multiprocessing.cpu_count() if 'nCPUs' not in kwargs else kwargs['nCPUs']
    perm =  999 if 'perm' not in kwargs else kwargs['perm']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_localmoran(w.gda_w, data, undefs, nCPUs, perm, seed)
    return lisa(lisa_obj)


def batch_local_moran(w, data, **kwargs):
    """Apply local moran statistics on a set of variables using a same weights.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A 2d list of float type values of selected variables

    Returns:
        lisa: An instance of BatchLisa class represents the results of local geary computations
    """
    if w == None:
        raise("Weights is None.")

    if (not isinstance(data, list)) or (len(data) < 1):
        raise("The data has to be a 2-d list of float type values of selected variables.")

    if w.num_obs != len(data[0]):   
        raise("The size of data doesnt not match the number of observations.")

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    nCPUs =  multiprocessing.cpu_count() if 'nCPUs' not in kwargs else kwargs['nCPUs']
    perm =  999 if 'perm' not in kwargs else kwargs['perm']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_batchlocalmoran(w.gda_w, data, undefs, nCPUs, perm, seed)
    return batchlisa(lisa_obj)