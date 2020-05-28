from ..libgeoda import gda_quantilelisa, VecBool
from .lisa import lisa
import multiprocessing

__author__ = "Hang Zhang <zhanghanggis@163.com>, "

def quantile_lisa(w, k, q, data, **kwargs):
    """
    Apply quantile LISA on one select variable after we already have a weight. 

    Note:
        Apply quantile LISA on one select variable
    Args:
        w (Weight): A spatial Weights object
        k (int): The number of quantiles, range[1, n-1]
        q (int): The index of selected quantile for lisa, range[0, k-1]
        data (tuple): A tuple with values of the selected variable

    Returns:
        lisa: An instance of lisa class represents the results of quantile lisa
    """
    if w == None:
        raise("Weights is None.")

    if data is None:
        raise("The data from selected variable is empty.")

    if k == None or k < 1:
        raise("The value of k needs to be greater than or equal to 1 ")

    if q == None or q < 0:
        raise("The value of q needs to be greater than to 0")
    elif q > k:
        raise("The value of q needs to be smaller than or equal to the max value of k")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    nCPUs =  multiprocessing.cpu_count() if 'nCPUs' not in kwargs else kwargs['nCPUs']
    perm =  999 if 'perm' not in kwargs else kwargs['perm']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_quantilelisa(w.gda_w, k, q, data,undefs, nCPUs, perm, seed)
    return lisa(lisa_obj)