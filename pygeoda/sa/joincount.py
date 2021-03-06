from ..libgeoda import gda_localjoincount, gda_localmultijoincount, VecBool, VecVecBool
from .lisa import lisa
import multiprocessing

__author__ = "Xun Li <lixun910@gmail.com>"

def local_joincount(w, data, **kwargs):
    """Local Join Count Statistics

    The function to apply local Join Count statistics.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple/list/pandas.Series): A list of numeric values of selected variable
        undefs (list, optional): A list of boolean values to indicate which value is undefined or null
        permutations (int, optional): The number of permutations for the LISA computation
        permutation_method (str, optional): The permutation method used for the LISA computation. Options are {'complete', 'lookup-table'}. Default is 'complete'.
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class. 
    """
    if w == None:
        raise ValueError("Weights is None.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    permutation_method = 'complete' if 'permutation_method' not in kwargs else kwargs['permutation_method']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    for i in data:
        if i != 0 and i != 1:
            raise ValueError("The input data is not binary.")

    lisa_obj = gda_localjoincount(w.gda_w, list(data), list(undefs), significance_cutoff, cpu_threads, permutations, permutation_method, seed)
    return lisa(lisa_obj)

def local_bijoincount(w, data, **kwargs):
    """Bivariate Local Join Count Statistics

    The function to apply (no-colocation) bivariate local Join Count statistics. The bivariate local join count only applies on two variables with no-colocation.

    Args:
        w (Weight): An instance of Weight class
        data (list or dataframe):   A list of numeric vectors of selected variable or a data frame of selected variables e.g. guerry[['Crm_prs', 'Literacy']]
        permutations (int, optional): The number of permutations for the LISA computation
        permutation_method (str, optional): The permutation method used for the LISA computation. Options are {'complete', 'lookup-table'}. Default is 'complete'.
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class 

    Examples:
        >>> import pygeoda
        >>> columbus = pygeoda.open("./data/columbus.shp")
        >>> columbus_q = pygeoda.queen_weights(columbus)
        >>> nsa = columbus.GetRealCol("nsa")
        >>> nsa_inv = [1-i for i in nsa]
        >>> lisa = pygeoda.local_bijoincount(columbus_q, [nsa, nsa_inv])
        >>> jc = lisa.lisa_values()
        (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.0, 3.0, 2.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        >>> pvals = lisa.lisa_pvalues()
        (nan, nan, nan, nan, nan, nan, nan, nan, 0.002, 0.034, nan, nan, nan, nan, nan, nan, 0.44, nan, nan, nan, nan, 0.262, nan, 0.125, 0.079, 0.053, nan, nan, nan, nan, 0.093, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan)
        >>> nn = lisa.lisa_num_nbrs()
        (2, 3, 4, 4, 8, 2, 4, 6, 8, 4, 5, 6, 4, 6, 6, 8, 3, 4, 3, 10, 3, 6, 3, 7, 8, 6, 4, 9, 7, 5, 3, 4, 4, 4, 7, 5, 6, 6, 3, 5, 3, 2, 6, 5, 4, 2, 2, 4, 3)
    """
    if w == None:
        raise ValueError("Weights is None.")

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    if len(data) != 2:
        raise ValueError("The input data should be a list of tuples of two selected variables.")
    
    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    permutation_method = 'complete' if 'permutation_method' not in kwargs else kwargs['permutation_method']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    data1 = data[0]
    data2 = data[1]

    n1 = len(data1)
    n2 = len(data2)

    if n1 != n2:
        raise ValueError("The size of data1 does not match the size of data2.")

    for d in data:
        for i in d:
            if i != 0 and i != 1:
                raise ValueError("The input data is not binary.")

    has_colocation = False
    for i in range(n1):
        if data1[i] == 1 and data2[i] == 1:
            has_colocation = True
            break

    if has_colocation:
        raise ValueError("The bivariate local join count only applies on two variables with no-colocation.")

    lisa_obj = gda_localmultijoincount(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, permutation_method, seed)
    return lisa(lisa_obj)

def local_multijoincount(w, data, **kwargs):
    """(Multivariate) Colocation Local Join Count Statistics

    The function to apply (multivariate) colocation local Join Count statistics

    Args:
        w (Weight): An instance of Weight class
        data (list or dataframe):   A list of numeric vectors of selected variable or a data frame of selected variables e.g. guerry[['Crm_prs', 'Literacy']]
        permutations (int, optional): The number of permutations for the LISA computation
        permutation_method (str, optional): The permutation method used for the LISA computation. Options are {'complete', 'lookup-table'}. Default is 'complete'.
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class 
    """
    if w == None:
        raise ValueError("Weights is None.")

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    permutation_method = 'complete' if 'permutation_method' not in kwargs else kwargs['permutation_method']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    n_vars = len(data)
    if n_vars <= 1:
        raise ValueError("The multivairate local Join Count applies to multiple (more than one) variables.")

    n_obs = len(data[0])
    for d in data:
        if len(d) != n_obs:
            raise ValueError("The input data have variables with different size.")
        for i in d:
            if i != 0 and i != 1:
                raise ValueError("The input data is not binary.")

    if n_vars == 2 and (sum(data[0]) + sum(data[1]) == n_obs):
        no_colocation = True
        for i in range(n_obs):
            if data[0][i] == 1 and data[1][i] == 1:
                no_colocation = False
                break
        if no_colocation: 
            raise ValueError("The input two variables have no colocations. Please use bivariate local join count: local_bijoincount().")

    lisa_obj = gda_localmultijoincount(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, permutation_method, seed)
    return lisa(lisa_obj)