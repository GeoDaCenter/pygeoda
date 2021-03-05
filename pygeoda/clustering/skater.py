__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import VecVecDouble, VecDouble
from ..libgeoda import gda_skater
from ..libgeoda import gda_betweensumofsquare, gda_totalsumofsquare, gda_withinsumofsquare, flat_2dclusters

def skater(k, w, data, **kwargs):
    ''' Spatial C(K)luster Analysis by Tree Edge Removal

    SKATER forms clusters by spatially partitioning data that has similar values for features of interest.

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

    Return: 
        dict: A dict with keys {"Clusters", "TotalSS", "Within-clusterSS", "TotalWithin-clusterSS", "Ratio"}

    '''
    min_bound = 0 if 'min_bound' not in kwargs else kwargs['min_bound']
    bound_variable = [] if 'bound_variable' not in kwargs else kwargs['bound_variable']
    scale_method = "standardize" if "scale_method" not in kwargs else kwargs['scale_method']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method'] 
    random_seed = 123456789 if 'random_seed' not in kwargs else kwargs['random_seed']
    cpu_threads = 6 if 'cpu_threads' not in kwargs else kwargs['cpu_threads']

    in_data = VecVecDouble()

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    for d in data:
        in_data.push_back(d)

    cluster_ids = gda_skater(k, w.gda_w, in_data, scale_method, distance_method, bound_variable, min_bound, random_seed, cpu_threads)

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