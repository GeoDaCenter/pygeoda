from ..libgeoda import gda_demean, gda_standardize, gda_standardize_mad

'''
1/19/2021: add demean, standardize, standardize_mad
'''
__author__ = "Xun Li <lixun910@gmail.com>, "

def demean(data):
    """Demean Standardization

    Note:
        The mean for each variable is subtracting from each observation resulting in mean zero.
    
    Args:
        data (list): An input data of multiple variables for median absolute deviation

    Returns:
        list: A data array
    """
    if data is None:
        raise ValueError("The data from selected variable is empty.")
        
    return gda_demean(data)


def standardize(data):
    """Standardization (Z)

    Note:
        Standarize data by transforming data to have zero mean and unit variance.

    Args:
        data (list): An input data of multiple variables for standardization

    Returns:
        list: A data array
    """
    if data is None:
        raise ValueError("The data from selected variable is empty.")
        
    return gda_standardize(data)

def mad(data):
    """Median Absolute Deviation

    Note:
        Compute the median absolute deviation, i.e., the (lo-/hi-) median of the absolute deviations from the median, and (by default) adjust by a factor for asymptotically normal consistency.

    Args:
        data (list): An input data of multiple variables for standardization

    Returns:
        list: A data array
    """
    if data is None:
        raise ValueError("The data from selected variable is empty.")
        
    return gda_standardize_mad(data)