__author__ = "Xun Li <lixun910@gmail.com>"

from pygeoda.clustering.utils import calculate_clustering_statistics
from ..libgeoda import VecVecDouble, VecPair, VecInt
from ..libgeoda import gda_maxp_greedy, gda_maxp_sa, gda_maxp_tabu

'''
Changes:
1/20/2021 Add maxp_greedy, maxp_sa, maxp_tabu
'''


def maxp_greedy(w, data, bound_variable, min_bound, **kwargs):
    ''' A greedy algorithm to solve the max-p-region problem 

    The max-p-region problem is a special case of constrained clustering where a finite number of geographical areas are aggregated into the maximum number of regions (max-p-regions), such that each region is geographically connected and the clusters could maximize internal homogeneity.

    Arguments:
        w (Weight): an instance of Weight class
        data (list or dataframe):   A list of numeric vectors of selected variable or a data frame of selected variables e.g. guerry[['Crm_prs', 'Literacy']]
        bound_variable (tuple or pandas.core.series.Series, optional): A numeric vector of selected bounding variable
        min_bound (float): A minimum value that the sum value of bounding variable int each cluster should be greater than
        iterations (int, optional): The number of iterations of greedy algorithm. Defaults to 99.
        init_regions (tuple, optional): The initial regions that the local search starts with. Default is empty. means the local search starts with a random process to "grow" clusters
        scale_method (str, optional): One of the scaling methods {'raw', 'standardize', 'demean', 'mad', 'range_standardize', 'range_adjust'} to apply on input data. Default is 'standardize' (Z-score normalization).
        distance_method (str, optional):  The distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int, optional): The seed for random number generator. Defaults to 123456789. It is the same as GeoDa software
        cpu_threads (int, optional): The number of cpu threads used for parallel computation

    Returns:
        dict: A dict with keys {"Clusters", "TotalSS", "Within-clusterSS", "TotalWithin-clusterSS", "Ratio"}
    '''

    iterations = 99 if 'iterations' not in kwargs else kwargs['iterations']
    init_regions = [] if 'init_regions' not in kwargs else kwargs['init_regions']
    scale_method = "standardize" if "scale_method" not in kwargs else kwargs['scale_method']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs[
        'distance_method']
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']
    cpu_threads = 6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']

    if w.num_obs < 1:
        raise ValueError("The weights is not valid.")

    if len(data) < 1:
        raise ValueError("The data from selected variable is empty.")

    # check if bound_variable is pandas.core.series.Series, if so, convert to list
    if type(bound_variable).__name__ == "Series":
        bound_variable = bound_variable.values.tolist()

    if len(bound_variable) != w.num_obs:
        raise ValueError(
            "The bound_variable has to be a list of numeric values, e.g. a column of input table.")

    if min_bound <= 0:
        raise ValueError("The min_bound has to be a positive numeric value.")

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)

    min_bounds = VecPair()
    max_bounds = VecPair()

    min_bounds.push_back((min_bound, list(bound_variable)))

    in_init_regions = VecInt(list(init_regions))

    cluster_ids = gda_maxp_greedy(w.gda_w, in_data, scale_method, iterations, min_bounds,
                                  max_bounds, in_init_regions, distance_method, random_seed, cpu_threads)

    return calculate_clustering_statistics(cluster_ids, in_data, w.num_obs)


def maxp_sa(w, data, bound_variable, min_bound, cooling_rate=0.85, **kwargs):
    ''' A simulated annealing algorithm to solve the max-p-region problem 

    The max-p-region problem is a special case of constrained clustering where a finite number of geographical areas are aggregated into the maximum number of regions (max-p-regions), such that each region is geographically connected and the clusters could maximize internal homogeneity.

    Arguments:
        w (Weight): an instance of Weight class
        data (list or dataframe):   A list of numeric vectors of selected variable or a data frame of selected variables e.g. guerry[['Crm_prs', 'Literacy']]
        bound_variable (tuple): A numeric vector of selected bounding variable
        min_bound (float): A minimum value that the sum value of bounding variable int each cluster should be greater than
        cooling_rate (float): The cooling rate of a simulated annealing algorithm. Defaults to 0.85
        sa_maxit (int): The number of iterations of simulated annealing. Defaults to 1
        iterations (int, optional): The number of iterations of greedy algorithm. Defaults to 99.
        init_regions (tuple, optional): The initial regions that the local search starts with. Default is empty. means the local search starts with a random process to "grow" clusters
        scale_method (str, optional): One of the scaling methods {'raw', 'standardize', 'demean', 'mad', 'range_standardize', 'range_adjust'} to apply on input data. Default is 'standardize' (Z-score normalization).
        distance_method (str, optional):  The distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int, optional): The seed for random number generator. Defaults to 123456789. It is the same as GeoDa software
        cpu_threads (int, optional): The number of cpu threads used for parallel computation

    Returns:
        dict: A dict with keys {"Clusters", "TotalSS", "Within-clusterSS", "TotalWithin-clusterSS", "Ratio"}
    '''

    sa_maxit = 1 if 'sa_maxit' not in kwargs else kwargs['sa_maxit']
    iterations = 99 if 'iterations' not in kwargs else kwargs['iterations']
    init_regions = [] if 'init_regions' not in kwargs else kwargs['init_regions']
    scale_method = "standardize" if "scale_method" not in kwargs else kwargs['scale_method']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs[
        'distance_method']
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']
    cpu_threads = 6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']

    if cooling_rate <= 0 or cooling_rate >= 1:
        raise ValueError("Cooling rate should be in range (0,1).")

    if w.num_obs < 1:
        raise ValueError("The weights is not valid.")

    if len(data) < 1:
        raise ValueError("The data from selected variable is empty.")

    if len(bound_variable) != w.num_obs:
        raise ValueError(
            "The bound_variable has to be a list of numeric values, e.g. a column of input table.")

    if min_bound <= 0:
        raise ValueError("The min_bound has to be a positive numeric value.")

    in_data = VecVecDouble()

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    for d in data:
        in_data.push_back(d)

    min_bounds = VecPair()
    max_bounds = VecPair()

    min_bounds.push_back((min_bound, list(bound_variable)))

    in_init_regions = VecInt(list(init_regions))

    cluster_ids = gda_maxp_sa(w.gda_w, in_data, scale_method, iterations, cooling_rate, sa_maxit,
                              min_bounds, max_bounds, in_init_regions, distance_method, random_seed, cpu_threads)

    return calculate_clustering_statistics(cluster_ids, in_data, w.num_obs)


def maxp_tabu(w, data, bound_variable, min_bound, tabu_length=10, **kwargs):
    ''' A tabu-search algorithm to solve the max-p-region problem 

    The max-p-region problem is a special case of constrained clustering where a finite number of geographical areas are aggregated into the maximum number of regions (max-p-regions), such that each region is geographically connected and the clusters could maximize internal homogeneity.

    Arguments:
        w (Weight): an instance of Weight class
        data (list or dataframe):   A list of numeric vectors of selected variable or a data frame of selected variables e.g. guerry[['Crm_prs', 'Literacy']]
        bound_variable (tuple): A numeric vector of selected bounding variable
        min_bound (float): A minimum value that the sum value of bounding variable int each cluster should be greater than
        tabu_length (int): The length of a tabu search heuristic of tabu algorithm. Defaults to 10.
        conv_tabu (int, optional): The number of non-improving moves. Defaults to 10.
        iterations (int, optional): The number of iterations of greedy algorithm. Defaults to 99.
        init_regions (tuple, optional): The initial regions that the local search starts with. Default is empty. means the local search starts with a random process to "grow" clusters
        scale_method (str, optional): One of the scaling methods {'raw', 'standardize', 'demean', 'mad', 'range_standardize', 'range_adjust'} to apply on input data. Default is 'standardize' (Z-score normalization).
        distance_method (str, optional):  The distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int, optional): The seed for random number generator. Defaults to 123456789. It is the same as GeoDa software
        cpu_threads (int, optional): The number of cpu threads used for parallel computation

    Returns:
        dict: A dict with keys {"Clusters", "TotalSS", "Within-clusterSS", "TotalWithin-clusterSS", "Ratio"}
    '''

    conv_tabu = 10 if 'conv_tabu' not in kwargs else kwargs['conv_tabu']
    iterations = 99 if 'iterations' not in kwargs else kwargs['iterations']
    init_regions = [] if 'init_regions' not in kwargs else kwargs['init_regions']
    scale_method = "standardize" if "scale_method" not in kwargs else kwargs['scale_method']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs[
        'distance_method']
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']
    cpu_threads = 6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']

    if w.num_obs < 1:
        raise ValueError("The weights is not valid.")

    if len(data) < 1:
        raise ValueError("The data from selected variable is empty.")

    if len(bound_variable) != w.num_obs:
        raise ValueError(
            "The bound_variable has to be a list of numeric values, e.g. a column of input table.")

    if min_bound <= 0:
        raise ValueError("The min_bound has to be a positive numeric value.")

    in_data = VecVecDouble()

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    for d in data:
        in_data.push_back(d)

    min_bounds = VecPair()
    max_bounds = VecPair()

    min_bounds.push_back((min_bound, list(bound_variable)))

    in_init_regions = VecInt(list(init_regions))

    cluster_ids = gda_maxp_tabu(
        w.gda_w, in_data, scale_method, iterations, tabu_length, conv_tabu,
        min_bounds, max_bounds, in_init_regions, distance_method, random_seed, cpu_threads
    )

    return calculate_clustering_statistics(cluster_ids, in_data, w.num_obs)
