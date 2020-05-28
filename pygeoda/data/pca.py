from ..libgeoda import gda_pca
from ..libgeoda import PCAResult

__author__ = "Hang Zhang <zhanghanggis@163.com>, "

class PCA(object):
    ''' Principal component analysis
    Note:
        The principal components can be interpreted as the best linear approximation to the multivariate point cloud of the data. The goal is to find a small number of principal components,that explains the bulk of the variance in the original variables.
    
    Args:
        data (tuple): A 2d numeric list with values of selected variables

    Returns:
        PCA_obj: A PCA object that wrappers the c++ PCAResult object containing the details of PCA computation
    '''
    def __init__(self, data):
        '''Constructor of PCAResult object
        
        Args:
            data (tuple): A 2d numeric list with values of selected variables
        '''
        if data is None:
            raise("The data from selected variable is empty.")
        self.pca_r = gda_pca(data)

    def getMethod(self):
        '''Get the PCA calculation method.

        Returns:
            a string of method description
                e.g. 'svd'
        '''
        return self.pca_r.getMethod()               

    def getStandardDev(self):
        '''get the standard deviation of PCAResult.
        
        Rerurns:
            :obj:`tuple` of float: a list of float values of standard deviation of PCAResult
                e.g. (1.463034,1.095819,1.049785,0.816680,0.740726,0.583971)
        '''                
        return self.pca_r.getStandardDev()

    def getPropOfVar(self):
        '''Get the Proportion of variance of PCAResult.
        
        Returns:
            :obj:`tuple` of float: a list of float values of Proportion of variance of PCAResult
                e.g. (1.463034,1.095819,1.049785,0.816680,0.740726,0.583971)
        '''
        return self.pca_r.getPropOfVar()

    def getCumProp(self):
        '''Get the Cumulative proportion of PCAResult.

        Returns:
            :obj:`tuple` of float: a list of float values of the Cumulative proportion of PCAResult
                e.g. (1.463034,1.095819,1.049785,0.816680,0.740726,0.583971)
        '''
        return self.pca_r.getCumProp()

    def getKaiser(self):
        '''Get the value 0f Kaiser in PCAResult.

        Returns:
            :obj:a `float` number: value 0f Kaiser in PCAResult
                e.g. 3.000
        '''
        return self.pca_r.getKaiser()
    
    def getThresh95(self):
        '''Get the value 0f  threshold criteria for contribution up to 95% in PCAResult.

        Returns:
            :obj:a `float` number:value 0f threshold criteria for contribution up to 95% in PCAResult
                e.g. 5.0000
        '''
        return self.pca_r.getThresh95()
    
    def getEigenValues(self):
        '''Get the Eigenvalues of PCAResult of PCAResult.

        Returns:
            :obj:`tuple` of float: a list of float values of the Eigenvalues of PCAResult
                e.g. (1.463034,1.095819,1.049785,0.816680,0.740726,0.583971)
        '''    
        return self.pca_r.getEigenValues()
    
    def getLoadings(self):
        '''Get a 2d numeric list with values of  PCAResult base selected variables.

        Returns:
            :obj:a 2d numeric `list` of float: a 2d numeric list with values of selected variables of PCAResult
                e.g. [[1.463034,1.095819,1.049785,0.816680,0.740726,0.583971],[0.8791, 0.0937, 0.0188, 0.006, 0.0016, 1.425]]
        '''
        return self.pca_r.getLoadings()
    
    def getSqCorrelations(self):
        '''Get a 2d numeric list with values of squared correlations of PCAResult base selected variables.

        Returns:
            :obj:a 2d numeric `list` of float: a 2d numeric list with values of selected variables of PCAResult
                e.g. [[1.463034,1.095819,1.049785,0.816680,0.740726,0.583971],[0.8791, 0.0937, 0.0188, 0.006, 0.0016, 1.425]]
        '''
        return self.pca_r.getSqCorrelations()