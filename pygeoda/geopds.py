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
from .gda import geoda

__author__ = "Xun Li <lixun910@gmail.com>"
__all__ = ['geopandas_to_geoda','geoda_to_geopandas']

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