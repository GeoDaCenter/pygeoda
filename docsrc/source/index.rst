.. pygeoda documentation master file, created by
   sphinx-quickstart on Thu Oct  3 19:20:18 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pygeoda 0.0.8
=============

pygeoda is a python library for spatial data analysis based on `GeoDa <https://geodacenter.github.io>`_ 
and `libgeoda <https://github.com/geodacenter/libgeoda>`_, It provides 
spatial data analysis functionalities including Exploratory Spatial Data Analysis, 
Spatial Cluster Detection and Clustering Analysis, Regionalization, etc. 
based on the C++ source code of GeoDa, which is an open-source software 
tool that serves as an introduction to spatial data analysis. 


Quick Start
-----------

pygeoda is a light-weighted library and has no dependencies. 
It works with ESRI Shapefiles and `geopandas <https://geopandas.org>`_.

    >>> import pygeoda
    >>> gda = pygeoda.open('./data/Guerry.shp')
    >>> w = pygeoda.queen_weights(gda)
    Weights Meta-data:
        number of observations:                   85
                  is symmetric:                 True
                      sparsity:  0.05813148788927336
               # min neighbors:                    2
               # max neighbors:                    8
              # mean neighbors:   4.9411764705882355
            # median neighbors:                  5.0
                  has isolates:                False
    >>> lisa = pygeoda.local_moran(w, gda['Crm_prs'])
    >>> lisa
    lisa object:
        lisa_values(): [0.516120231288079, 0.8182751384950308, ...]
        lisa_pvalues(): [0.197, 0.013, ...]
        lisa_num_nbrs(): [4, 6, ...]
        lisa_clusters(): [0, 1, ...]
        lisa_labels(): ('Not significant', 'High-High', 'Low-Low', 'High-Low', 'Low-High', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#FF0000', '#0000FF', '#a7adf9', '#f4ada8', '#464646', '#999999')


    >>> import geopandas    
    >>> df = geopandas.read_file('./data/Guerry.shp')
    >>>
    >>> import pygeoda
    >>> w = pygeoda.queen_weights(df)
    Weights Meta-data:
        number of observations:                   85
                  is symmetric:                 True
                      sparsity:  0.05813148788927336
               # min neighbors:                    2
               # max neighbors:                    8
              # mean neighbors:   4.9411764705882355
            # median neighbors:                  5.0
                  has isolates:                False
    >>> lisa = pygeoda.local_moran(w, df['Crm_prs'])
    >>> lisa
    lisa object:
        lisa_values(): [0.516120231288079, 0.8182751384950308, ...]
        lisa_pvalues(): [0.197, 0.013, ...]
        lisa_num_nbrs(): [4, 6, ...]
        lisa_clusters(): [0, 1, ...]
        lisa_labels(): ('Not significant', 'High-High', 'Low-Low', 'High-Low', 'Low-High', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#FF0000', '#0000FF', '#a7adf9', '#f4ada8', '#464646', '#999999')

.. toctree::
   :maxdepth: 2
   :caption: USER GUIDE

   1. Introduction <intro>
   2. Installation <install>
   3. Load Spatial Data <load_data>
   4. Map Classification <map_classification>
   5. Spatial Weights <spatial_weights>
   6. Local Indicators of Spatial Association<spatial_auto>
   7. Spatial Clustering <spatial_clustering>
   ESDA with pygeoda and geopandas <esda_geopandas>
   


-------------

.. toctree::
   :maxdepth: 2
   :caption: API REFERENCE
   
   pygeoda API <api>



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Authors
=======

`Xun Li <https://lixun910.github.io>`_; `Luc Anselin <https://spatial.uchicago.edu/directory/luc-anselin-phd>`_

Contributors
============

`Guanpeng Dong <http://hhwm.henu.edu.cn/info/1031/1151.htm>`_; `Yong Liu <http://hhwm.henu.edu.cn/info/1031/1121.htm>`_; Hang Zhang; Yeqing Han; 

----

.. image:: https://spatial.uchicago.edu/sites/spatial.uchicago.edu/files/styles/columnwidth-wider/public/uploads/images/CSDS_logo_4C_1.jpg?itok=rKJfXzmf
    :target: https://spatial.uchicago.edu
    :alt: CSDS is an initiative of the Division of Social Sciences and part of the UChicago's investment in computational social science.