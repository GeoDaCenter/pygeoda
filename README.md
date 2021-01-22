# pygeoda

[![Build Status](https://travis-ci.org/lixun910/pygeoda.svg?branch=master)](https://travis-ci.org/lixun910/pygeoda)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/lixun910/pygeoda?svg=true)](https://ci.appveyor.com/project/lixun910/pygeoda)
[![PyPI version](https://badge.fury.io/py/pygeoda.svg)](https://badge.fury.io/py/pygeoda)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pygeoda)


pygeoda is a python library for spatial data analysis based on libgeoda and GeoDa. It provides spatial data analysis functionalities including Exploratory Spatial Data Analysis, Spatial Cluster Detection and Clustering Analysis, Regionalization, etc. based on the C++ source code of GeoDa, which is an open-source software tool that serves as an introduction to spatial data analysis. The GeoDa software and its documentation are available at https://geodacenter.github.io.

### Installation

#### Install from pip

```
pip install pygeoda
```

#### Install from source

You can install pygeoda v0.0.6 from source by using the following command in a terminal:

```
pip install git+https://github.com/geodacenter/pygeoda    
```

#### Docs

[https://geodacenter.github.io/pygeoda](https://geodacenter.github.io/pygeoda)

## Current version 0.0.6

* Map Classification
   * NaturalBreaks
   * QuantileBreaks
   * Hinge15Breaks
   * Hinge30Breaks
   * PercentileBreaks
   * StddevBreaks
   
* Spatial Weights
    * Queen
    * Rook
    * Distance based
    * K-Nearest Neighbor
    * Kernel
    
* Spatial Autocorrelation
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
      
* Data
  * Demean standardize
  * Standardize data (Z)
  * Median absolute deviation
