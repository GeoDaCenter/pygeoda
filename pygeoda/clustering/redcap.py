from ..libgeoda import VecVecDouble, VecDouble
from ..libgeoda import gda_redcap

__author__ = "Xun Li <lixun910@gmail.com>, "

def redcap(k, w, data, method, **kwargs):
    ''' Regionalization with dynamically constrained agglomerative clustering and partitioning (REDCAP)

    REDCAP starts from building a spanning tree with 4 different ways (single-linkage, average-linkage, complete-linkage and Ward-linkage).
    Then, REDCAP provides 2 different ways to prune the tree (First-order and Full-order) to build clusters.
    In pygeoda, the following methods are provided:

    * First-order and Single-linkage
    * Full-order and Single-linkage
    * Full-order and Complete-linkage
    * Full-order and Average-linkage
    * Full-order and Ward-linkage

    Arguments:
        k (int): number of clusters
        w (Weight): An instance of Weight class
        data (tuple):   A list of numeric vectors of selected variable
        bound_vals (tuple): A numeric vector of selected bounding variable
        min_bound (float): A minimum value that the sum value of bounding variable int each cluster should be greater than
        min_bound (float, optional): a minimum value that the sum value of bounding variable int each cluster should be greater than 
        distance_method (str, optional): {"euclidean", "manhattan"} the distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int,optional): the seed for random number generator. Defaults to 123456789. 
        cpu_threads (int, optional): The number of cpu threads used for parallel computation

    Returns:
        list: A list of numeric vectors represents a group of clusters
    '''

    min_bound = 0 if 'min_bound' not in kwargs else kwargs['min_bound']
    bound_vals = [] if 'bound_vals' not in kwargs else kwargs['bound_vals']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']
    cpu_threads = 6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']

    if method not in ['firstorder-singlelinkage', 'fullorder-singlelinkage', 'fullorder-averagelinkage', 'fullorder-completelinkage', 'fullorder-wardlinkage']:
        raise ValueError('The method has to be one of {"firstorder-singlelinkage", "fullorder-completelinkage", "fullorder-averagelinkage","fullorder-singlelinkage", "fullorder-wardlinkage"}')

    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)
    
    #in_bound_vals = VecDouble(bound_vals)

    return gda_redcap(k, w.gda_w, in_data, method, distance_method, bound_vals, min_bound, random_seed, cpu_threads)
