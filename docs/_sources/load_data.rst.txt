.. _load_data_ref:

.. currentmodule:: pygeoda

3 Load Spatial Data
===================

pygeoda supports reading the ESRI ShapeFiles. For other data formats, 
please use `geopandas <https://geopandas.org/>`_ to load the spatial data first, 
then pass the geopandas object to function `pygeoda.open()`. 

For example, to load the ESRI Shapefile **Guerry.shp**
download from: https://geodacenter.github.io/data-and-lab/Guerry/. 

::

    >>> import pygeoda
    >>> guerry = pygeoda.open("./data/Guerry.shp")
    >>> guerry
    geoda object:
        Number of observations: 85
        Number of fields: 27
        Geometry type(s): Polygon
            field name:       field type (shapfile):
            CODE_DE                       string
            COUNT                         real
            AVE_ID_                         real
            ...

The geopandas can be used to load or manipulate spatial data first. 
Then, the geopandas object can be used to create a geoda object using 
the same function `pygeoda.open()`:

::

    >>> import geopandas
    >>> df = geopandas.read_file("./data/Guerry.shp")
    >>>
    >>> import pygeoda
    >>> guerry = pygeoda.open(df)
    >>> guerry
    geoda object:
        Number of observations: 85
        Number of fields: 27
        Geometry type(s): ('MultiPolygon', 'Polygon')
            field name:       field type (numpy.dtype):
            CODE_DE                       object
            COUNT                         float64
            AVE_ID_                         float64
            ...

.. note::
    The "Geometry type(s)" and "field type" are different from using 
    pygeoda.open() function to open an ESRI shapefile and a geopandas object.
    When opening an ESRI shapefile, the "Geometry type" could be one of 
    {'Polygon', 'Point', 'Line'} and the "field type" could be one of 
    {'real', 'string', 'integer'}. When opening a geopandas object, the 
    "Geometry type" is the defined by `GeoSeries <https://geopandas.org/docs/user_guide/data_structures.html>`_ 
    (e.g. MultiPolygon, Polygon, etc.) and the "field type" is defined by `numpy.dtype` 
    (e.g. object, float64, int64, etc.)
    

3.1 Attributes of geoda object
------------------------------

* n_cols
* n_obs
* field_names
* field_types

To access the meta-data of the loaded Guerry dataset:
::

    >>> print("number of columns:", guerry.num_cols)
    number of columns: 26

    >>> print("number of observations:", guerry.num_obs)
    number of observations: 85

    >>> print("field names:", guerry.field_names)
    field names: ('CODE_DE', 'COUNT', 'AVE_ID_', 'dept', 'Region', 'Dprtmnt', 'Crm_prs', 'Crm_prp', 'Litercy', 'Donatns', 'Infants', 'Suicids', 'MainCty', 'Wealth', 'Commerc', 'Clergy', 'Crm_prn', 'Infntcd', 'Dntn_cl', 'Lottery', 'Desertn', 'Instrct', 'Prsttts', 'Distanc', 'Area', 'Pop1831')

    >>> print("field types:", guerry.field_types)
    field types: {'CODE_DE': 'string', 'COUNT':'real', 'AVE_ID_': 'real',...}

.. note::
    If using geopandas object in `pygeoda.open()`, there will be a geometry column "geometry" with data type "geometry".

3.2 Access Table Data
---------------------

One can use the bracket `[ ]` operator to access the table data:

    >>> guerry = pygeoda.open('./data/Guerry.shp')
    >>> guerry['Crm_prs']
    (28870.0,  26226.0,  26747.0, 12935.0,...)
    >>> guerry[['Crm_prs', 'Litercy']]
    [(28870.0,  26226.0,  26747.0, 12935.0,...), (37.0,  51.0,  13.0,...)]


.. note::
    If using geopandas object in `pygeoda.open()`, there output of `[[ ]]` operator is a dataframe object, which can be 
    used as an input parameter in pygeoda functions like `skater()`, `neighbor_match_test()`, etc.

::

    >>> guerry = pygeoda.open(df)
    >>> guerry['Crm_prs']
    [28870.0,  26226.0,  26747.0, 12935.0,...]
    >>> guerry[['Crm_prs', 'Litercy']]
      Crm_prs    Litercy
    --------------------
    0 28880      37
    1 26226      51


.. note::
    In pygeoda, to pass the values of a single variable to a pygeoda function, one can use either a tuple or list;
    to pass the values of multiple variables, one can use either a list of tuples/lists or a `dataframe <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html>`_.