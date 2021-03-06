from ..libgeoda import VecVecDouble, VecDouble
from ..libgeoda import gda_redcap
from ..libgeoda import gda_betweensumofsquare, gda_totalsumofsquare, gda_withinsumofsquare, flat_2dclusters

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
        data (list or dataframe):   A list of numeric vectors of selected variable or a data frame of selected variables e.g. guerry[['Crm_prs', 'Literacy']]
        bound_variable (tuple, optional): A numeric vector of selected bounding variable
        min_bound (float, optional): a minimum value that the sum value of bounding variable int each cluster should be greater than 
        scale_method (str, optional): One of the scaling methods {'raw', 'standardize', 'demean', 'mad', 'range_standardize', 'range_adjust'} to apply on input data. Default is 'standardize' (Z-score normalization).
        distance_method (str, optional): {"euclidean", "manhattan"} the distance method used to compute the distance betwen observation i and j. Defaults to "euclidean". Options are "euclidean" and "manhattan"
        random_seed (int,optional): the seed for random number generator. Defaults to 123456789. 
        cpu_threads (int, optional): The number of cpu threads used for parallel computation

    Returns:
        dict: A dict with keys {"Clusters", "TotalSS", "Within-clusterSS", "TotalWithin-clusterSS", "Ratio"}
    '''

    min_bound = 0 if 'min_bound' not in kwargs else kwargs['min_bound']
    bound_variable = [] if 'bound_variable' not in kwargs else kwargs['bound_variable']
    scale_method = "standardize" if "scale_method" not in kwargs else kwargs['scale_method']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']
    cpu_threads = 6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']

    if method not in ['firstorder-singlelinkage', 'fullorder-singlelinkage', 'fullorder-averagelinkage', 'fullorder-completelinkage', 'fullorder-wardlinkage']:
        raise ValueError('The method has to be one of {"firstorder-singlelinkage", "fullorder-completelinkage", "fullorder-averagelinkage","fullorder-singlelinkage", "fullorder-wardlinkage"}')

    in_data = VecVecDouble()

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    for d in data:
        in_data.push_back(d)
    
    #in_bound_variable = VecDouble(bound_variable)

    cluster_ids = gda_redcap(k, w.gda_w, in_data, scale_method, method, distance_method, bound_variable, min_bound, random_seed, cpu_threads)

    between_ss = gda_betweensumofsquare(cluster_ids, in_data)
    total_ss = gda_totalsumofsquare(in_data)
    ratio = between_ss / total_ss
    within_ss = gda_withinsumofsquare(cluster_ids, in_data)

    return {
        "Total sum of squares" : total_ss,
        "Within-cluster sum of squares" : list(within_ss) + [0]*(len(cluster_ids) - len(within_ss)),
        "Total within-cluster sum of squares" : between_ss,
        "The ratio of between to total sum of squares" : ratio,
        "Clusters" : flat_2dclusters(w.num_obs, cluster_ids),
    }
