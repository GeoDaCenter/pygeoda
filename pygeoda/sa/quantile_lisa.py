from ..libgeoda import gda_quantilelisa, gda_multiquantilelisa
from ..libgeoda import VecBool, VecInt, VecVecDouble, VecVecBool, VecDouble
from .lisa import lisa

__author__ = "Hang Zhang <zhanghanggis@163.com>, Xun Li <lixun910@gmail.com>"

'''
Changes:
1/21/2021 update quantile_lisa; add multiquantile_lisa
'''

def quantile_lisa(w, k, q, data, **kwargs):
    """Apply local quantile LISA statistics 

    Args:
        w (Weight): A spatial Weights object
        k (int): The number of quantiles, range[1, n-1]
        q (int): The index of selected quantile for lisa, range[0, k-1]
        data (tuple): A array of numeric values of selected variable
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

def multiquantile_lisa(w, quantile_data, **kwargs):
    """Apply multivariate quantile LISA statistics

    Args:
        w (Weight): A spatial Weights object
        quantile_data (tuple): A list of {k:k_value, q:q_value, data:data_value} for more than one variable. Each variable will be set with: k, indicates the number of quantiles; q, indicates which quantile or interval used in local join count statistics; data, is a numeric array of selected variable
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

    n_q = len(quantile_data)

    if n_q < 1:
        raise ValueError("quantile_data is empty.")

    k_s = VecInt()
    q_s = VecInt()
    d_s = VecVecDouble()

    for q_data in quantile_data:
        if 'k' not in q_data or 'q' not in q_data or 'data' not in q_data:
            raise ValueError("quantile_data should be a list of {k:k_value, q:q_value, data:data_value}.")
        k = q_data['k']
        q = q_data['q']
        d = q_data['data']

        if k == None or k < 1:
            raise ValueError("The value of k needs to be greater than or equal to 1 ")

        if q == None or q < 0:
            raise ValueError("The value of q needs to be greater than to 0")
        elif q > k:
            raise ValueError("The value of q needs to be smaller than or equal to the max value of k")

        k_s.push_back(k)
        q_s.push_back(q)
        d_s.push_back(VecDouble(d))

    lisa_obj = gda_multiquantilelisa(w.gda_w, k_s, q_s, d_s, undefs, significance_cutoff, cpu_threads, permutations, seed)
    return lisa(lisa_obj)