from ..libgeoda import GeoDa, VecInt, VecInt64, gda_load_gal, gda_load_gwt, gda_load_swm, GeoDaWeight

__author__ = "Xun Li <lixun910@gmail.com>"

class Weight:
    """
    GeoDa Weight class 
    """
    def __init__(self, gda_w):
        """
        Constructor of Weight class.

        Parameters
        ----------
        gda_w : Object
            A libgeoda GeoDaWeight pointer
        """
        self.gda_w = gda_w
        self.num_obs = gda_w.num_obs

    def is_symmetric(self):
        """
        Check if weights matrix is symmetric

        Parameters
        ----------
        None

        Returns
        -------
        is_symmetric : Boolean
            True means symmetric weights matrix, e.g. contiguity weights
            False means assymmetric weights matrix, e.g. distance-based weights
        """
        if self.gda_w != None:
            return self.gda_w.is_symmetric

    def has_isolates(self):
        """
        Check if any observation has no neighbors 

        Parameters
        ----------
        None

        Returns
        -------
        has_isolates : Boolean
            True means at least one observation has no neighbors 
            False means all observations have at least one neighbor
        """
        if self.gda_w != None:
            return self.gda_w.HasIsolates()

    def weights_sparsity(self):
        """
        Get sparsity computed from weights matrix

        Returns
        -------
        sparsity : float
            sparsity is computed as (#obs w/ neighbor) / (total # obs)
        """
        if self.gda_w != None:
            return self.gda_w.sparsity

    def min_neighbors(self):
        """Get minmum number of neighbors

        Returns:
            int: The number of minimum neighbors 
        """
        if self.gda_w != None:
            return self.gda_w.min_nbrs

    def median_neighbors(self):
        """Get the median number of neighbors

        Returns:
            float: The number of median neighbors 
        """
        if self.gda_w != None:
            return self.gda_w.median_nbrs

    def mean_neighbors(self):
        """Get the mean number of neighbors

        Returns:
            float: The number of mean neighbors 
        """
        if self.gda_w != None:
            return self.gda_w.mean_nbrs

    def max_neighbors(self):
        """Get the maximum number of neighbors

        Returns:
            int: The number of maximum neighbors 
        """
        if self.gda_w != None:
            return self.gda_w.max_nbrs

    def weights_type(self):
        """Get Weights type

        Returns:
            int: weights type
        """
        if self.gda_w != None:
            return self.gda_w.weight_type


    def get_neighbors(self, idx):
        """
        Get neighbors of idx-th observation

        Parameters
        ----------
        idx : int
            The index of observation

        Returns
        -------
        nbrs : tuple
            a tuple of ids of neighbors of specified idx-th observation.
        """
        if self.gda_w != None:
            return self.gda_w.GetNeighbors(idx)

    def spatial_lag(self, values):
        """
        Compute spatial lagged values for values of selected variable 

        Parameters
        ----------
        values : tuple
            The tuple of values of selected column

        Returns
        -------
        lags : list
            the computed spatial lagged values:
        """
        if self.gda_w != None:
            rst = []
            for i in range(self.num_obs):
                rst.append(self.gda_w.SpatialLag(i, values))
            return rst

    def save_weights(self, out_path, layer_name, id_name, id_values):
        """
        Save current spatial weights to a file.

        Parameters
        ----------
        out_path : str
            The path of an output weights file
        layer_name : str
            The name of the layer of input dataset 
        id_name : str
            The id name (or field name), which is an associated column contains unique values, 
            that makes sure that the weights are connected to the correct 
            observations in the data table.
        id_values : tuple
            The tuple of values of selected id_name (column/field)

        """
        if self.gda_w != None:
            return self.gda_w.Save(out_path, layer_name, id_name, id_values)

    def __repr__(self):
        if self.gda_w:
            info = ""
            info += "Weights Meta-data:\n"
            info += '{0:>24} {1:>20}\n'.format("number of observations:", self.num_obs) 
            info += '{0:>24} {1:>20}\n'.format("is symmetric:", "True" if self.is_symmetric() else "False") 
            info += '{0:>24} {1:>20}\n'.format("sparsity:", self.weights_sparsity()) 
            info += '{0:>24} {1:>20}\n'.format("# min neighbors:", self.min_neighbors()) 
            info += '{0:>24} {1:>20}\n'.format("# max neighbors:", self.max_neighbors()) 
            info += '{0:>24} {1:>20}\n'.format("# mean neighbors:", self.mean_neighbors()) 
            info += '{0:>24} {1:>20}\n'.format("# median neighbors:", self.median_neighbors()) 
            info += '{0:>24} {1:>20}\n'.format("has isolates:", "True" if self.has_isolates() else "False") 
            return info

def read_gal(file_path, id_vec):
    """Read GAL Weights
    Create a spatial weights object from a .GAL file

    Args:
        file_path (str): The file paht of the .GAL file
        id_vec (tuple): The id values used in the .GAL file. e.g. [1,2,3,4,...]

    Returns:
        Weight: An instance of Weight class 
    """

    f = open(file_path)
    first_line = f.readline()

    items = first_line.split(" ")

    if len(items) < 1:
        raise ValueError("The content of weights file is not correct.")

    num_obs = int(items[1])

    if len(id_vec) != num_obs:
        raise ValueError("The id_vec size does not match the number of observations in weights file.")

    gda_w = gda_load_gal(file_path, id_vec)

    return Weight(gda_w)

def read_gwt(file_path, id_vec):
    """Read GWT Weights
    Create a spatial weights object from a .GWT file

    Args:
        file_path (str): The file paht of the .GAL file
        id_vec (tuple): The id values used in the .GAL file. e.g. [1,2,3,4,...]

    Returns:
        Weight: An instance of Weight class 
    """

    f = open(file_path)
    first_line = f.readline()

    items = first_line.split(" ")

    if len(items) < 1:
        raise ValueError("The content of weights file is not correct.")

    num_obs = int(items[1])

    if len(id_vec) != num_obs:
        raise ValueError("The id_vec size does not match the number of observations in weights file.")

    gda_w = gda_load_gwt(file_path, id_vec)

    return Weight(gda_w)

def read_swm(file_path, **kwargs):
    """Read SWM Weights
    Create a spatial weights object from a .swm file

    Args:
        file_path (str): The file paht of the .swm file
        id_vec (tuple): The id values used in the .sfile. e.g. [1,2,3,4,...] (optional)

    Returns:
        Weight: An instance of Weight class 
    """

    id_vec = [] if 'id_vec'  not in kwargs else kwargs['id_vec']

    if not all(isinstance(x, int) for x in id_vec):
        raise ValueError("The values of id_vec has to be integer type.")

    gda_w = gda_load_swm(file_path, VecInt(id_vec))

    return Weight(gda_w)
