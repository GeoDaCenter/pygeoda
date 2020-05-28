from ..libgeoda import LISA, BatchLISA

__author__ = "Xun Li <lixun910@gmail.com>, Yeqing Han <yeqinghan_geo@163.com>"

class lisa:
    """A LISA class wrappers the results of LISA computation
    
    Attributes:
        gda_lisa An object of GeoDaLISA
    """

    def __init__(self, lisa_obj):
        """Constructor of lisa object

        Args:
            lisa_obj (Object): An object/pointer of LISA class
        """
        self.gda_lisa = lisa_obj

    def Run(self):
        """Call to run LISA computation
        """
        return self.gda_lisa.Run()


    def SetPermutations(self, num_perm):
        """Set the number of permutations for the LISA computation

        Args:
            num_perm (int): the number of permutations e.g. 99, 999, 9999, 999999
        """
        if num_perm < 1 or num_perm > 999999:
            raise("The number of permutations is a positive integer number, but has to be less than 999999.")

        return self.gda_lisa.SetNumPermutations(num_perm)

    def SetThreads(self, num_threads):
        """Set the number of CPU threads for the LISA computation

        Args:
            num_threads (int): the number of CPU threads
        """
        if num_threads < 1: 
            raise("The number of CPU threads has to be a positive integer number.")
            
        return self.gda_lisa.SetNumThreads(num_threads)


    def GetLISAValues(self):
        """Get the local spatial autocorrelation values returned from LISA computation.

        Return:
            :obj:`list` of float: a list of float values of local spatial autocorrelation computation 
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetLISAValues()

    def GetPValues(self):
        """Get the local pseudo-p values of significance returned from LISA computation.

        Return:
            :obj:`list` of float: a list of float values of local pseudo-p values of significance returned from LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetLocalSignificanceValues()

    def GetClusterIndicators(self):
        """Get the local cluster indicators returned from LISA computation.

        Return:
            :obj:`list` of float: a list of float values of local cluster indicators returned from LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetClusterIndicators()

    def GetNumNeighbors(self):
        """Get the number of neighbors of every observations in LISA computation.

        Return:
            :obj:`list` of int: a list of integer values of the number of neighbors of every observations in LISA computation.
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetNumNeighbors()

    def GetLabels(self):
        """Get the cluster labels of LISA computation.

        Return:
            :obj:`list` of :obj:`str`: a list of string values of the number of the cluster labels of LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetLabels()


    def GetColors(self):
        """Get the cluster colors of LISA computation.

        Return:
            :obj:`list` of :obj:`str`: a list of string values of the number of the cluster colors of LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetColors()

    def GetFDR(self,p):
        '''
        Get the False Discovery Rate (FDR) in LISA.
        
        Args:
            p: The current p-value of significance breakpoint
            
        Returns:
            :A p-value (breakpoint) computed as the False Discovery Rate value
        '''
        
        return self.gda_lisa.GetFDR(p)


class batchlisa:
    """A BatchLISA class wrappers the results of LISA computations
    
    Attributes:
        gda_lisa An object of BatchLISA
    """

    def __init__(self, lisa_obj):
        """Constructor of lisa object

        Args:
            lisa_obj (Object): An object/pointer of LISA class
        """
        self.gda_lisa = lisa_obj

    def Run(self):
        """Call to run LISA computation
        """
        return self.gda_lisa.Run()


    def SetPermutations(self, num_perm):
        """Set the number of permutations for the LISA computation

        Args:
            num_perm (int): the number of permutations e.g. 99, 999, 9999, 999999
        """
        if num_perm < 1 or num_perm > 999999:
            raise("The number of permutations is a positive integer number, but has to be less than 999999.")

        return self.gda_lisa.SetNumPermutations(num_perm)

    def SetThreads(self, num_threads):
        """Set the number of CPU threads for the LISA computation

        Args:
            num_threads (int): the number of CPU threads
        """
        if num_threads < 1: 
            raise("The number of CPU threads has to be a positive integer number.")
            
        return self.gda_lisa.SetNumThreads(num_threads)


    def GetLISAValues(self, idx):
        """Get the local spatial autocorrelation values returned from LISA computation.

        Return:
            :obj:`list` of float: a list of float values of local spatial autocorrelation computation 
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetLISAValues(idx)

    def GetPValues(self, idx):
        """Get the local pseudo-p values of significance returned from LISA computation.

        Return:
            :obj:`list` of float: a list of float values of local pseudo-p values of significance returned from LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetLocalSignificanceValues(idx)

    def GetClusterIndicators(self, idx):
        """Get the local cluster indicators returned from LISA computation.

        Return:
            :obj:`list` of float: a list of float values of local cluster indicators returned from LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetClusterIndicators(idx)

    def GetNumNeighbors(self):
        """Get the number of neighbors of every observations in LISA computation.

        Return:
            :obj:`list` of int: a list of integer values of the number of neighbors of every observations in LISA computation.
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetNumNeighbors()

    def GetLabels(self):
        """Get the cluster labels of LISA computation.

        Return:
            :obj:`list` of :obj:`str`: a list of string values of the number of the cluster labels of LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetLabels()


    def GetColors(self):
        """Get the cluster colors of LISA computation.

        Return:
            :obj:`list` of :obj:`str`: a list of string values of the number of the cluster colors of LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetColors()

    def GetFDR(self,p):
        '''
        Get the False Discovery Rate (FDR) in LISA.
        Args:
            p: The current p-value of significance breakpoint
            
        Returns:
            :A p-value (breakpoint) computed as the False Discovery Rate value
        '''
        
        return self.gda_lisa.GetFDR(p)