__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import VecVecDouble
from ..libgeoda import gda_maxp

def maxp(w, data, bound_vals, min_bound, local_search, **kwargs):
    ''' An algorithm to solve the max-p-region problem 
    
    Note: 
        The max-p-region problem is a special case of constrained clustering where a finite number of geographical areas, n, are aggregated into the maximum number of regions, p, such that each region satisfies the following const raints: 1. The areas within a region must be geographically connected.
        
    Arguments:
        w (Weight): an instance of Weight class
        data (tuple):   A 2d numeric list of selected variable
        bound_vals (tuple): A 1-d vector of selected bounding variable
        min_bound (float): A minimum value that the sum value of bounding variable int each cluster should be greater than
        local_search (str): The name of the heurist algorithm to find a optimal solution. Default to "greedy". Options are "greedy", "tabu" and "sa" (simulated annealing)
        distance_method (str, optional):  The distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int,optional): The seed for random number generator. Defaults to 123456789. It is the same as GeoDa software
        initial (int, optional): The number of iterations of greedy algorithm. Defaults to 99.
        tabu_length (int): The length of a tabu search heuristic of tabu algorithm. Defaults to 95.
        cool_rate (float): The cooling rate of a simulated annealing algorithm. Defaults to 0.85
        init_seeds (tuple): The initial clusters that the local search starts with, e.g. one can assign the LISA cluster as the init_seeds for max-p method. Default is empty. means the local search starts with a random process to "grow" clusters

    Returns:
        tuple: a 2d tuple represents a group of clusters
    '''
    
    initial = 99 if 'initial' not in kwargs else kwargs['initial']
    tabu_length = 85 if 'tabu_length' not in kwargs else kwargs['tabu_length']
    cool_rate = 0.85 if 'cool_rate' not in kwargs else kwargs['cool_rate']
    init_seeds = [] if 'init_seeds' not in kwargs else kwargs['init_seeds']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']

    if w.num_obs < 1:
        raise "The weights is not valid."

    if len(data) < 1:
        raise "The data from selected variable is empty."

    if len(bound_vals) != w.num_obs:
        raise "The bound_vals has to be a list of numeric values, e.g. a column of input table."

    if min_bound <= 0:
        raise "The min_bound has to be a positive numeric value."
    
    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)

    return gda_maxp(w.gda_w, in_data, bound_vals, min_bound, local_search, initial, tabu_length, cool_rate, init_seeds, distance_method, random_seed)