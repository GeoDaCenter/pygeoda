from ..libgeoda import gda_hinge15breaks
from ..libgeoda import gda_hinge30breaks
from ..libgeoda import gda_naturalbreaks
from ..libgeoda import gda_quantilebreaks
from ..libgeoda import gda_percentilebreaks
from ..libgeoda import gda_stddevbreaks

__author__ = "Hang Zhang <zhanghanggis@163.com>, "

def hinge15_breaks(data,**kwargs):
    """Box map (Anselin 1994)

    Note:
        A box map (Anselin 1994) is the mapping counterpart of the idea behind a box plot. The point of departure is again a quantile map, more specifically, a quartile map. But the four categories are extended to six bins, to separately identify the lower and upper outliers The map menu has two entries for the box map, one for each option for the hinges (1.5 and 3.0), identical to what we had for the box plot. Here the hinges equal to 1.5   
    
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
    """Box map (Anselin 1994)

    Note:
        A box map (Anselin 1994) is the mapping counterpart of the idea behind a box plot. The point of departure is again a quantile map, more specifically, a quartile map. But the four categories are extended to six bins, to separately identify the lower and upper outliers The map menu has two entries for the box map, one for each option for the hinges (1.5 and 3.0), identical to what we had for the box plot. Here the hinges equal to 3.0 
    
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
    """Natural breaks map
    
    Note:
        A natural breaks map uses a nonlinear algorithm to group observations such that the within-group homogeneity is maximized, following the pathbreaking work of Fisher (1958) and Jenks (1977). In essence, this is a clustering algorithm in one dimension to determine the break points that yield groups with the largest internal similarity.
    
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
    """Quantile map

    Note:
        A quantile map is based on sorted values for a variable that are then grouped into bins that each have the same number of observations, the so-called quantiles. The number of bins corresponds to the particular quantile, e.g., five bins for a quintile map, or four bins for a quartile map, two of the most commonly used categories.

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
    """Percentile map

    Note:
        The percentile map is a variant of a quantile map that would start off with 100 categories. However, rather than having these 100 categories, the map classification is reduced to six ranges, the lowest 1%, 1-10%, 10-50%, 50-90%, 90-99% and the top 1%. 
    
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
    """Standard deviation map

    Note:
        In a standard deviation map, the variable under consideration is transformed to standard deviational units (with mean 0 and standard deviation 1). The number of categories in the classification depends on the range of values, i.e., how many standard deviational units cover the range from lowest to highest. It is also quite common that some categories do not contain any observations
    
    Args:
        data (tuple): A tuple with values of a selected variable
    
    Returns:
        list: A numeric list of break values
    """
    if data is None:
        raise("The data from selected variable is empty.")

    #undefs = [False]*len(data) if 'undefs' not in kwargs else kwargs['undefs']
    return gda_stddevbreaks(data)

