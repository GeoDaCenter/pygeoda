__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import gda_distance_weights, gda_min_distthreshold, gda_knn_weights
from .weight import Weight

def distance_weights(geoda_obj, dist_thres, **kwargs):
    '''Distance-based Spatial Weights
    Create a distance-based weights

    Args:
        geoda_obj (geoda): An instance of geoda class. 
        dist_thres (float): A positive numeric value of distance threshold used to find neighbors.
            For example, one can use the pygeoda.min_distthreshold() to get a distance that 
            guarantees that every observation has at least 1 neighbor.
        power (float, optional): The power (or exponent) of a number indicates how many times to use the number in a multiplication.
        is_inverse (bool, optional):  A bool flag indicates whether or not to apply inverse on distance value.
            Defaults to False.
        is_arc (bool, optional): A bool flag indicates if compute arc distance or Euclidean distance. Defaults to False (Euclidean distance) 
        is_mile (bool, optional): A bool flag indicates if the distance unit is mile or km. Defaults to True (mile).

    Returns:
        Weight: An instance of Weight class 
    '''
    power = 1.0 if 'power' not in kwargs else kwargs['power']
    is_inverse = False if 'is_inverse' not in kwargs else kwargs['is_inverse']
    is_arc = False if 'is_arc' not in kwargs else kwargs['is_arc']
    is_mile = True if 'is_mile' not in kwargs else kwargs['is_mile']

    poly_id = ""
    kernel = ""
    diagonal = False
    gda_w = gda_distance_weights(geoda_obj.gda, dist_thres, poly_id, power, is_inverse, is_arc, is_mile, kernel, diagonal)

    return Weight(gda_w)


def min_distthreshold(geoda_obj, is_arc=False, is_mile=True):
    '''Minimum Distance Threshold for Distance-based Weights
    Get minimum threshold of distance that makes sure each observation has at least one neighbor   

    Args:
        geoda_obj (geoda): An instance of geoda class. 
        is_arc (bool, optional): A bool flag indicates if compute arc distance or Euclidean distance. Defaults to False (Euclidean distance) 
        is_mile (bool, optional): A bool flag indicates if the distance unit is mile or km. Defaults to True (mile).

    Returns:
        thres (float): A float value of minimum threhold for distance based weights.
    '''
    return gda_min_distthreshold(geoda_obj.gda, is_arc, is_mile)

def knn_weights(geoda_obj, k, **kwargs):
    '''K-Nearest Neighbors-based Spatial Weights
    Create a k-nearest neighbors based spatial weights

    Args:
        geoda_obj (geoda): An instance of geoda class. 
        k (int): A positive integer number for k-nearest neighbors
        power (float, optional): The power (or exponent) of a number indicates how many times to use the number in a multiplication.
        is_inverse (bool, optional):  A bool flag indicates whether or not to apply inverse on distance value.
            Defaults to False.
        is_arc (bool, optional): A bool flag indicates if compute arc distance or Euclidean distance. Defaults to False (Euclidean distance) 
        is_mile (bool, optional): A bool flag indicates if the distance unit is mile or km. Defaults to True (mile).


    Returns:
        Weight: An instance of Weight class 
    '''
    power = 1.0 if 'power' not in kwargs else kwargs['power']
    is_inverse = False if 'is_inverse' not in kwargs else kwargs['is_inverse']
    is_arc = False if 'is_arc' not in kwargs else kwargs['is_arc']
    is_mile = True if 'is_mile' not in kwargs else kwargs['is_mile']
    
    # not used
    kernel = "" 
    bandwidth = 0 
    adaptive_bandwidth = False 
    use_kernel_diagnals = False 
    polyid = ""

    gda_w = gda_knn_weights(geoda_obj.gda, k, power, is_inverse, is_arc, is_mile, kernel, bandwidth, adaptive_bandwidth, use_kernel_diagnals, polyid)

    return Weight(gda_w)