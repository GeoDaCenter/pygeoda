# pygeoda

[![PyPI version](https://badge.fury.io/py/pygeoda.svg)](https://badge.fury.io/py/pygeoda)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pygeoda)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/pygeoda/badges/version.svg)](https://anaconda.org/conda-forge/pygeoda)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/pygeoda/badges/downloads.svg)](https://anaconda.org/conda-forge/pygeoda)


pygeoda is a python library for spatial data analysis based on libgeoda and GeoDa. It provides spatial data analysis functionalities including Exploratory Spatial Data Analysis, Spatial Cluster Detection and Clustering Analysis, Regionalization, etc. based on the C++ source code of GeoDa, which is an open-source software tool that serves as an introduction to spatial data analysis. 

### Installation

To install from PyPi:

```
pip install pygeoda
```

To install with conda run:

```
conda install -c conda-forge pygeoda 
```

To install from source: (See more details: https://geodacenter.github.io/pygeoda/install.html)

```
pip install git+https://github.com/geodacenter/pygeoda    
```


#### Documentation

[https://geodacenter.github.io/pygeoda](https://geodacenter.github.io/pygeoda)

#### Quick Start

* pygeoda + ESRI Shapefile
```Python
import pygeoda
gda = pygeoda.open('./data/Guerry.shp')
w = pygeoda.queen_weights(gda)
lisa = pygeoda.local_moran(w, gda['Crm_prs'])
#lisa object:
#    lisa_values(): [0.516120231288079, 0.8182751384950308, ...]
#    lisa_pvalues(): [0.197, 0.013, ...]
#    lisa_num_nbrs(): [4, 6, ...]
#    lisa_clusters(): [0, 1, ...]
#    lisa_labels(): ('Not significant', 'High-High', 'Low-Low', 'High-Low', 'Low-High', 'Undefined', 'Isolated')
#    lisa_colors(): ('#eeeeee', '#FF0000', '#0000FF', '#a7adf9', '#f4ada8', '#464646', '#999999')
```

* pygeoda + GeoPandas

```Python
import geopandas
df = geopandas.read_file('./data/Guerry.shp')

import pygeoda
gda = pygeoda.open(df)
w = pygeoda.queen_weights(gda)
lisa = pygeoda.local_moran(w, gda['Crm_prs'])
#lisa object:
#    lisa_values(): [0.516120231288079, 0.8182751384950308, ...]
#    lisa_pvalues(): [0.197, 0.013, ...]
#    lisa_num_nbrs(): [4, 6, ...]
#    lisa_clusters(): [0, 1, ...]
#    lisa_labels(): ('Not significant', 'High-High', 'Low-Low', 'High-Low', 'Low-High', 'Undefined', 'Isolated')
#    lisa_colors(): ('#eeeeee', '#FF0000', '#0000FF', '#a7adf9', '#f4ada8', '#464646', '#999999')
```


## Current version 0.0.8

* Spatial Weights
    * Queen
    * Rook
    * Distance based
    * K-Nearest Neighbor
    * Kernel
    
* Local Indicators of Spatial Association (LISA)
    * Local Moran
    * Local Geary
    * Local Getis-Ord 
    * Local Join Count
    * Multivariate Local Geary
    * Local Join Count
    * Bivariate Local Join Count
    * (Multivariate) Colocation Local Join Count
    * Quantile LISA
    * Multivariate Quantile LISA

* Spatial Clustering
    * SCHC Spatial Constrained Hierarchical Clustering 
      * Single-linkage
      * Complete-linkage
      * Average-linkage
      * Ward-linkage
    * SKATER
    * REDCAP
      * First-order and Single-linkage
      * Full-order and Complete-linkage
      * Full-order and Average-linkage
      * Full-order and Single-linkage
      * Full-order and Ward-linkage
    * AZP
      * greedy
      * Tabu Search
      * Simulated Annealing
    * Max-p
      * greedy
      * Tabu Search
      * Simulated Annealing
      
* Map Classification
   * NaturalBreaks
   * QuantileBreaks
   * Hinge15Breaks
   * Hinge30Breaks
   * PercentileBreaks
   * StddevBreaks
   
* Data
  * Demean standardize
  * Standardize data (Z)
  * Median absolute deviation


## Authors

Xun Li and Luc Anselin

## Contributors

Guanpeng Dong; Yong Liu; Hang Zhang; Yeqing Han;
