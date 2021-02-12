__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import VecBool, VecVecBool
from ..libgeoda import gda_localgeary, gda_localmultigeary
from .lisa import lisa

'''
Changes:
1/21/2021 Update local_multigeary, local_geary for 0.0.6
'''

def local_multigeary(w, data, **kwargs):
    '''Apply local multi-variates geary statistics on multi-variables, at least two variables, after we already have a weight.

    Args:
        w (Weight): An instance of Weight class
        data (list): A list of numeric tuples with values of selected variables
        undefs (tuple, optional): A tuple of boolean values to indicate which value is undefined or null
        permutations (int, optional): The number of permutations for the LISA computation
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class.
    '''
    if w == None:
        raise ValueError("Weights is None.")

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_localmultigeary(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, seed)
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
        raise ValueError("Weights is None.")

    if w.num_obs != len(data):
        raise ValueError("The size of data doesnt not match the number of observations.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_localgeary(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, seed)
    return lisa(lisa_obj)