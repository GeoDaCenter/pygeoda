.. _load_data_ref:

.. currentmodule:: pygeoda

3 Load Spatial Data
===================

The data formats that pygeoda v0.0.4 can load directly ESRI Shapefile only. For other formats, please load with geopandas,and then call geopandas_to_geoda for pygeoda processing.

.. note::
    In this tutorial, we only tested loading ESRI shapefiles
    using pygeoda v0.0.4. Please create a ticket in pygeoda's
    repo https://github.com/lixun910/pygeoda/issues if you
    experience any issues when loading spatial data.

For example, to load the ESRI Shapefile **Guerry.shp**
download from: https://geodacenter.github.io/data-and-lab/Guerry/

::

    >>> import pygeoda
    >>> guerry = pygeoda.open("./data/Guerry.shp")

The `pygeoda.open()` function returns a geoda object, which
can be used to access the meta-data, fields, and columns of the input dataset.
::

    Usage
    pygeoda.open(ds_path)

    Arguments
    ds_path	(character) The path of the spatial dataset

    Value
    gda_obj An object of geoda class

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
    field types: ('string', 'numeric', 'numeric', 'integer', 'string', 'string', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'integer', 'numeric', 'integer', 'numeric')

3.1 Access Table Data
---------------------

The `geoda` instance also provide functions to get data from the dataset:

* GetIntegerCol(col_name)
* GetRealCol(col_name)
* GetStringCol(col_name)

For example, to get the integer values of the "Crm_prp" column:
::

    >>> crm_prp = guerry.GetIntegerCol("Crm_prp")
    >>> print("firs 10 values of Crm_prp:", crm_prp[:10])
    firs 10 values of Crm_prp: (15890, 5521, 7925, 7289, 8174, 10263, 8847, 9597, 4086, 10431)