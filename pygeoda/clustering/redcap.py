from ..libgeoda import VecVecDouble
from ..libgeoda import gda_redcap

__author__ = "Xun Li <lixun910@gmail.com>, "

def redcap(k, w, data, method,  bound_vals=[], min_bound=0, distance_method='euclidean', random_seed=123456789):
    ''' Regionalization with dynamically constrained agglomerative clustering and partitioning

    Like SKATER, REDCAP starts from building a spanning tree with 3 different ways (single-linkage, average-linkage, and the complete-linkage).
    The single-linkage way leads to build a minimum spanning tree. Then, REDCAP provides 2 different ways to prune the tree (First-order and Full-order):
    Therefore, in GeoDa and pygeoda, the following methods are provided:

    * First-order and Single-linkage
    * Full-order and Complete-linkage
    * Full-order and Average-linkage
    * Full-order and Single-linkage

    Arguments:
        k (int): number of clusters
        w (Weight): An instance of Weight class
        data (tuple):  A 2d numeric list of selected variable
        method (str): {"firstorder-singlelinkage", "fullorder-completelinkage", "fullorder-averagelinkage","fullorder-singlelinkage"}
        bound_vals (tuple, optional): 1d tuple of selected bounding variable
        min_bound (float, optional): a minimum value that the sum value of bounding variable int each cluster should be greater than 
        distance_method (str, optional): {"euclidean", "manhattan"} the distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int,optional): the seed for random number generator. Defaults to 123456789. 

    Returns:
        tuple: a 2d tuple represents a group of clusters
    '''
    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)
    return gda_redcap(k, w.gda_w, in_data, method, distance_method, bound_vals, min_bound, random_seed)
