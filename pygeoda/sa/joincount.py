from ..libgeoda import gda_localjoincount, gda_localmultijoincount, VecBool, VecVecBool
from .lisa import lisa
import multiprocessing

__author__ = "Xun Li <lixun910@gmail.com>"

def local_joincount(w, data, **kwargs):
    """Apply local join count statistics 

    Args:
        w (Weight): An instance of Weight class.
        data (tuple): A 1d tuple of float type values of selected variable
        permutations (int, optional): The number of permutations for the LISA computation
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class represents the results of lisa computations 
    """
    if w == None:
        raise ValueError("Weights is None.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_localjoincount(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, seed)
    return lisa(lisa_obj)

def local_multijoincount(w, data, **kwargs):
    """Apply multivariate local join count statistics on multi-variables

    Args:
        w (Weight): An instance of Weight class
        data (list): A 2d numeric list with values of selected variables

    Rrturns:
        lisa: An instance of lisa class represents the results of multivariate local join count
    """
    if w == None:
        raise ValueError("Weights is None.")

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_localmultijoincount(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, seed)
    return lisa(lisa_obj)