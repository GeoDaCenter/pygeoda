try:
    import geopandas
    import pandas
    import shapely
except ImportError:
    print("GeoPandas is not found. Please install GeoPandas for ESDA features.")

import sys
import string
import random

from .libgeoda import GeoDa, GeoDaTable
from .gda import geoda

__author__ = "Xun Li <lixun910@gmail.com>"
__all__ = ['geopandas_to_geoda','geoda_to_geopandas']

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def print_crs(gdf_crs):
    prj_str = ''
    for k, v in gdf_crs.items():
        param = '+' + str(k) + '=' + str(v) + ' '
        prj_str += param
    return prj_str

def geopandas_to_geoda(gdf):
    """Create a geoda instance from geopandas object.

    Args:
        gdf (GeoDataFrame): An instance of geopands class.
    
    Returns:
        (geoda): An instance of geoda class.
    """

    geoms = gdf.geometry
    n_rows = len(gdf)
    n_cols = gdf.columns.size
    col_nms = gdf.columns

    # Table
    gda_tbl = GeoDaTable()

    for i in range(n_cols):
        col_nm = str(col_nms[i])
        if col_nm == 'geometry':
            continue
        col_type = gdf[col_nm].dtype
        vals = gdf[col_nm].to_list()
        if col_type == 'float64' or col_type == 'float':
            gda_tbl.AddRealColumn(col_nm, vals)
        elif col_type == 'int64' or col_type == 'int':
            gda_tbl.AddIntColumn(col_nm, vals)
        #else:
        #    gda_tbl.AddStringColumn(col_nm, vals)

    # Geoms
    wkb_size = []
    wkb_array = []
    wkb_bytecount = 0
    for i in range(n_rows):
        wkb = geoms[i].to_wkb()
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
    gdf.geom_type
    map_type = "map_polygons"

    # random file name
    layer_name = id_generator()

    # projection
    #prj = str(print_crs(gdf.crs))
    prj = ""

    gda = GeoDa(gda_tbl, layer_name, map_type,  wkb_bytes, tuple(wkb_size), prj)

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