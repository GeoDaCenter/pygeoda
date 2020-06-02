.. _spatial_sa_ref:

.. currentmodule:: pygeoda

5 Spatial Autocorrelation
================================

pygeoda 0.0.4 provids following methods for univariate
local spatial autocorrelation statistics:

* Local Moran: local_moran()
* Local Geary: local_geary()
* Local Getis-Ord statistics: local_g() and local_gstar()
* Local Join Count: local_joincount()

Methods for bivariate and multivariate local spatial
autocorrelation statistics, as well as global spatial
autocorrelation satatistics, will be included in next
release of pygeoda.

In this tutorial, we will only introduce how to call these
methods using pygeoda. For more information about the local
spatial autocorrelation statisticis, please read the lab
note that Dr. Luc Anselin wrote:
http://geodacenter.github.io/workbook/6a_local_auto/lab6a.html. 


6.1 Local Moran
---------------
The Local Moran statistic is a method to identify local clusters
and local spatial outliers. For example, we can call  function
`local_moran()` with the created Queen weights and the data
“crm_prp” as input parameters:
::

    >>> lisa = pygeoda.local_moran(queen_w, crm_prp)


6.2 LISA object
---------------

The `local_moran()` function will return a `lisa` object,
which we can call its functions to access the results of lisa
computation. The functions include:

* GetClusterIndicators(): Get the local cluster indicators returned from LISA computation.
* GetColors(): Get the cluster colors of LISA computation.
* GetLabels(): Get the cluster labels of LISA computation.
* GetLISAValues(): Get the local spatial autocorrelation values returned from LISA computation.
* GetNumNeighbors(): Get the number of neighbors of every observations in LISA computation.
* GetPValues(): Get the local pseudo-p values of significance returned from LISA computation.
* GetFDR(): Get the False Discovery Rate (FDR) in LISA.
* SetPermutations(num_perm): Set the number of permutations for the LISA computation
* SetThreads(num_threads): Set the number of CPU threads for the LISA computation
* Run(): Call to run LISA computation

For example, we can call the function `GetLISAValues()`
to get the values of local Moran:
::

    >>> lms = lisa.GetLISAValues()
    >>> print(lms[:20])
    (0.015431978309803657, 0.3270633223656033, 0.021295296214118884, 0.004610544790030418, -0.0028342407096540465, 0.41493771583040345, -0.13794630908086175, 0.09986576922564794, 0.2823176310018141, 0.1218745112146858, -0.09512054168698209, 0.032611193818022896, 0.3878324535340113, 1.1888723840162665, -0.6452792226077357, -0.30964927402750314, 0.3662775143008573, 2.0375343538940496, -0.005015479968822494, 0.06971105719113387)

To get the pseudo-p values of significance of local Moran computation:
::

    >>> pvals = lisa.GetPValues()
    >>> print(pvals[:20])
    (0.414, 0.123, 0.001, 0.474, 0.452, 0.087, 0.243, 0.326, 0.299, 0.303, 0.237, 0.46, 0.258, 0.018, 0.199, 0.188, 0.131, 0.004, 0.456, 0.342)

To get the cluster indicators of local Moran computation:
::

    >>> cats = lisa.GetClusterIndicators()
    >>> print(cats[:20]
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0)


The predefined values of the indicators of LISA cluster are:

* 0 Not significant
* 1 High-High
* 2 Low-Low
* 3 High-Low
* 4 Low-High
* 5 Neighborless
* 6 Undefined

which can be accessed via function `GetLabels()`:
::

    >>> lbls = lisa.GetLabels()
    >>> lbls
    ('Not significant',
    'High-High',
    'Low-Low',
    'High-Low',
    'Low-High',
    'Undefined',
    'Isolated')

.. note::
    Different LISA objects (e.g. local_geary()) will return different
    labels and colors.

By default, the `local_moran()` function will run with
some default parameters, e.g.:
::

    permutation number: 999
    seed for random number generator: 123456789

, which are identical to GeoDa desktop software so that
we can replicate the results in GeoDa software. It is also
easy to change the paremter and re-run the LISA computation
by calling Run() function.

For example, re-run the above local Moran example
using 9999 permutations:
::

    >>> lisa.SetPermutations(9999)
    >>> lisa.Run()

Then, we can use the same `lisa` object to get the new results
after 9999 permutations:
::

    >>> pvals = lisa.GetPValues()
    >>> print(pvals[:20])
    (0.4187, 0.1265, 0.0004, 0.4679, 0.4545, 0.0728, 0.2312, 0.3071, 0.3115, 0.3088, 0.2187, 0.4803, 0.2623, 0.0113, 0.2, 0.1797, 0.1267, 0.0026, 0.4565, 0.3517)

pygeoda uses GeoDa’s C++ code, in which multi-threading is used
to accelerate the computation of LISA. We can specify how many
threads to run the computation:
::

    >>> lisa.SetThreads(4)
    >>> lisa.Run()
    >>> print(lisa.GetPValues()[:20])
    (0.4187, 0.1265, 0.0004, 0.4679, 0.4545, 0.0728, 0.2312, 0.3071, 0.3115, 0.3088, 0.2187, 0.4834, 0.2686, 0.0102, 0.2024, 0.1795, 0.1218, 0.0025, 0.459, 0.3588)

6.3 Local Geary
---------------

Local Geary is a type of LISA that focuses on squared
differences/dissimilarity. A small value of the local geary
statistics suggest positive spatial autocorrelation, whereas
large values suggest negative spatial autocorrelation.

For example, we can call the function `local_geary()` with the
created Queen weights and the data “crm_prp” as
input parameters:
::

    >>> geary_crmprp = pygeoda.local_geary(queen_w, crm_prp)

To get the cluster indicators of the local Geary computation:
::

    >>> cats = geary_crmprp.GetClusterIndicators()
    >>> print(cats[:20])
    (0, 2, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2)


To get the pseudo-p values of the local Geary computation:
::

    >>> geary_crmprp.GetPValues()
    >>> print(pvals[:20])
    (0.398, 0.027, 0.025, 0.126, 0.017, 0.314, 0.61, 0.141, 0.284, 0.11, 0.559, 0.462, 0.211, 0.236, 0.249, 0.229, 0.069, 0.041, 0.205, 0.02)

6.4 Local Getis-Ord Statistics
------------------------------

There are two types of local Getis-Ord statistics: one is
computing a ratio of the weighted average of the values
in the neighboring locations, not including the value at
the location; while another type of statistic includes the
value at the location in both numerator and denominator.

A value larger than the mean suggests a high-high cluster
or hot spot, a value smaller than the mean indicates a
low-low cluster or cold spot.

For example, we can call the function `local_g()` with the
created Queen weights and the data “crm_prp” as
input parameters:
::

    >>> localg_crmprp = pygeoda.local_g(queen_w, crm_prp)

To get the cluster indicators of the local G computation:
::

    >>> cats = localg_crmprp.GetClusterIndicators()
    >>> print(cats[:20])
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0)


To get the pseudo-p values of the local G computation:
::

    >>> pvals = localg_crmprp.GetPValues()
    >>> print(pvals[:20])
    (0.414, 0.123, 0.001, 0.474, 0.452, 0.087, 0.243, 0.326, 0.299, 0.303, 0.237, 0.46, 0.258, 0.018, 0.199, 0.188, 0.131, 0.004, 0.456, 0.342)


For the second type of local Getis-Ord statistics, we
can call the function `local_gstar()` with the created
Queen weights and the data “crm_prp” as input parameters:
::

    localgstar_crmprp = pygeoda.local_gstar(queen_w, crm_prp)


6.5 Local Join Count
--------------------

Local Join Count is a method to identify local clusters
for binary data by using a local version of the so-called
BB join count statistic. The statistic is only meaningful
for those observations with value 1. 

For example, we can load the columbus dataset, and call
the function `local_joincount()` with a Queen weights and
the data “nsa”, which is a set of binary (0,1) values,
as input parameters:
::

    >>> columbus = pygeoda.open('./data/columbus.shp')
    >>> nsa = columbus.GetIntegerCol("nsa")
    >>> columbus_w = pygeoda.queen_weights(columbus)
    >>> localjc_nsa = pygeoda.local_joincount(columbus_w, nsa)

To get the cluster indicators of the local Join Count computation:
::

    >>> cats = localjc_nsa.GetClusterIndicators()
    >>> print(cats[:20])
    (0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0)


To get the pseudo-p values of the local Join Count  computation:
::

    >>> pvals = localjc_nsa.GetPValues()
    >>> print(pvals[:20])
    (0.213, 0.07, 0.017, 0.024, 0.001, 0.226, 0.055, 0.007, 0.006, 0.275, 0.017, 0.008, 0.043, 0.004, 0.002, 0.001, 0.147, 0.049, 0.087, 0.001)

To get the number of neighbors of the local Join Count computation:
::

    >>> nn = localjc_nsa.GetNumNeighbors()
    >>> print(nn[:20])
    (2, 3, 4, 4, 8, 2, 4, 6, 8, 4, 5, 6, 4, 6, 6, 8, 3, 4, 3, 10)


6.6 Quantile LISA
-----------------

The quantile local spatial autocorrelation converte the continuous variable 
to a binary variable that takes the value of 1 for a specific quantile. 
Then appaly a local join count to the data converted.Here a k and q need 
to be selected. More specifically, the k is the number of quantiles, 
ranging form 1 to -1, and the q is the index of selected quantile for lisa, 
ranging from 0 to k-1.

For example, we can call the function `quantile_lisa()` with the created 
Queen weights, k is equal to 7, q is equal to 5 and the data “crm_prp” as 
input parameters:
::

    >>> columbus = pygeoda.open('./data/columbus.shp')
    >>> crm_prp = columbus.GetIntegerCol("crm_prp")
    >>> columbus_w = pygeoda.queen_weights(columbus)
    >>> Lisa = pygeoda.quantile_lisa(columbus_w, 7, 5, crm_prp)

To get the pseudo-p values of the quantile lisa computation:
::

    >>> pvals = lisa.GetPValues()
    >>> print(pvals[:20])
    (0.434, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.031, 0.001, 0.001, 0.431, 0.026, 0.001, 0.001)

To get the number of neighbors of the quantile lisa computation:
::

    >>> nnvals = lisa.GetNumNeighbors()
    >>> print(nnvals[:20])
        (4, 6, 6, 4, 3, 7, 3, 3, 5, 5, 7, 3, 3, 6, 5, 5, 6, 6, 7, 3)


6.7 Batch Local Moran
---------------------

Batch Local Moran is a method to apply local moran statistics on 
a set of variables using a same weights. This is a convenient way 
to batch process Lisa with the same weight. Note the data is a 2d 
list of float type values of selected variables.

For example, we can call the function `batch_local_moran()` with the 
created created Queen weights and the data was selected from the 
dataset as the input parameters. When we have multiple variables, 
we can create a list that contains the variables and then use a for 
loop to select variables.
::
    >>> guerry = pygeoda.open('./data/columbus.shp')
    >>> guerry_w = pygeoda.queen_weights(guerry)
    >>> slect_vars = ['Crm_prp','Crm_prs']
    >>> data = [guerry.GetRealCol(v) for v in slect_vars]
    >>> Lisa = pygeoda.batch_local_moran(guerry_w, data)

To get the local Moran values of one of the selected variables:
::

    >>> lms = lisa.GetLISAValues(0) 
    >>> print(lms[:20])
    (0.015, 0.327, 0.021, 0.004, -0.002, 0.414, -0.137, 0.099, 0.282, 0.121, -0.095, 0.032, 0.387, 1.188, -0.645, -0.309, 0.366, 2.037, -0.005, 0.069)
    >>> lms = lisa.GetLISAValues(1) 
    >>> print(lms[:20])
    (0.516, 0.818, 0.794, 0.733, 0.228, 0.829, 0.615, 1.627, -0.019, 0.687, 1.707, 0.821, -0.213, 0.29, -0.184, -0.047, 0.249, 0.054, 0.862, 0.835)

To get the pseudo-p values of the local moran computation of one selected variable:
::

    >>> pvals = lisa.GetPValues(0)
    >>> print(pvals[:20])
    (0.414, 0.123, 0.001, 0.474, 0.452, 0.087, 0.243, 0.326, 0.299, 0.303, 0.237, 0.461, 0.248, 0.015, 0.178, 0.172, 0.149, 0.001, 0.456, 0.371)
    >>> pvals = lisa.GetPValues(1)
    >>> print(pvals[:20])
    (0.197, 0.013, 0.023, 0.068, 0.111, 0.045, 0.281, 0.048, 0.183, 0.004, 0.002, 0.052, 0.106, 0.002, 0.266, 0.244, 0.008, 0.426, 0.060, 0.115)