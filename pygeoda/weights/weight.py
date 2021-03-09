from ..libgeoda import VecInt64

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