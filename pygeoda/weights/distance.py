__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import gda_distance_weights, gda_min_distthreshold, gda_knn_weights
from .weight import Weight

def distance(geoda_obj, dist_thres, **kwargs):
    '''Create a kernel weights with fixed bandwidth. 

    Args:
        geoda_obj (geoda): An instance of geoda class. 
        dist_thres (float): A positive numeric value of distance threshold used to find neighbors.
            For example, one can use the pygeoda.weights.min_threshold() to get a distance that 
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
    gda_w = gda_distance_weights(geoda_obj.gda, dist_thres, poly_id, power, is_inverse, is_arc, is_mile)

    return Weight(gda_w)


def min_threshold(geoda_obj, is_arc=False, is_mile=True):
    ''' find a minimum threshold for distance based weights. 
        
    This value guarantees that every observation has at least 1 neighbor.

    Args:
        geoda_obj (geoda): An instance of geoda class. 
        is_arc (bool, optional): A bool flag indicates if compute arc distance or Euclidean distance. Defaults to False (Euclidean distance) 
        is_mile (bool, optional): A bool flag indicates if the distance unit is mile or km. Defaults to True (mile).

    Returns:
        thres (float): A float value of minimum threhold for distance based weights.
    '''
    return gda_min_distthreshold(geoda_obj.gda, is_arc, is_mile)

def knn(geoda_obj, k, **kwargs):
    '''Create a K-Nearest Neighbors weights. 

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
    
    gda_w = gda_knn_weights(geoda_obj.gda, k, power, is_inverse, is_arc, is_mile)

    return Weight(gda_w)