from ..libgeoda import gda_localmoran, VecBool
from .lisa import lisa
import multiprocessing

__author__ = "Xun Li <lixun910@gmail.com>"

def local_moran(w, data, **kwargs):
    """Apply local moran statistics.

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