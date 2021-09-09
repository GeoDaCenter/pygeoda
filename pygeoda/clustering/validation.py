__author__ = "Xun Li <lixun910@gmail.com>"

from ..libgeoda import gda_spatialvalidation, gda_all_joincount_ratio, gda_makespatial

class Diameter:
    """Diameter Measure

    Attributes:
        steps (int): the longest shortest distance between any pairs
        ratio (float): the ratio of steps over the number of elements in the cluster
    """
    def __init__(self, diam):
        """Constructor of Diameter

        Args:
            diam (Object): An object/pointer of libgeoda Diameter class
        """
        self.steps = diam.steps
        self.ratio = diam.ratio

    def __repr__(self):
        info = "{"
        info += "'Steps': {0}, ".format(self.steps)
        info += "'Ratio': {0}".format(self.ratio)
        info += "}"
        return info

class Compactness:
    """Compactness Measure

    Attributes:
        area (float): the area of a cluster. If points, the convex hull is used to compute
            the area.
        perimeter (float): the perimeter of a cluster. If points, the convex hull is used
            to compute the perimeter
        isoperimeter_quotient (float): (4 * pi * area) / (perimeter^2)
    """
    def __init__(self, comp):
        """Constructor of Compactness

        Args:
            comp (Object): An object/pointer of libgeoda Compactness class
        """
        self.area = comp.area
        self.perimeter = comp.perimeter
        self.isoperimeter_quotient = comp.isoperimeter_quotient

    def __repr__(self):
        info = "{"
        info += "'Area': {0}, ".format(self.area)
        info += "'Perimeter': {0}, ".format(self.perimeter)
        info += "'Isoperimeter quotient': {0}".format(self.isoperimeter_quotient)
        info += "}"
        return info

class JoinCountRatio:
    """Join Count Ratio

    Join count ratio is the join counts, the number of times a category is surrounded 
    by neighbors of the same category, over the total number of neighbors after converting
    each category to a dummy variable.

    Attributes:
        n (int): the number of elements in a cluster
        neighbors (int): the total number of neighbors of elements in a cluster
        join_count (int): the total join count of elements in a cluster
        ratio (float): the ratio of total join count over total neighbors
    """
    def __init__(self, jcr):
        """Constructor of JoinCountRatio

        Args:
            jcr (Object): An object/pointer of libgeoda JoinCountRatio class
        """
        self.n = jcr.n
        self.neighbors = jcr.totalNeighbors
        self.join_count = jcr.totalJoinCount
        self.ratio = jcr.ratio

    def __repr__(self):
        info = "{"
        info += "'n': {0}, ".format(self.n)
        info += "'Neighbors': {0}, ".format(self.neighbors)
        info += "'Join Count': {0}, ".format(self.join_count)
        info += "'Ratio': {0}".format(self.ratio)
        info += "}"
        return info

class Fragmentation:
    """
    Fragmentation measure of spatial validation

    Attributes: 
        n (int): number of elements in clusters
        entropy (float): entropy measure for fraction of observations in each cluster
        std_entropy (float): standardized entropy measure
        simpson (float): simpson's index is a measure of diversity in each cluster
        std_simpson (float): standardized simpson measure
    """
    def __init__(self, gda_frag):
        """
        Constructor of Fragmentation class.

        Args:
            gda_frag (Object): A libgeoda Fragmentation instance
        """
        self.n = gda_frag.n
        self.entropy = gda_frag.entropy
        self.std_entropy = gda_frag.std_entropy
        self.simpson = gda_frag.simpson
        self.std_simpson = gda_frag.std_simpson

    def __repr__(self):
        info = "{"
        info += "'Entropy': {0}, ".format(self.entropy)
        info += "'Entropy*': {0}, ".format(self.std_entropy)
        info += "'Simpson': {0}, ".format(self.simpson)
        info += "'Simpson*': {0}".format(self.std_simpson)
        info += "}"
        return info

class ValidationResult:
    """
    Spatial Validation Result

    Attributes:
        spatially_constrained (bool): indicate if the clusters are 
        n (int): number of clusters
        joincount_ratio (JoinCountRatio): a list of JoinCountRatio objects
        fragmantation (Fragmentation): an object of Fragmentation
        cluster_fragmentation (Fragmentation): a list of Fragmentation objects, or None for spatially constrained clusters
        compactness (Compactness): a list of Compactness objects, or None for non-spatially constrained clusters
        diameter (Diameter): a list of Diameter objects, or None for non-spatially constrained clusters
    """
    def __init__(self, gda_validation):
        """
        Constructor of ValidationResult class.

        Args:
            gda_validation (Object): A libgeoda validation instance
        """
        self.spatially_constrained = gda_validation.spatially_constrained
        
        self.fragmentation = Fragmentation(gda_validation.fragmentation)
        self.n = self.fragmentation.n
        self.joincount_ratio = []
        
        for i in range(self.n):
            self.joincount_ratio.append(JoinCountRatio(gda_validation.joincount_ratio[i]))

        self.all_joincount_ratio = JoinCountRatio(gda_all_joincount_ratio(gda_validation.joincount_ratio))

        if self.spatially_constrained:
            self.cluster_fragmentation = None
            self.compactness = []
            self.diameter = []
            for i in range(self.n):
                self.compactness.append(Compactness(gda_validation.cluster_compactness[i]))
                self.diameter.append(Diameter(gda_validation.cluster_diameter[i]))
        else:
            self.cluster_fragmentation = []
            for i in range(self.n):
                self.cluster_fragmentation.append(Fragmentation(gda_validation.cluster_fragmentation[i]))
            self.compactness = None
            self.diameter = None

    def __repr__(self):
        info = "{"
        info += "'Spatially Constrained': {0}\n".format(self.spatially_constrained)
        info += "'Join Count Ratio': {0}\n".format(self.joincount_ratio)
        info += "'All Join Count Ratio': {0}\n".format(self.all_joincount_ratio)
        info += "'Fragmentation': {0}\n".format(self.fragmentation)
        info += "'Cluster Fragmentation': {0}\n".format(self.cluster_fragmentation)
        info += "'Compactness': {0}\n".format(self.compactness)
        info += "'Diameter': {0}\n".format(self.diameter)
        info += "}"
        return info

def spatial_validation(geoda_obj, clusters, w):
    """Spatial Validation
    Spatial validation provides a collection of validation measures including
    (1) fragmentations (entropy, simpson), (2) join count ratio, (3) compactness
    - isoperimeter quotient and (4) diameter.

    Args:
        geoda_obj (geoda): An instance of Geoda object
        clusters (list): A cluster classification variable (categorical values
        from a dataframe or values returned from cluster functions)
        w (Weight): An instance of Weight class.

    Returns:
        ValidationResult: An instance of ValidationResult including fragmentation, join count ratio,
                compactness, and diameter
    """
    if w is None:
        raise ValueError("Weights is None.")

    if w.num_obs != len(clusters):
        raise ValueError("The size of data doesnt not match the number of observations.")

    result = gda_spatialvalidation(geoda_obj.gda, clusters, w.gda_w)

    return ValidationResult(result)

def make_spatial(clusters, w):
    """Make spatially constrained clusters
    Make spatially constrained clusters from non-spatially constrained clusters

    Args:
        clusters (list): A cluster classification variable (categorical values
        from a dataframe or values returned from cluster functions, e.g. kmeans)
        w (Weight): An instance of Weight class.

    Returns:
        result (list): A new categorical values represent spatially constrained clusters
    """
    if w is None:
        raise ValueError("Weights is None.")

    if w.num_obs != len(clusters):
        raise ValueError("The size of data doesnt not match the number of observations.")

    result = gda_makespatial(list(clusters), w.gda_w)

    return result