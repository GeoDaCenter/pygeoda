# pygeoda

[![Build Status](https://travis-ci.org/lixun910/pygeoda.svg?branch=master)](https://travis-ci.org/lixun910/pygeoda)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/lixun910/pygeoda?svg=true)](https://ci.appveyor.com/project/lixun910/pygeoda)
[![PyPI version](https://badge.fury.io/py/pygeoda.svg)](https://badge.fury.io/py/pygeoda)


pygeoda is a python library for spatial data analysis based on libgeoda and GeoDa

### version 0.0.6

### Installation

#### Install from pip

```
pip install pygeoda
```

#### Install from source

You can install pygeoda v0.0.6 from source by using the following command in a terminal:

```
pip install git+https://gitee.com/geodacenter/pygeoda    
```

#### Docs

[https://geodacenter.github.io/pygeoda/install.html](https://geodacenter.github.io/pygeoda/install.html)

#### Features

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
    * Multivariate Local Join Count
    * Quantile LISA
    * False Discovery Rate (FDR)

* Spatial Clustering
    * SKATER
    * REDCAP
    * Max-p
    
* Others
    * PCA
    * MDS (multi dimensional scaling)



### Contributors

* @lixun910
* @zh345
* @yeqing_han
