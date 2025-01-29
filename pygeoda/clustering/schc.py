from pygeoda.clustering.utils import calculate_clustering_statistics
from ..libgeoda import VecVecDouble
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
        bound_variable (tuple or pandas.core.series.Series, optional): A numeric vector of selected bounding variable
        min_bound (float, optional): a minimum value that the sum value of bounding variable int each cluster should be greater than 
        scale_method (str, optional): One of the scaling methods {'raw', 'standardize', 'demean', 'mad', 'range_standardize', 'range_adjust'} to apply on input data. Default is 'standardize' (Z-score normalization).
        distance_method (str, optional): {"euclidean", "manhattan"} the distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"

    Returns:
        dict: A dict with keys {"Clusters", "TotalSS", "Within-clusterSS", "TotalWithin-clusterSS", "Ratio"}
    '''

    min_bound = 0 if 'min_bound' not in kwargs else kwargs['min_bound']
    bound_variable = [] if 'bound_variable' not in kwargs else kwargs['bound_variable']
    scale_method = "standardize" if "scale_method" not in kwargs else kwargs['scale_method']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 

    if linkage_method not in ["single", "complete", "average", "ward"]:
        raise ValueError('The method has to be one of {"single", "complete", "average", "ward"}')

    # check if bound_variable is pandas.core.series.Series, if so, convert to list
    if type(bound_variable).__name__ == "Series":
        bound_variable = bound_variable.values.tolist()
        
    # if bound_variable is not empty, check if it has the same length as the number of observations
    if len(bound_variable) > 0 and len(bound_variable) != w.num_obs:
        raise ValueError("The bound_variable has to be a list of numeric values, e.g. a column of input table.")
    
    # check if min_bound is available when bound_variable is not empty
    if len(bound_variable) > 0 and min_bound == 0:
        raise ValueError("min_bound is required and greater than 0 when bound_variable is not empty.")

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    in_data = VecVecDouble()
    for d in data:
        in_data.push_back(d)
   
    cluster_ids = gda_schc(k, w.gda_w, in_data, scale_method, linkage_method, distance_method, bound_variable, min_bound)

    return calculate_clustering_statistics(cluster_ids, in_data, w.num_obs)