from .libgeoda import gda_betweensumofsquare 
from .libgeoda import gda_totalsumofsquare 
from .libgeoda import gda_withinsumofsquare
from .libgeoda import gda_sumofsquares as ss

__author__ = "Xun Li <lixun910@gmail.com>"
__all__ = ['between_sumofsquare', 'within_sumofsquare', 'total_sumofsquare']

def between_sumofsquare(clusters, data):
    '''Compute between sum of square value of a group of clusters

    Arguments:
        clusters (tuple): 2d tuple which returns from spatial clustering methods, e.g. skater()
        data (tuple): 2d tuple which is used in spatial clustering methods, e.g. skater(k, w, data)

    Return:
        (float): between sum of square value
    '''
    return gda_betweensumofsquare(clusters, data)


def total_sumofsquare(data):
    '''Compute total sum of square value of a 2d tuple data 

    Arguments:
        data (tuple): 2d tuple which is used in spatial clustering methods, e.g. skater(k, w, data)

    Return:
        (float): total sum of square value
    '''
    return gda_totalsumofsquare(data)

def within_sumofsquare(clusters, data):
    '''Compute within sum of square value of a group of clusters

    Arguments:
        clusters (tuple): 2d tuple which returns from spatial clustering methods, e.g. skater()
        data (tuple): 2d tuple which is used in spatial clustering methods, e.g. skater(k, w, data)

    Return:
        (float): within sum of square value
    '''
    return gda_totalsumofsquare(data)