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

    def IsSymmetric(self):
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

    def HasIsolates(self):
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

    def GetSparsity(self):
        """
        Get sparsity computed from weights matrix

        Returns
        -------
        sparsity : float
            sparsity is computed as (#obs w/ neighbor) / (total # obs)
        """
        if self.gda_w != None:
            return self.gda_w.sparsity

    def GetMinNbrs(self):
        """Get minmum number of neighbors

        Returns:
            int: The number of minimum neighbors 
        """
        if self.gda_w != None:
            return self.gda_w.min_nbrs

    def GetMedianNbrs(self):
        """Get the median number of neighbors

        Returns:
            float: The number of median neighbors 
        """
        if self.gda_w != None:
            return self.gda_w.median_nbrs

    def GetMeanNbrs(self):
        """Get the mean number of neighbors

        Returns:
            float: The number of mean neighbors 
        """
        if self.gda_w != None:
            return self.gda_w.mean_nbrs

    def GetMaxNbrs(self):
        """Get the maximum number of neighbors

        Returns:
            int: The number of maximum neighbors 
        """
        if self.gda_w != None:
            return self.gda_w.max_nbrs

    def GetWeightsType(self):
        """Get Weights type

        Returns:
            int: weights type
        """
        if self.gda_w != None:
            return self.gda_w.weight_type

    def GetDensity(self):
        """
        Get density computed from weights matrix

        Returns
        -------
        density : float
            density is computed as:
        """
        if self.gda_w != None:
            return self.gda_w.density


    def GetNeighbors(self, idx):
        """
        Compute neighbors of idx-th observation

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

    def SpatialLag(self, idx, values):
        """
        Compute spatial lag values of idx-th observation

        Parameters
        ----------
        idx : int
            The index of observation
        values : tuple
            The tuple of values of selected column

        Returns
        -------
        lag : float
            the spatial lag value computed as:
        """
        if self.gda_w != None:
            return self.gda_w.SpatialLag(idx, values)

    def SaveToFile(self, out_path, layer_name, id_name, id_values):
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

    def __str__(self):
        if self.gda_w:
            info = ""
            info += "Weights Meta-data:\n"
            info += "\nis symmetric:" + str(self.IsSymmetric()) 
            info += "\nsparsity:" + str(self.GetSparsity())
            info += "\ndensity:" + str(self.GetDensity())
            info += "\nmin neighbors:" + str(self.GetMinNbrs())
            info += "\nmean neighbors:" + str(self.GetMeanNbrs())
            info += "\nmedian neighbors:" + str(self.GetMedianNbrs())
            info += "\nmax neighbors:" + str(self.GetMaxNbrs())
            return info