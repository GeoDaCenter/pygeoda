__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import gda_geary, gda_multigeary, VecBool, VecVecBool
from .lisa import lisa
import multiprocessing

def local_multigeary(w, data, **kwargs):
    '''Apply local multi-variates geary statistics on multi-variables, at least two variables, after we already have a weight.

    Args:
        w (Weight): An instance of Weight class
        data (list): A 2d numeric list with values of selected variables
    Returns:
        lisa: An instance of lisa class represents the results of local multi-variates geary computations
    '''
    if w == None:
        raise("Weights is None.")

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    nCPUs =  multiprocessing.cpu_count() if 'nCPUs' not in kwargs else kwargs['nCPUs']
    perm =  999 if 'perm' not in kwargs else kwargs['perm']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_multigeary(w.gda_w, data, undefs, nCPUs, perm, seed)
    return lisa(lisa_obj)

def local_geary(w, data, **kwargs):
    '''Apply local geary statistics on one select variable after we already have a weight.

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

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    nCPUs =  multiprocessing.cpu_count() if 'nCPUs' not in kwargs else kwargs['nCPUs']
    perm =  999 if 'perm' not in kwargs else kwargs['perm']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_geary(w.gda_w, data, undefs, nCPUs, perm, seed)
    return lisa(lisa_obj)