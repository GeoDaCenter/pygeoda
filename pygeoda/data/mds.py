from ..libgeoda import gda_mds

__author__ = "Hang Zhang <zhanghanggis@163.com>, "

def mds(data,k):
    """Multi dimensional scale analysis chart

    Note:
        Multidimensional Scaling or MDS is an alternative approach to portraying a multivariate data cloud in lower dimensions.7 MDS is based on the notion of distance between observation points in multiattribute space. A set of coordinates in two dimensions are found such that the distances between the resulting pairs of points are as close as possible to their pair-wise distances in multi-attribute space.
    
    Args:
        data (tuple): A 2d numeric list of selected variables
        k (int): The number of dimensions that mds returns. Value range [1,k: the number of selected variables]

    Returns:
        list: A 2d numeric list of mds results (top k components),which contains the position of each geographical unit in the rectangular coordinate system of the chart
            e.g. [(-1,3.4,5,-7.32...X),(-2,3,-4,1,5,4...Y)]
    """
    if data is None:
        raise("The data from selected variable is empty.")
        
    return gda_mds(data,k)