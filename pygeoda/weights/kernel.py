__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import gda_distance_weights, gda_knn_weights
from .weight import Weight

def kernel_weights(geoda_obj, bandwidth, kernel, **kwargs):
    '''Distance-based Kernel Spatial Weights
    Create a kernel weights by specifying a bandwidth and a kernel method

    Args:
        geoda_obj (geoda): An instance of geoda class. 
        bandwidth (float): A float value represents the distance of bandwidth used in kernel function.
            For example, one can use the pygeoda.min_distthreshold() to get a distance that 
            guarantees that every observation has at least 1 neighbor.
        kernel (str): A string value, which has to be one of {'triangular', 'uniform', 'epanechnikov', 'quartic', 'gaussian'}
        use_kernel_diagonals (bool, optional):  A bool flag indicates whether or not the lower order neighbors should be 
            included in the weights structure. Defaults to False.
        is_inverse (bool, optional):  A bool flag indicates whether or not to apply inverse on distance value. Defaults to False.
        power (float, optional): The power (or exponent) of a number indicates how many times to use the number in a multiplication.
        is_arc (bool, optional): A bool flag indicates if compute arc distance or Euclidean distance. Defaults to False (Euclidean distance) 
        is_mile (bool, optional): A bool flag indicates if the distance unit is mile or km. Defaults to True (mile).

    Returns:
        Weight: An instance of Weight class 
    '''
    if kernel not in ['triangular', 'uniform', 'epanechnikov', 'quartic', 'gaussian']:
        raise("The parameter 'kernel' has to be one of {'triangular', 'uniform', 'epanechnikov', 'quartic', 'gaussian'}")
    
    use_kernel_diagonals = False if 'use_kernel_diagonals' not in kwargs else kwargs['use_kernel_diagonals']
    is_arc = False if 'is_arc' not in kwargs else kwargs['is_arc']
    is_mile = True if 'is_mile' not in kwargs else kwargs['is_mile']
    power = 1.0 if 'power' not in kwargs else kwargs['power']
    is_inverse = False if 'is_inverse' not in kwargs else kwargs['is_inverse']

    poly_id = ""
    
    gda_w = gda_distance_weights(geoda_obj.gda, bandwidth, poly_id, power, is_inverse, is_arc, is_mile, kernel, use_kernel_diagonals)

    return Weight(gda_w)


def kernel_knn_weights(geoda_obj, k, kernel, **kwargs):
    '''K-NN Kernel Spatial Weights
    Create a kernel weights by specifying k-nearest neighbors and a kernel method

    Args:
        geoda_obj (geoda): An instance of geoda class. 
        k (int): a positive integer number for k-nearest neighbors
        kernel (str): A string value, which has to be one of {'triangular', 'uniform', 'epanechnikov', 'quartic', 'gaussian'}
        Adaptive_bandwidth (bool, optional): True(default) or False: True - use adaptive bandwidth calculated using distance of k-nearest neithbors, False - use max distance of all observation to their k-nearest neighbors
        use_kernel_diagonals (bool, optional):  A bool flag indicates whether or not the lower order neighbors should be 
            included in the weights structure. Defaults to False.
        is_inverse (bool, optional):  A bool flag indicates whether or not to apply inverse on distance value. Defaults to False.
        power (float, optional): The power (or exponent) of a number indicates how many times to use the number in a multiplication.
        is_arc (bool, optional): A bool flag indicates if compute arc distance or Euclidean distance. Defaults to False (Euclidean distance) 
        is_mile (bool, optional): A bool flag indicates if the distance unit is mile or km. Defaults to True (mile).

    Returns:
        Weight: An instance of Weight class 
    '''
    if kernel not in ['triangular', 'uniform', 'epanechnikov', 'quartic', 'gaussian']:
        raise("The parameter 'kernel' has to be one of 'triangular', 'uniform', 'epanechnikov', 'quartic', 'gaussian'")

    adaptive_bandwidth = True if 'adaptive_bandwidth' not in kwargs else kwargs['adaptive_bandwidth']
    use_kernel_diagonals = False if 'use_kernel_diagonals' not in kwargs else kwargs['use_kernel_diagonals']
    power = 1.0 if 'power' not in kwargs else kwargs['power']
    is_inverse = False if 'is_inverse' not in kwargs else kwargs['is_inverse']
    is_arc = False if 'is_arc' not in kwargs else kwargs['is_arc']
    is_mile = True if 'is_mile' not in kwargs else kwargs['is_mile']
    bandwidth = 0
    polyid = ""
    
    gda_w = gda_knn_weights(geoda_obj.gda, k, power, is_inverse, is_arc, is_mile, kernel, bandwidth, adaptive_bandwidth, use_kernel_diagonals, polyid)

    return Weight(gda_w)