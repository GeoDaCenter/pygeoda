from ..libgeoda import LISA, BatchLISA
import math

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

    def run(self):
        """Call to run LISA computation
        """
        return self.gda_lisa.Run()


    def set_permutations(self, num_perm):
        """Set the number of permutations for the LISA computation

        Args:
            num_perm (int): the number of permutations e.g. 99, 999, 9999, 999999
        """
        if num_perm < 1 or num_perm > 999999:
            raise ValueError("The number of permutations is a positive integer number, but has to be less than 999999.")

        return self.gda_lisa.SetNumPermutations(num_perm)

    def set_threads(self, num_threads):
        """Set the number of CPU threads for the LISA computation

        Args:
            num_threads (int): the number of CPU threads
        """
        if num_threads < 1: 
            raise ValueError("The number of CPU threads has to be a positive integer number.")
            
        return self.gda_lisa.SetNumThreads(num_threads)


    def lisa_values(self):
        """Get LISA values
        Get the local spatial autocorrelation values returned from LISA computation.

        Return:
            tuple: A numeric vector of local spatial autocorrelation
        """
        return self.gda_lisa.GetLISAValues()

    def lisa_pvalues(self):
        """Get pseudo-p values of LISA
        Get the local pseudo-p values of significance returned from LISA computation.

        Return:
            A numeric vector of pseudo-p values of local spatial autocorrelation
        """
        vals = self.gda_lisa.GetLocalSignificanceValues()
        clean_vals = [math.nan if v < 0 else v for v in vals]
        return clean_vals

    def lisa_clusters(self):
        """Get local cluster indicators
        Get the local cluster indicators returned from LISA computation.

        Return:
            A numeric vector of LISA cluster indicator
        """
        return self.gda_lisa.GetClusterIndicators()

    def lisa_num_nbrs(self):
        """Get the number of neighbors of every observations in LISA computation.

        Return:
            :obj:`list` of int: a list of integer values of the number of neighbors of every observations in LISA computation.
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetNumNeighbors()

    def lisa_labels(self):
        """Get the cluster labels of LISA computation.

        Return:
            :obj:`list` of :obj:`str`: a list of string values of the number of the cluster labels of LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetLabels()


    def lisa_colors(self):
        """Get the cluster colors of LISA computation.

        Return:
            :obj:`list` of :obj:`str`: a list of string values of the number of the cluster colors of LISA computation
                e.g. local moran, local geary etc.
        """
        return self.gda_lisa.GetColors()

    def lisa_fdr(self, p):
        '''False Discovery Rate value of local spatial autocorrelation
        Get False Discovery Rate value based on current LISA computation and current significant p-value
        
        Args:
            p: A value of current siginificant p-value
            
        Returns:
            float: A numeric vector of False Discovery Rate
        '''
        
        return self.gda_lisa.GetFDR(p)

    def lisa_bo(self, p):
        '''Bonferroni bound value
        Get Bonferroni bound value based on current LISA computation and current significat p-value
        
        Args:
            p: A value of current siginificant p-value
            
        Returns:
            A numeric value of Bonferroni bound
        '''
        
        return self.gda_lisa.GetBO(p)

    def __repr__(self):
        info = "lisa object:\n\n"
        info += "\tlisa_values(): [{0}, ...]\n".format(str(self.lisa_values()[:10])[1:-1])
        info += "\tlisa_pvalues(): [{0}, ...]\n".format(str(self.lisa_pvalues()[:10])[1:-1])
        info += "\tlisa_num_nbrs(): [{0}, ...]\n".format(str(self.lisa_num_nbrs()[:10])[1:-1])
        info += "\tlisa_clusters(): [{0}, ...]\n".format(str(self.lisa_clusters()[:10])[1:-1])
        info += "\tlisa_labels(): {0}\n".format(str(self.lisa_labels()))
        info += "\tlisa_colors(): {0}\n".format(str(self.lisa_colors()))
        return info



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

    def run(self):
        """Call to run LISA computation
        """
        return self.gda_lisa.Run()


    def set_permutations(self, num_perm):
        """Set the number of permutations for the LISA computation

        Args:
            num_perm (int): the number of permutations e.g. 999, 9999, 999999
        """
        if num_perm < 1:
            raise ValueError("The number of permutations is a positive integer number.")

        return self.gda_lisa.SetNumPermutations(num_perm)

    def set_threads(self, num_threads):
        """Set the number of CPU threads for the LISA computation

        Args:
            num_threads (int): the number of CPU threads
        """
        if num_threads < 1: 
            raise ValueError("The number of CPU threads has to be a positive integer number.")
            
        return self.gda_lisa.SetNumThreads(num_threads)


    def lisa_values(self, idx):
        """Get LISA values
        Get the local spatial autocorrelation values returned from LISA computation.

        Args:
            idx (int): The index of input data list
        Return:
            tuple: A numeric vector of local spatial autocorrelation
        """
        return self.gda_lisa.GetLISAValues(idx)

    def lisa_pvalues(self, idx):
        """Get the local pseudo-p values of significance returned from LISA computation.

        Args:
            idx (int): The index of input data list

        Return:
            :obj:`list` of float: a list of float values of local pseudo-p values of significance returned from LISA computation
        """
        return self.gda_lisa.GetLocalSignificanceValues(idx)

    def lisa_clusters(self, idx):
        """Get the local cluster indicators returned from LISA computation.

        Args:
            idx (int): The index of input data list

        Return:
            :obj:`list` of float: a list of float values of local cluster indicators returned from LISA computation
        """
        return self.gda_lisa.GetClusterIndicators(idx)

    def lisa_num_nbrs(self):
        """Get numbers of neighbors for all observations
        Get the number of neighbors of every observations in LISA computation.

        Return:
            A numeric vector of the number of neighbors
        """
        return self.gda_lisa.GetNumNeighbors()

    def lisa_labels(self):
        """Get cluster labels
        Get the cluster labels of LISA computation.

        Return:
            A string vector of cluster labels
        """
        return self.gda_lisa.GetLabels()


    def lisa_colors(self):
        """Get cluster colors
        Get the cluster colors of LISA computation.

        Return:
            A string vector of cluster colors
        """
        return self.gda_lisa.GetColors()

    def lisa_fdr(self, p):
        '''False Discovery Rate value of local spatial autocorrelation
        Get False Discovery Rate value based on current LISA computation and current significant p-value
        
        Args:
            p: A value of current siginificant p-value
            
        Returns:
            float: A numeric vector of False Discovery Rate
        '''
        
        return self.gda_lisa.GetFDR(p)

    def lisa_bo(self, p):
        '''Bonferroni bound value
        Get Bonferroni bound value based on current LISA computation and current significat p-value
        
        Args:
            p: A value of current siginificant p-value
            
        Returns:
            float: A numeric value of Bonferroni bound
        '''
        
        return self.gda_lisa.GetBO(p)