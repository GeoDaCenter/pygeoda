from ..libgeoda import gda_hinge15breaks
from ..libgeoda import gda_hinge30breaks
from ..libgeoda import gda_naturalbreaks
from ..libgeoda import gda_quantilebreaks
from ..libgeoda import gda_percentilebreaks
from ..libgeoda import gda_stddevbreaks

__author__ = "Hang Zhang <zhanghanggis@163.com>, "

def hinge15_breaks(data,**kwargs):
    """Hinge15 box breaks (Anselin 1994)

    Note:
        Hinge15 breaks calculate a list of breakpoints, including the top, bottom, median, and two quartiles of the data. Here the hinge is equal to 1.5.
    Args:
        data (tuple): A tuple with values of a selected variable
    
    Returns:
        list: A numeric list of break values
    """
    if data is None:
        raise("The data from selected variable is empty.")

    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_hinge15breaks(data)
def hinge30_breaks(data,**kwargs):
    """Hinge30 box break (Anselin 1994)

    Note:
        Hinge30_breaks calculate a list of breakpoints, including the top, bottom, median, and two quartiles of the data. Here the hinge is equal to 3.0.
    
    Args:
        data (tuple): A tuple with values of a selected variable
    
    Returns:
        list: A numeric list of break values
    """
    if data is None:
        raise("The data from selected variable is empty.")

    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_hinge30breaks(data)

def natural_breaks(k,data,**kwargs):
    """Natural breaks
    
    Note:
        Natural breaks Calculate of a breakpoint list based on the fracture principle of maximum similarity within a group.
    
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

    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_naturalbreaks(k,data)

def quantile_breaks(k,data,**kwargs):
    """Quantile breaks

    Note:
        The quantile breaks is based on sorted values for a variable that are then grouped into bins that each have the same number of observations, the so-called quantiles. Here the number of quantiles is variable.
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

    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_quantilebreaks(k,data)

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

    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_percentilebreaks(data)

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

    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_stddevbreaks(data)

