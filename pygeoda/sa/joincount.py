from ..libgeoda import gda_localjoincount, gda_localmultijoincount, VecBool, VecVecBool
from .lisa import lisa
import multiprocessing

__author__ = "Xun Li <lixun910@gmail.com>"

def local_joincount(w, data, **kwargs):
    """Local Join Count Statistics

    The function to apply local Join Count statistics.

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

def local_bijoincount(w, data1, data2, **kwargs):
    """Bivariate Local Join Count Statistics

    The function to apply (no-colocation) bivariate local Join Count statistics. The bivariate local join count only applies on two variables with no-colocation.

    Args:
        w (Weight): An instance of Weight class
        data1 (tuple): A 1d tuple of float type values of selected variable
        data2 (tuple): A 1d tuple of float type values of selected variable
        permutations (int, optional): The number of permutations for the LISA computation
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class represents the results of bivariate local join count

    Examples:
        >>> import pygeoda
        >>> columbus = pygeoda.open("./data/columbus.shp")
        >>> columbus_q = pygeoda.weights.queen(columbus)
        >>> nsa = columbus.GetRealCol("nsa")
        >>> nsa_inv = [1-i for i in nsa]
        >>> lisa = pygeoda.local_bijoincount(columbus_q, nsa, nsa_inv)
        >>> jc = lisa.GetLISAValues()
        (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 3.0, 2.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        >>> pvals = lisa.GetPValues()
        (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002, 0.034, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.44, 0.0, 0.0, 0.0, 0.0, 0.262, 0.0, 0.125, 0.079, 0.053, 0.0, 0.0, 0.0, 0.0, 0.093, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        >>> nn = lisa.GetNumNeighbors()
        (2, 3, 4, 4, 8, 2, 4, 6, 8, 4, 5, 6, 4, 6, 6, 8, 3, 4, 3, 10, 3, 6, 3, 7, 8, 6, 4, 9, 7, 5, 3, 4, 4, 4, 7, 5, 6, 6, 3, 5, 3, 2, 6, 5, 4, 2, 2, 4, 3)
    """
    if w == None:
        raise ValueError("Weights is None.")

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    n1 = len(data1)
    n2 = len(data2)

    if n1 != n2:
        raise ValueError("The size of data1 does not match the size of data2.")

    if sum(data1) + sum(data2) != n1:
        raise ValueError("The bivariate local join count only applies on two variables with no-colocation.")

    data = [data1, data2]
    lisa_obj = gda_localmultijoincount(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, seed)
    return lisa(lisa_obj)

def local_multijoincount(w, data, **kwargs):
    """(Multivariate) Colocation Local Join Count Statistics

    The function to apply (multivariate) colocation local Join Count statistics

    Args:
        w (Weight): An instance of Weight class
        data (list): A 2d numeric list with values of selected variables
        permutations (int, optional): The number of permutations for the LISA computation
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class represents the results of multivariate local join count
    """
    if w == None:
        raise ValueError("Weights is None.")

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    n_vars = len(data)
    if n_vars <= 1:
        raise ValueError("The multivairate local Join Count applies to multiple (more than one) variables.")

    n_obs = len(data[0])
    for d in data:
        if len(d) != n_obs:
            raise ValueError("The input data have variables with different size.")

    if n_vars == 2 and (sum(data[0]) + sum(data[1]) == n_obs):
        raise ValueError("The input two variables have no colocations. Please use bivariate local join count: local_bijoincount().")

    lisa_obj = gda_localmultijoincount(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, seed)
    return lisa(lisa_obj)