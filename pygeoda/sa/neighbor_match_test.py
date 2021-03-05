__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import VecBool, VecVecBool
from ..libgeoda import gda_neighbor_match_test, VecVecDouble
from .lisa import lisa
import math

'''
Changes:
1/21/2021 Update local_multigeary, local_geary for 0.0.6
'''

def neighbor_match_test(geoda_obj, data, k, **kwargs):
    '''Local Neighbor Match Test
    The local neighbor match test is to assess the extent of overlap between k-nearest neighbors in geographical space and k-nearest neighbors in multi-attribute space.

    Args:
        geoda_obj (geoda): An instance of geoda class. 
        data (list or dataframe):   A list of numeric vectors of selected variable or a data frame of selected variables e.g. guerry[['Crm_prs', 'Literacy']]
        k (int): A positive integer number for k-nearest neighbors searching.
        scale_method (str, optional): One of the scaling methods {'raw', 'standardize', 'demean', 'mad', 'range_standardize', 'range_adjust'} to apply on input data. Default is 'standardize' (Z-score normalization).
        distance_method (str, optional): The type of distance metrics used to measure the distance between input data. Options are {'euclidean', 'manhattan'}. Default is 'euclidean'.
        power (float, optional): The power (or exponent) of a number says how many times to use the number in a multiplication.
        is_inverse (bool, optional): FALSE (default) or TRUE, apply inverse on distance value.
        is_arc (bool, optional): FALSE (default) or TRUE, compute arc distance between two observations.
        is_mile (bool, optional) TRUE (default) or FALSE, convert distance unit from mile to km.

    Returns:
        dict: A dict with values for key "Cardinality" and "Probability".
    '''
    scale_method = 'standardize' if 'scale_method' not in kwargs else kwargs['scale_method']
    distance_method = 'euclidean' if 'distance_method' not in kwargs else kwargs['distance_method']
    power = 1.0 if 'power' not in kwargs else kwargs['power']
    is_inverse =  False if 'is_inverse' not in kwargs else kwargs['is_inverse']
    is_arc =  False if 'is_arc' not in kwargs else kwargs['is_arc']
    is_mile =  False if 'is_mile' not in kwargs else kwargs['is_mile']

    if type(data).__name__ == "DataFrame":
        data = data.values.transpose().tolist()

    result = gda_neighbor_match_test(geoda_obj.gda, k, power, is_inverse, is_arc, is_mile, data, scale_method, distance_method)
    card = result[0]
    prob = result[1]

    new_card = [int(i) for i in card]
    # check p value
    new_prob = [p if p >= 0 else math.nan for p in prob]

    return {
        "Cardinality": new_card,
        "Probability": new_prob
    }
