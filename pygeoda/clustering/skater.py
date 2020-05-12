__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import VecVecDouble
from ..libgeoda import gda_skater

def skater(k, w, data, bound_vals=[], min_bound=-1, distance_method='euclidean', random_seed=123456789):
    ''' Spatial C(K)luster Analysis by Tree Edge Removal

    SKATER forms clusters by spatially partitioning data that has similar values for features of interest.

    Arguments:
        k (int): number of clusters
        w (Weight): an instance of Weight class
        data (tuple):  2d numeric tuple of selected variable
        bound_vals (tuple, optional): 1d tuple of selected bounding variable
        min_bound (float, optional): a minimum value that the sum value of bounding variable int each cluster should be greater than 
        distance_method (str, optional): {"euclidean", "manhattan"} the distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int,optional): the seed for random number generator. Defaults to 123456789. 

    Return: 
        tuple: a 2d tuple represents a group of clusters
    '''
    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)
    return gda_skater(k, w.gda_w, in_data, distance_method, bound_vals, min_bound, random_seed)