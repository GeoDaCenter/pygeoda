__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import VecVecDouble, VecPair, VecDouble, VecInt
from ..libgeoda import gda_maxp_greedy, gda_maxp_sa, gda_maxp_tabu

def maxp_greedy(w, data, bound_vals, min_bound, **kwargs):
    ''' An algorithm to solve the max-p-region problem 
    
    Note: 
        The max-p-region problem is a special case of constrained clustering where a finite number of geographical areas, n, are aggregated into the maximum number of regions, p, such that each region satisfies the following const raints: 1. The areas within a region must be geographically connected.
        
    Arguments:
        w (Weight): an instance of Weight class
        data (tuple):   A list of numeric vectors of selected variable
        bound_vals (tuple): A numeric vector of selected bounding variable
        min_bound (float): A minimum value that the sum value of bounding variable int each cluster should be greater than
        iterations (int, optional): The number of iterations of greedy algorithm. Defaults to 99.
        init_regions (tuple, optional): The initial regions that the local search starts with. Default is empty. means the local search starts with a random process to "grow" clusters
        distance_method (str, optional):  The distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int, optional): The seed for random number generator. Defaults to 123456789. It is the same as GeoDa software
        cpu_threads (int, optional): The number of cpu threads used for parallel computation

    Returns:
        list: A list of numeric vectors represents a group of clusters
    '''
    
    iterations = 99 if 'iterations' not in kwargs else kwargs['iterations']
    init_regions = [] if 'init_regions' not in kwargs else kwargs['init_regions']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']
    cpu_threads = 6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']

    if w.num_obs < 1:
        raise ValueError("The weights is not valid.")

    if len(data) < 1:
        raise ValueError("The data from selected variable is empty.")

    if len(bound_vals) != w.num_obs:
        raise ValueError("The bound_vals has to be a list of numeric values, e.g. a column of input table.")

    if min_bound <= 0:
        raise ValueError("The min_bound has to be a positive numeric value.")
    
    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)

    in_bound_vals = VecDouble(bound_vals)
    min_bounds = VecPair((min_bound, in_bound_vals))
    max_bounds = VecPair()

    in_init_regions = VecInt(init_regions)

    return gda_maxp_greedy(w.gda_w, in_data, iterations, min_bounds, max_bounds, in_init_regions, distance_method, random_seed, cpu_threads)