from .libgeoda import GeoDa
import os
__author__ = "Xun Li <lixun910@gmail.com>"
__all__ = ['geoda', 'open']

class geoda:
    """
    A wrapper class of GeoDa class from libgeoda

    Attributes:
        num_obs (int): The number of observations
        num_cols (int): The number of columns
        field_names (tuple): A list of field names 
        field_types (tuple): A list of field types {integer, real, string}
        map_type (str): The map type (Point, Polygon (or LineSegment)
    """
    def __init__(self, gda_obj):
        """
        Constructor of geoda object.

        Parameters
        ----------
        gda_obj : Object
            An object / pointer of GeoDa class 
        """
        self.gda = gda_obj

        self.num_obs = gda_obj.GetNumObs()

        self.num_cols = gda_obj.GetNumCols()

        self.field_names = gda_obj.GetFieldNames()

        self.field_types = gda_obj.GetFieldTypes()

        self.map_type = gda_obj.GetMapType()

    def GetNumCols(self):
        """
        Get the number of columns

        Returns
        -------
        : int
            the number of columns
        """
        return self.gda.GetNumCols()

    def GetNumObs(self):
        """Get the number of observations

        Return:
            int: thu number of observations
        """
        return self.gda.GetNumObs()

    def GetFieldNames(self):
        """Get the field names of all columns

        Return:
            :obj:`list` of :obj:`str`: a list of field names 
        """
        return self.gda.GetFieldNames()

    def GetFieldTypes(self):
        """Get the field types (integer, real, string) of all columns

        Return:
            :obj:`list` of :obj:`str`: a list of field types
        """
        return self.gda.GetFieldTypes()

    def GetMapType(self):
        """Get the map type

        Return:
            :obj:`str`: map type
        """
        return self.gda.GetMapType()

    def GetIntegerCol(self, col_name):
        """Get the integer values from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of int: a list of integer values of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise "The column name is not valid or not existed."
        return self.gda.GetIntegerCol(col_name)

    def GetRealCol(self, col_name):
        """Get the real values from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of float: a list of float values of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise "The column name is not valid or not existed."
        return self.gda.GetNumericCol(col_name)

    def GetStringCol(self, col_name):
        """Get the string values from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of :obj:`str`: a list of string values of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise "The column name is not valid or not existed."
        return self.gda.GetStringCol(col_name)

    def GetUndefinedVals(self, col_name):
        """Get the undefined flags from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of :obj:`bool`: a list of bool flags indicating if the values are undefined of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise "The column name is not valid or not existed."
        return self.gda.GetUndefinesCol(col_name)


def open(ds_path):
    """Create a geoda object by reading a spatial dataset

    Since pygeoda v0.0.4, it only supports ESRI Shapefile. It is recommended to use 
    geopandas to load spatial dataset, and then use `geopandas_to_geoda()` to 
    create a geoda object. See :ref:`geopandas-pygeoda`

    Args:
        ds_path (str): The path of the spatial dataset

    Return:
        :obj:`Object`: An object of geoda instance
    """
    if not isinstance(ds_path, str) or len(ds_path) <= 0:
        raise "The input path of data source is not valid"
    if not ds_path.lower().endswith('.shp'):
        raise 'Pygeoda can only open ESRI shapefile since v0.0.4'
    if not os.path.exists(ds_path[0:-3]+'dbf'):
        raise 'This shapefile miss a DBF file'
    if not os.path.exists(ds_path[0:-3]+'shx'):
        raise 'This shapefile miss a SHX file'
    gda_obj = GeoDa(ds_path)
    return geoda(gda_obj)
