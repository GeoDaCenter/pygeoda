.. pygeoda documentation master file, created by
   sphinx-quickstart on Thu Oct  3 19:20:18 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pygeoda 0.0.4
=============

pygeoda is a python library that wraps all core functions of spatial data
analysis in GeoDa and libgeoda. Unlike the desktop software GeoDa,
libgeoda is a non-UI and feature focused C++ library that is designed
for programmers to do spatial data analysis using their favoriate
programming languages (R, Python, Java etc.). It also aims to be easily
integratd with other libraries, softwares or systems on different
platforms.

This document is used to introduce the pygeoda v0.0.4 library, includes all
the functions that are currently provided in version 0.0.4.

* pygeoda Github repository: https://github.com/lixun910/pygeoda
* pygeoda jupyter notebooks: https://github.com/lixun910/pygeoda_tutorial/tree/v0.0.3

You can try these jupyter notebooks in your browser via MyBinder (no installation required): 

.. image:: https://img.shields.io/badge/pygeoda-0.0.4-E66581.svg?logo=data:image/png;base64,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
    :target: https://mybinder.org/v2/gh/lixun910/pygeoda_tutorial/v0.0.3


----------

.. toctree::
   :maxdepth: 2
   :caption: USER GUIDE

   1. Introduction <intro>
   2. Installation <install>
   3. Load Spatial Data <load_data>
   4. Map Classification <map_classification>
   5. Spatial Weights <spatial_weights>
   6. Spatial Autocorrelation<spatial_auto>
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

Contributors
============

Xun Li; Hang Zhang; Yeqing Han.

Institution
-----------

.. image:: https://rgeoda.github.io/rgeoda-book/images/csds.jpg
    :target: https://spatial.uchicago.edu
    :alt: CSDS is an initiative of the Division of Social Sciences and part of the UChicago's investment in computational social science.
    
.. image:: https://yrcsd.henu.edu.cn/dfiles/7761/css/v2/image/logo.png
    :target: https://yrcsd.henu.edu.cn
    :alt: Yellow River Civilization Center is the key research base of Humanities and social sciences of the Ministry of Education

Personnel
---------
.. image:: https://spatial.uchicago.edu/sites/spatial.uchicago.edu/files/styles/directoryimage/public/uploads/images/xunli2.png?itok=A2Al_sWF
    :target: https://spatial.uchicago.edu/directories/full/team
    :width: 60
    :height: 60
.. image:: https://spatial.uchicago.edu/sites/spatial.uchicago.edu/files/styles/directoryimage/public/uploads/images/Screen%20Shot%202020-04-11%20at%2010.20.00%20AM.png?itok=1lXLfX0d
    :target: https://spatial.uchicago.edu/directories/full/fellows
    :width: 60
    :height: 60
.. image:: https://spatial.uchicago.edu/sites/spatial.uchicago.edu/files/styles/directoryimage/public/uploads/images/Screen%20Shot%202020-04-11%20at%2010.20.09%20AM.png?itok=bGNGi0gW
    :target: https://spatial.uchicago.edu/directories/full/fellows
    :width: 60
    :height: 60
.. image:: https://spatial.uchicago.edu/sites/spatial.uchicago.edu/files/styles/directoryimage/public/uploads/images/Screen%20Shot%202020-04-11%20at%2010.14.17%20AM.png?itok=Mf7BBQli
    :target: https://spatial.uchicago.edu/directories/full/Research-Assistants
    :width: 60
    :height: 60
.. image:: https://spatial.uchicago.edu/sites/spatial.uchicago.edu/files/styles/directoryimage/public/uploads/images/Screen%20Shot%202020-04-11%20at%2010.16.50%20AM.png?itok=pKz2KWCm
    :target: https://spatial.uchicago.edu/directories/full/Research-Assistants
    :width: 60
    :height: 60