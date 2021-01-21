from ..libgeoda import gda_localmoran, VecBool, gda_batchlocalmoran, VecVecBool
from .lisa import lisa, batchlisa
import multiprocessing

__author__ = "Xun Li <lixun910@gmail.com>"

def local_moran(w, data, **kwargs):
    """Apply local moran statistics on one select variable after we already have a weight.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A array of numeric values of selected variable
        permutations (int, optional): The number of permutations for the LISA computation
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class represents the results of lisa computation
    """
    if w == None:
        raise ValueError("Weights is None.")

    if w.num_obs != len(data):
        raise ValueError("The size of data doesnt not match the number of observations.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_localmoran(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, seed)
    return lisa(lisa_obj)


def batch_local_moran(w, data, **kwargs):
    """Apply local moran statistics on a set of variables using a same weights.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A list of numeric array of selected variables
        permutations (int, optional): The number of permutations for the LISA computation
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of BatchLisa class represents the results of lisa computations
    """
    if w == None:
        raise ValueError("Weights is None.")

    if (not isinstance(data, list)) or (len(data) < 1):
        raise ValueError("The data has to be a list of numeric array of selected variables.")

    if w.num_obs != len(data[0]):   
        raise ValueError("The size of data doesnt not match the number of observations.")

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_batchlocalmoran(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, seed)
    return batchlisa(lisa_obj)