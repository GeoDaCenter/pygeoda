__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import VecVecDouble, VecPair, VecDouble, VecInt, Pair
from ..libgeoda import gda_azp_greedy, gda_azp_sa, gda_azp_tabu

'''
Changes:
1/20/2021 Add azp_greedy, _sa, azp_tabu
'''

def azp_greedy(p, w, data, bound_vals, min_bound, **kwargs):
    ''' A greedy algorithm to solve the AZP problem 
    
    Note: 
        The automatic zoning procedure (AZP) was initially outlined in Openshaw (1977) as a way to address some of the consequences of the modifiable areal unit problem (MAUP). In essence, it consists of a heuristic to find the best set of combinations of contiguous spatial units into p regions, minimizing the within sum of squares as a criterion of homogeneity. The number of regions needs to be specified beforehand.

    Arguments:
        p (int): The number of spatially constrained clusters
        w (Weight): an instance of Weight class
        data (tuple):   A list of numeric vectors of selected variable
        bound_vals (tuple): A numeric vector of selected bounding variable
        min_bound (float): A minimum value that the sum value of bounding variable int each cluster should be greater than
        inits (int, optional): The number of construction re-runs, which is for ARiSeL "automatic regionalization with initial seed location"
        init_regions (tuple, optional): The initial regions that the local search starts with. Default is empty. means the local search starts with a random process to "grow" clusters
        distance_method (str, optional):  The distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int, optional): The seed for random number generator. Defaults to 123456789. It is the same as GeoDa software
        cpu_threads (int, optional): The number of cpu threads used for parallel computation

    Returns:
        list: A list of numeric vectors represents a group of clusters
    '''
    
    inits = 0 if 'inits' not in kwargs else kwargs['inits']
    init_regions = [] if 'init_regions' not in kwargs else kwargs['init_regions']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']

    if w.num_obs < 1:
        raise ValueError("The weights is not valid.")

    if p < 1 or p > w.num_obs:
        raise ValueError("The number of clusters should be a positive integer.")

    if len(data) < 1:
        raise ValueError("The data from selected variable is empty.")

    if len(bound_vals) != w.num_obs:
        raise ValueError("The bound_vals has to be a list of numeric values, e.g. a column of input table.")

    if min_bound <= 0:
        raise ValueError("The min_bound has to be a positive numeric value.")
    
    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)

    min_bounds = VecPair()
    max_bounds = VecPair()

    min_bounds.push_back((min_bound, bound_vals))

    in_init_regions = VecInt(init_regions)

    return gda_azp_greedy(p, w.gda_w, in_data, inits, min_bounds, max_bounds, in_init_regions, distance_method, random_seed)

def azp_sa(p, w, data, bound_vals, min_bound, cooling_rate=0.85, **kwargs):
    ''' A simulated annealing algorithm to solve the AZP problem 
    
    Note: 
        The automatic zoning procedure (AZP) was initially outlined in Openshaw (1977) as a way to address some of the consequences of the modifiable areal unit problem (MAUP). In essence, it consists of a heuristic to find the best set of combinations of contiguous spatial units into p regions, minimizing the within sum of squares as a criterion of homogeneity. The number of regions needs to be specified beforehand.
        
    Arguments:
        p (int): The number of spatially constrained clusters
        w (Weight): an instance of Weight class
        data (tuple):   A list of numeric vectors of selected variable
        bound_vals (tuple): A numeric vector of selected bounding variable
        min_bound (float): A minimum value that the sum value of bounding variable int each cluster should be greater than
        cooling_rate (float): The cooling rate of a simulated annealing algorithm. Defaults to 0.85
        sa_maxit (int): The number of iterations of simulated annealing. Defaults to 1
        inits (int, optional): The number of construction re-runs, which is for ARiSeL "automatic regionalization with initial seed location"
        init_regions (tuple, optional): The initial regions that the local search starts with. Default is empty. means the local search starts with a random process to "grow" clusters
        distance_method (str, optional):  The distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int, optional): The seed for random number generator. Defaults to 123456789. It is the same as GeoDa software
        cpu_threads (int, optional): The number of cpu threads used for parallel computation

    Returns:
        list: A list of numeric vectors represents a group of clusters
    '''

    sa_maxit = 1 if 'sa_maxit'  not in kwargs else kwargs['sa_maxit']
    inits = 0 if 'inits' not in kwargs else kwargs['inits']
    init_regions = [] if 'init_regions' not in kwargs else kwargs['init_regions']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']

    if cooling_rate <=0 or cooling_rate >=1:
        raise ValueError("Cooling rate should be in range (0,1).")

    if w.num_obs < 1:
        raise ValueError("The weights is not valid.")

    if p < 1 or p > w.num_obs:
        raise ValueError("The number of clusters should be a positive integer.")

    if len(data) < 1:
        raise ValueError("The data from selected variable is empty.")

    if len(bound_vals) != w.num_obs:
        raise ValueError("The bound_vals has to be a list of numeric values, e.g. a column of input table.")

    if min_bound <= 0:
        raise ValueError("The min_bound has to be a positive numeric value.")
    
    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)

    min_bounds = VecPair()
    max_bounds = VecPair()

    min_bounds.push_back((min_bound, bound_vals))

    in_init_regions = VecInt(init_regions)

    return gda_azp_sa(p, w.gda_w, in_data, inits, cooling_rate, sa_maxit, min_bounds, max_bounds, in_init_regions, distance_method, random_seed)

def azp_tabu(p, w, data, bound_vals, min_bound, tabu_length=10, **kwargs):
    ''' A tabu-search algorithm to solve the AZP problem 
    
    Note: 
        The automatic zoning procedure (AZP) was initially outlined in Openshaw (1977) as a way to address some of the consequences of the modifiable areal unit problem (MAUP). In essence, it consists of a heuristic to find the best set of combinations of contiguous spatial units into p regions, minimizing the within sum of squares as a criterion of homogeneity. The number of regions needs to be specified beforehand.
        
    Arguments:
        p (int): The number of spatially constrained clusters
        w (Weight): an instance of Weight class
        data (tuple):   A list of numeric vectors of selected variable
        bound_vals (tuple): A numeric vector of selected bounding variable
        min_bound (float): A minimum value that the sum value of bounding variable int each cluster should be greater than
        tabu_length (int): The length of a tabu search heuristic of tabu algorithm. Defaults to 10.
        conv_tabu (int, optional): The number of non-improving moves. Defaults to 10.
        inits (int, optional): The number of construction re-runs, which is for ARiSeL "automatic regionalization with initial seed location"
        init_regions (tuple, optional): The initial regions that the local search starts with. Default is empty. means the local search starts with a random process to "grow" clusters
        distance_method (str, optional):  The distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int, optional): The seed for random number generator. Defaults to 123456789. It is the same as GeoDa software
        cpu_threads (int, optional): The number of cpu threads used for parallel computation

    Returns:
        list: A list of numeric vectors represents a group of clusters
    '''
    
    conv_tabu = 10 if 'conv_tabu' not in kwargs else kwargs['conv_tabu']
    inits = 0 if 'inits' not in kwargs else kwargs['inits']
    init_regions = [] if 'init_regions' not in kwargs else kwargs['init_regions']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']

    if w.num_obs < 1:
        raise ValueError("The weights is not valid.")
    
    if p < 1 or p > w.num_obs:
        raise ValueError("The number of clusters should be a positive integer.")

    if len(data) < 1:
        raise ValueError("The data from selected variable is empty.")

    if len(bound_vals) != w.num_obs:
        raise ValueError("The bound_vals has to be a list of numeric values, e.g. a column of input table.")

    if min_bound <= 0:
        raise ValueError("The min_bound has to be a positive numeric value.")
    
    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)

    min_bounds = VecPair()
    max_bounds = VecPair()

    min_bounds.push_back((min_bound, bound_vals))

    in_init_regions = VecInt(init_regions)

    return gda_azp_tabu(p, w.gda_w, in_data, inits, tabu_length, conv_tabu, min_bounds, max_bounds, in_init_regions, distance_method, random_seed)