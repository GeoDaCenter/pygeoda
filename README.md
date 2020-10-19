# pygeoda

[![Build Status](https://travis-ci.org/lixun910/pygeoda.svg?branch=master)](https://travis-ci.org/lixun910/pygeoda)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/lixun910/pygeoda?svg=true)](https://ci.appveyor.com/project/lixun910/pygeoda)
[![PyPI version](https://badge.fury.io/py/pygeoda.svg)](https://badge.fury.io/py/pygeoda)


pygeoda is a python library for spatial data analysis based on libgeoda and GeoDa

### version 0.0.4

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

### Installation

#### Install from pip

NOTE: pip wheels will be available soon.

#### Install from source

You can install pygeoda v0.0.4 from source by using the following command in a terminal:

```
pip install git+https://gitee.com/lixun910/pygeoda    
```

### How to contribute

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request

### Contributors

* @lixun910
* @zh345
* @yeqing_han
