try:
    import geopandas
    import pandas
    import shapely
except ImportError:
    print("(Optional) GeoPandas is not found. Please install GeoPandas for ESDA features.")

import sys
import string
import random

from .libgeoda import GeoDa, GeoDaTable, VecString, VecBool, VecInt64, VecDouble

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
            raise ValueError("The column name is not valid or not existed.")
        return self.gda.GetIntegerCol(col_name)

    def GetRealCol(self, col_name):
        """Get the real values from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of float: a list of float values of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise ValueError("The column name is not valid or not existed.")
        return self.gda.GetNumericCol(col_name)

    def GetStringCol(self, col_name):
        """Get the string values from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of :obj:`str`: a list of string values of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise ValueError("The column name is not valid or not existed.")
        return self.gda.GetStringCol(col_name)

    def GetUndefinedVals(self, col_name):
        """Get the undefined flags from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of :obj:`bool`: a list of bool flags indicating if the values are undefined of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise ValueError("The column name is not valid or not existed.")
        return self.gda.GetUndefinesCol(col_name)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def geopandas_to_geoda(gdf, with_table=False):
    """Create a geoda instance from geopandas object.

    Note: the table data are NOT copied to pygeoda for performance issue. It is
    recommended to use table data in dataframe directly.

    Args:
        gdf (GeoDataFrame): An instance of geopands class.
        with_table (boolean): A boolean flag indicates if copy the table content to geoda instance
    
    Returns:
        (geoda): An instance of geoda class.
    """

    geoms = gdf.geometry
    n_rows = len(gdf)
    n_cols = gdf.columns.size
    col_nms = gdf.columns

    # Table
    gda_tbl = GeoDaTable()

    if with_table:
        for i in range(n_cols):
            col_nm = str(col_nms[i])
            if col_nm == 'geometry':
                continue
            col_type = gdf[col_nm].dtype
            vals = gdf[col_nm].to_list()
            if col_type == 'float64' or col_type == 'float':
                vf = VecDouble(n_rows)
                undef = VecBool(n_rows)
                for i in range(n_rows):
                    vf[i] = vals[i]
                    undef[i] = vals[i] == None
                gda_tbl.AddRealColumn(col_nm, vf, undef)
            elif col_type == 'int64' or col_type == 'int':
                vi = VecInt64(n_rows)
                undef = VecBool(n_rows)
                for i in range(n_rows):
                    vi[i] = vals[i]
                    undef[i] = vals[i] == None
                gda_tbl.AddIntColumn(col_nm, vi, undef)
            else:
                vs = VecString(n_rows)
                undef = VecBool(n_rows)
                for i in range(n_rows):
                    undef[i] = vals[i] == None
                    if undef[i] == False:
                        vs[i] = vals[i]
                gda_tbl.AddStringColumn(col_nm, vs, undef)

    # Geoms
    wkb_size = []
    wkb_array = []
    wkb_bytecount = 0
    for i in range(n_rows):
        wkb = geoms[i].wkb
        wkb_array.append(wkb)
        wkb_size.append(len(wkb))
        wkb_bytecount += wkb_size[-1]

    #wkb_bytes = bytes(wkb_bytecount)
    wkb_bytes = bytearray(wkb_bytecount)
    if sys.version_info[0] < 3: wkb_bytes = bytearray()
    start = 0
    for i in range(n_rows):
        wkb_bytes[start: start + wkb_size[i]] = wkb_array[i]
        start += wkb_size[i]
        

    # map type
    if gdf.geom_type[0].endswith("Polygon"):
        map_type = "map_polygons"
    elif gdf.geom_type[0].endswith("Point"):
        map_type = "map_points" 
    elif gdf.geom_type[0].endswith("Line"):
        map_type = "map_lines" 
    else:
        raise ValueError("Error: pygeoda only supports geometry type of Polygon and Point.")

    # random layer name
    layer_name = id_generator()

    # projection will be NOT handled in libgeoda
    gda = GeoDa(gda_tbl, layer_name, map_type, wkb_bytes, wkb_size)

    return geoda(gda)

def geoda_to_geopandas(geoda_obj):
    """Create a geopandas object from a geoda object.

    Args:
        geoda_obj (geoda): An instance of geoda class.
    
    Returns:
        (GeoDataFrame): An instance of geopandas class.
    """
    gda = geoda_obj.gda

    n_cols = gda.GetNumCols()
    col_nms = gda.GetFieldNames()
    col_tps = gda.GetFieldTypes()

    # pandas DF
    data = {}
    for i in range(n_cols):
        c_nm = col_nms[i]
        c_tp = col_tps[i]
        if c_tp == "integer":
            data[c_nm] = gda.GetIntegerCol(c_nm)
        elif c_tp == "numeric":
            data[c_nm] = gda.GetNumericCol(c_nm)
        else:
            if sys.version_info[0] < 3: 
                vals = gda.GetStringCol(c_nm)
                vals = [str(i) for i in vals]
                data[c_nm] = vals
            else:
                data[c_nm] = gda.GetStringCol(c_nm)
    df = pandas.DataFrame(data)

    # geometries
    geoms = []
    wkb_array = gda.GetGeometryWKB()
    for wkb in wkb_array:
        if sys.version_info[0] < 3: wkb = bytearray(wkb)
        shapely_obj = shapely.wkb.loads(bytes(wkb))
        geoms.append(shapely_obj)

    gdf = geopandas.GeoDataFrame(df, geometry=geoms)

    # projection
    return gdf

class geodaGpd(geoda):
    def __init__(self, gpd_obj):
        self.gda = geopandas_to_geoda(gpd_obj)
        self.df = gpd_obj

    def GetNumCols(self):
        """
        Get the number of columns

        Returns
        -------
        : int
            the number of columns
        """
        return len(self.df.columns)

    def GetFieldNames(self):
        """Get the field names of all columns

        Return:
            :obj:`list` of :obj:`str`: a list of field names 
        """
        return self.df.columns.tolist()

    def GetFieldTypes(self):
        """Get the field types (integer, real, string) of all columns

        Return:
            :obj:`list` of :obj:`str`: a list of field types
        """
        return self.df.dtypes

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
            raise ValueError("The column name is not valid or not existed.")

        return self.gda.GetIntegerCol(col_name)

    def GetRealCol(self, col_name):
        """Get the real values from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of float: a list of float values of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise ValueError("The column name is not valid or not existed.")
        return self.gda.GetNumericCol(col_name)

    def GetStringCol(self, col_name):
        """Get the string values from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of :obj:`str`: a list of string values of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise ValueError("The column name is not valid or not existed.")
        return self.gda.GetStringCol(col_name)

    def GetUndefinedVals(self, col_name):
        """Get the undefined flags from a column
        Args:
            :obj:`str`: the name of selected column
        Return:
            :obj:`list` of :obj:`bool`: a list of bool flags indicating if the values are undefined of selected column
        """
        if not isinstance(col_name, str) or len(col_name) <= 0:
            raise ValueError("The column name is not valid or not existed.")
        return self.gda.GetUndefinesCol(col_name)


def open(data_source):
    """Create a geoda object by reading a spatial dataset: either ESRI Shapefile or GeoPandas object.

    Since pygeoda v0.0.4, it only supports ESRI Shapefile. It is recommended to use 
    geopandas to load spatial dataset, and then use `geopandas_to_geoda()` to 
    create a geoda object. See :ref:`geopandas-pygeoda`

    Args:
        data_source (object): The data_source could be either the file path of the ESRI shapefile or a geopandas dataframe object.

    Return:
        :obj:`Object`: An object of geoda instance
    """
    if isinstance(data_source, str):
        ds_path = data_source
        if not isinstance(ds_path, str) or len(ds_path) <= 0:
            raise ValueError("The input path of data source is not valid")
        if not ds_path.lower().endswith('.shp'):
            raise ValueError('Pygeoda can only open ESRI shapefile since v0.0.4')
        if not os.path.exists(ds_path[0:-3]+'dbf'):
            raise ValueError('This shapefile miss a DBF file')
        if not os.path.exists(ds_path[0:-3]+'shx'):
            raise ValueError('This shapefile miss a SHX file')
        gda_obj = GeoDa(ds_path)

        return geoda(gda_obj)
    else:
        try:
            import geopandas
            if isinstance(data_source, geopandas.GeoDataFrame):
                pass
        except:
            pass

    return ValueError("pygeoda can't open current data source. Please use either a file path of an ESRI shapefile or a GeoPandas instance.")
