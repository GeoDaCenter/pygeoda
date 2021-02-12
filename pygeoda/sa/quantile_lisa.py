from ..libgeoda import gda_quantilelisa, gda_multiquantilelisa
from ..libgeoda import VecBool, VecInt, VecVecDouble, VecVecBool, VecDouble
from .lisa import lisa

__author__ = "Xun Li <lixun910@gmail.com>, Hang Zhang <zhanghanggis@163.com>"

'''
Changes:
1/21/2021 update quantile_lisa; add multiquantile_lisa
2/11/2021 update local_quantilelisa, local_multiquantilelisa
'''

def local_quantilelisa(w, k, q, data, **kwargs):
    """Quantile LISA Statistics
    The function to apply quantile LISA statistics

    Args:
        w (Weight): A spatial Weights object
        data (tuple): A tuple of numeric values of selected variable
        k (int): The number of quantiles, range[1, n-1]
        q (int): The index of selected quantile for lisa, range[0, k-1]
        permutations (int, optional): The number of permutations for the LISA computation
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class represents the results of quantile lisa
    """
    if w == None:
        raise ValueError("Weights is None.")

    if data is None:
        raise ValueError("The data from selected variable is empty.")

    if k == None or k < 1:
        raise ValueError("The value of k needs to be greater than or equal to 1 ")

    if q == None or q < 0:
        raise ValueError("The value of q needs to be greater than to 0")
    elif q > k:
        raise ValueError("The value of q needs to be smaller than or equal to the max value of k")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_quantilelisa(w.gda_w, k, q, data,undefs, significance_cutoff, cpu_threads, permutations, seed)
    return lisa(lisa_obj)

def local_multiquantilelisa(w, data, k, q, **kwargs):
    """Multivariate Quantile LISA Statistics
    The function to apply multivariate quantile LISA statistics

    Args:
        w (Weight): A spatial Weights object
        data (list): A list of tuples with numeric values of selected variables
        k (tuple): A tuple of "k" (int) values indicate the number of quantiles for each variable
        q (tuple): A tuple of "q" (int) values indicate which quantile or interval for each variable used in local join count statistics
        permutations (int, optional): The number of permutations for the LISA computation
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class represents the results of quantile lisa
    """

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    if w == None:
        raise ValueError("Weights is None.")

    if len(data) == 0:
        raise ValueError("The input data can not be empty.")

    if len(data) != len(k) or len(k) != len(q):
        raise ValueError("The size of k, q and data are not matched.")

    lisa_obj = gda_multiquantilelisa(w.gda_w, k, q, data, undefs, significance_cutoff, cpu_threads, permutations, seed)
    return lisa(lisa_obj)