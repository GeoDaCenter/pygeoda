from ..libgeoda import VecVecDouble, VecDouble
from ..libgeoda import gda_schc

__author__ = "Xun Li <lixun910@gmail.com>, "

def schc(k, w, data, linkage_method, **kwargs):
    ''' Spatially Constrained Hierarchical Clucstering (SCHC)

    Spatially constrained hierarchical clustering is a special form of constrained 
    clustering, where the constraint is based on contiguity (common borders). 
    The method builds up the clusters using agglomerative hierarchical clustering 
    methods: single linkage, complete linkage, average linkage and Ward's method 
    (a special form of centroid linkage). Meanwhile, it also maintains the spatial 
    contiguity when merging two clusters.

    Arguments:
        k (int): number of clusters
        w (Weight): An instance of Weight class
        data (tuple): A list of numeric vectors of selected variable
        linkage_method (str): The method of agglomerative hierarchical clustering: {"single", "complete", "average","ward"}. Defaults to "ward".
        bound_vals (tuple, optional): A numeric vector of selected bounding variable
        min_bound (float, optional): a minimum value that the sum value of bounding variable int each cluster should be greater than 
        distance_method (str, optional): {"euclidean", "manhattan"} the distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"

    Returns:
        list: A list of numeric vectors represents a group of clusters
    '''

    min_bound = 0 if 'min_bound' not in kwargs else kwargs['min_bound']
    bound_vals = [] if 'bound_vals' not in kwargs else kwargs['bound_vals']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 

    if linkage_method not in ["single", "complete", "average","ward"]:
        raise ValueError('The method has to be one of {"single", "complete", "average","ward"}')

    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)
    
    #in_bound_vals = VecDouble(bound_vals)

    return gda_schc(k, w.gda_w, in_data, linkage_method, distance_method, bound_vals, min_bound)
