from ..libgeoda import gda_mds

__author__ = "Hang Zhang <zhanghanggis@163.com>, "

def mds(data,k):
    """Multi dimensional scale analysis

    Note:
        Multidimensional Scaling or MDS is an alternative approach to portraying a multivariate data cloud in lower dimensions.
    
    Args:
        data (tuple): A 2d numeric list of selected variables.
        k (int): The number of dimensions that mds returns. Value range [1,k: the number of selected variables].

    Returns:
        list: A 2d numeric list of mds results (top k components),which contains the position of each geographical unit in the rectangular coordinate system
            e.g. [(-1,3.4,5,-7.32...X),(-2,3,-4,1,5,4...Y)]
    """
    if data is None:
        raise("The data from selected variable is empty.")
        
    return gda_mds(data,k)