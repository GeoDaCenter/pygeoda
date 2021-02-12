from ..libgeoda import gda_hinge15breaks
from ..libgeoda import gda_hinge30breaks
from ..libgeoda import gda_naturalbreaks
from ..libgeoda import gda_quantilebreaks
from ..libgeoda import gda_percentilebreaks
from ..libgeoda import gda_stddevbreaks
from ..libgeoda import VecBool

__author__ = "Xun Li <lixun910@gmail.com>, Hang Zhang <zhanghanggis@163.com>, "

def hinge15_breaks(data,**kwargs):
    """(Box) Hinge15 Breaks
    
    Hinge15 breaks data into 6 groups like box plot groups (Lower outlier, < 25%, 25-50%, 50-75%, >75%, Upper outlier) with hinge=1.5

    Args:
        data (tuple): A tuple with values of a selected variable
    
    Returns:
        list: A numeric list of break values
    """
    if data is None:
        raise("The data from selected variable is empty.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']

    return gda_hinge15breaks(data, undefs)

def hinge30_breaks(data,**kwargs):
    """(Box) Hinge30 Breaks

    Hinge30 breaks data into 6 groups like box plot groups (Lower outlier, < 25%, 25-50%, 50-75%, >75%, Upper outlier) with hinge=3.0

    Args:
        data (tuple): A tuple with values of a selected variable
    
    Returns:
        list: A numeric list of break values
    """
    if data is None:
        raise("The data from selected variable is empty.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']

    return gda_hinge30breaks(data, undefs)

def natural_breaks(k,data,**kwargs):
    """Natural Breaks (Jenks)
    
    Natural Breaks group data whose boundaries are set where there are relatively big differences.

    Args:
        k (int): Number of breaks
        data (tuple): A tuple with values of a selected variable
    
    Returns:
        list: A numeric list of break values
    """
    if k is None or k < 2:
        raise("The value of K needs to be greater than or equal to 2 ")

    if data is None:
        raise("The data from selected variable is empty.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    return gda_naturalbreaks(k, data, undefs)

def quantile_breaks(k,data,**kwargs):
    """Quantile breaks

    Quantile breaks data into groups that each have the same number of observations

    Args:
        k (int): Number of breaks
        data (tuple): A tuple with values of a selected variable
    
    Returns:
        list: A numeric list of break values
    """
    if k is None or k < 2:
        raise("The value of K needs to be greater than or equal to 2 ")

    if data is None:
        raise("The data from selected variable is empty.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    return gda_quantilebreaks(k, data, undefs)

def percentile_breaks(data,**kwargs):
    """Percentile breaks

    Note:
        The percentile breaks divides the data to  six ranges, the lowest 1%, 1-10%, 10-50%, 50-90%, 90-99% and the top 1%, returning the range boundaries as a breakpoint list. 

    Args:
        data (tuple): A tuple with values of a selected variable
    
    Returns:
        list: A numeric list of break values
    """
    if data is None:
        raise("The data from selected variable is empty.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']
    return gda_percentilebreaks(data, undefs)

def stddev_breaks(data,**kwargs):
    """Standard deviation breaks

    Note:
        Standard deviation breaks calculate the number of standard deviational units of  the range from lowest to highest, returning a breakpoint list. 
    Args:
        data (tuple): A tuple with values of a selected variable
    
    Returns:
        list: A numeric list of break values
    """
    if data is None:
        raise("The data from selected variable is empty.")

    undefs = VecBool() if 'undefs' not in kwargs else kwargs['undefs']

    return gda_stddevbreaks(data, undefs)

