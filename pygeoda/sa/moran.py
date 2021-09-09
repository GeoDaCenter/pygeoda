from ..libgeoda import gda_localmoran, gda_bi_localmoran, VecBool, gda_batchlocalmoran, VecVecBool, gda_localmoran_eb
from .lisa import lisa, batchlisa

__author__ = "Xun Li <lixun910@gmail.com>"

def local_moran(w, data, **kwargs):
    """Local Moran statistics.

    Args:
        w (Weight): An instance of Weight class.
        data (tuple/list/pandas.Series): A tuple of numeric values of selected variable
        undefs (tuple/list, optional): A tuple of boolean values to indicate which value is undefined or null
        permutations (int, optional): The number of permutations for the LISA computation
        permutation_method (str, optional): The permutation method used for the LISA computation. Options are {'complete', 'lookup-table'}. Default is 'complete'.
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
    permutation_method = 'complete' if 'permutation_method' not in kwargs else kwargs['permutation_method']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_localmoran(w.gda_w, list(data), list(undefs), significance_cutoff, cpu_threads, permutations, permutation_method, seed)
    return lisa(lisa_obj)

def local_bimoran(w, data1, data2, **kwargs):
    """Bivariate local Moran statistics.
    The bivariate Local Moran’s I captures the relationship between the value for one variable at location i, and the average of the neighboring values for another variable.
    
    Args:
        w (Weight): An instance of Weight class.
        data1 (tuple/list/pandas.Series): A tuple of numeric values of first variable
        data1 (tuple/list/pandas.Series): A tuple of numeric values of second variable
        undefs (tuple/list, optional): A tuple of boolean values to indicate which value is undefined or null
        permutations (int, optional): The number of permutations for the LISA computation
        permutation_method (str, optional): The permutation method used for the LISA computation. Options are {'complete', 'lookup-table'}. Default is 'complete'.
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class represents the results of lisa computation
    """
    if w == None:
        raise ValueError("Weights is None.")

    if w.num_obs != len(data1) or len(data1) != len(data2):
        raise ValueError("The size of data doesnt not match the number of observations.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    permutation_method = 'complete' if 'permutation_method' not in kwargs else kwargs['permutation_method']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_bi_localmoran(w.gda_w, list(data1), list(data2), list(undefs), significance_cutoff, cpu_threads, permutations, permutation_method, seed)
    return lisa(lisa_obj)

def local_moran_eb(w, event_data, base_data, **kwargs):
    """The function to apply local Moran with EB Rate statistics. 
    The EB rate is first computed from "event" and "base" variables, and then used in local moran statistics.

    Args:
        w (Weight): An instance of Weight class
        event_data (tuple/list/pandas.Series): A numeric tuple of selected "event" variable
        base_data (tuple/list/pandas.Series): A numeric tuple of selected "base" variable
        permutations (int, optional): The number of permutations for the LISA computation
        permutation_method (str, optional): The permutation method used for the LISA computation. Options are {'complete', 'lookup-table'}. Default is 'complete'.
        significance_cutoff (float, optional): A cutoff value for significance p-values to filter not-significant clusters
        cpu_threads (int, optional): The number of cpu threads used for parallel LISA computation
        seed (int, optional): The seed for random number generator

    Returns:
        lisa: An instance of lisa class represents the results of lisa computation
    """
    if w == None:
        raise ValueError("Weights is None.")

    if w.num_obs != len(event_data) or w.num_obs != len(base_data):
        raise ValueError("The size of data doesnt not match the number of observations.")

    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    permutation_method = 'complete' if 'permutation_method' not in kwargs else kwargs['permutation_method']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_localmoran_eb(w.gda_w, list(event_data), list(base_data), significance_cutoff, cpu_threads, permutations, permutation_method, seed)
    return lisa(lisa_obj)

def batch_local_moran(w, data, **kwargs):
    """Apply local moran statistics on a set of variables

    Args:
        w (Weight): An instance of Weight class.
        data (list/pandas.dataframe): A list of numeric array of selected variables
        permutations (int, optional): The number of permutations for the LISA computation
        permutation_method (str, optional): The permutation method used for the LISA computation. Options are {'complete', 'lookup-table'}. Default is 'complete'.
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

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    undefs = VecVecBool() if 'undefs' not in kwargs else kwargs['undefs']
    permutations =  999 if 'permutations' not in kwargs else kwargs['permutations']
    permutation_method = 'complete' if 'permutation_method' not in kwargs else kwargs['permutation_method']
    significance_cutoff = 0.05 if 'significance_cutoff' not in kwargs else kwargs['significance_cutoff']
    cpu_threads =  6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']
    seed =  123456789 if 'seed' not in kwargs else kwargs['seed']

    lisa_obj = gda_batchlocalmoran(w.gda_w, data, undefs, significance_cutoff, cpu_threads, permutations, permutation_method, seed)
    return batchlisa(lisa_obj)