.. _spatial_sa_ref:

.. currentmodule:: pygeoda

5 Local Indicators of Spatial Association–LISA
==============================================

pygeoda provids following methods for univariate, bivariate and multivariate 
local spatial autocorrelation statistics:

* Local Moran: local_moran(), local_moran_eb()
* Local Geary: local_geary(), local_multigeary()
* Local Getis-Ord statistics: local_g() and local_gstar()
* Local Join Count: local_joincount(), local_bijoincount(), local_multijoincount()
* Local Quantile LISA: local_quantilelisa(), local_multiquantilelisa()
* Local Neighbor Match Test: neighbor_match_test()


For more information about the local spatial autocorrelation statisticis, 
please read Dr. Luc Anselin's lab notes:
http://geodacenter.github.io/workbook/6a_local_auto/lab6a.html. 


6.1 Local Moran
---------------
The Local Moran statistic is a method to identify local clusters
and local spatial outliers. For example, we can call  function
`local_moran()` with the created Queen weights and the data
“crm_prp = guerry['Crm_prp']” as input parameters:
::

    >>> lm = pygeoda.local_moran(queen_w, crm_prp)
    >>> lm
    lisa object:
        lisa_values(): [0.015431978309803657, 0.3270633223656033, ...]
        lisa_pvalues(): [0.414, 0.123, ...]
        lisa_num_nbrs(): [4, 6, ...]
        lisa_clusters(): [0, 0, ...]
        lisa_labels(): ('Not significant', 'High-High', 'Low-Low', 'High-Low', 'Low-High', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#FF0000', '#0000FF', '#a7adf9', '#f4ada8', '#464646', '#999999')


6.2 LISA object
---------------

The `local_moran()` function will return a `lisa` object,
which we can call its functions to access the results of lisa
computation. The functions include:

* lisa_clusters(): Get the local cluster indicators returned from LISA computation.
* lisa_colors(): Get the cluster colors of LISA computation.
* lisa_labels(): Get the cluster labels of LISA computation.
* lisa_values(): Get the local spatial autocorrelation values returned from LISA computation.
* lisa_num_nbrs(): Get the number of neighbors of every observations in LISA computation.
* lisa_pvalues(): Get the local pseudo-p values of significance returned from LISA computation.
* lisa_fdr(): Get the False Discovery Rate (FDR) in LISA.
* lisa_bo(): Get the False Discovery Rate (FDR) in LISA.

For example, we can call the function `GetLISAValues()`
to get the values of local Moran:
::

    >>> lms = lm.lisa_values()
    >>> print(lms[:20])
    (0.015431978309803657, 0.3270633223656033, 0.021295296214118884, 0.004610544790030418, -0.0028342407096540465, 0.41493771583040345, -0.13794630908086175, 0.09986576922564794, 0.2823176310018141, 0.1218745112146858, -0.09512054168698209, 0.032611193818022896, 0.3878324535340113, 1.1888723840162665, -0.6452792226077357, -0.30964927402750314, 0.3662775143008573, 2.0375343538940496, -0.005015479968822494, 0.06971105719113387)

To get the pseudo-p values of significance of local Moran computation:
::

    >>> pvals = lm.lisa_pvalues()
    >>> print(pvals[:20])
    (0.414, 0.123, 0.001, 0.474, 0.452, 0.087, 0.243, 0.326, 0.299, 0.303, 0.237, 0.46, 0.258, 0.018, 0.199, 0.188, 0.131, 0.004, 0.456, 0.342)

To get the cluster indicators of local Moran computation:
::

    >>> cats = lm.lisa_clusters()
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

    >>> lbls = lm.lisa_labels()
    >>> lbls
    ('Not significant', 'High-High', 'Low-Low', 'High-Low', 'Low-High', 'Undefined', 'Isolated')

.. note::
    Different LISA objects (e.g. local_geary()) will return different
    labels and colors.

By default, the `local_moran()` function will run with
some default parameters, e.g.:
::

    significance_cutoff: 0.05
    permutation: 999
    permutation_method: 'complete'
    cpu_threads: 6
    seed (for random number generator): 123456789

, which are identical to GeoDa desktop software so to replicate the results 
in GeoDa software.  You can set different values when calling the lisa functions. 

For example, re-run the above local Moran example using 9999 permutations:
::

    >>> lm = pygeoda.local_moran(queen_w, crm_prp, permutations=9999)

Then, we can use the same `lisa` object to get the new results
after 9999 permutations:
::

    >>> pvals = lm.lisa_pvalues()
    >>> pvals[:20]
    (0.4187, 0.1265, 0.0004, 0.4679, 0.4545, 0.0728, 0.2312, 0.3071, 0.3115, 0.3088, 0.2187, 0.4803, 0.2623, 0.0113, 0.2, 0.1797, 0.1267, 0.0026, 0.4565, 0.3517)

pygeoda uses GeoDa’s C++ code, in which multi-threading is used
to accelerate the computation of LISA. We can specify how many
threads to run the computation:
::

    >>> lm = pygeoda.local_moran(queen_w, crm_prp, permutations=9999, cpu_threads=8)
    >>> lm.lisa_pvalues()[:20]
    (0.4187, 0.1265, 0.0004, 0.4679, 0.4545, 0.0728, 0.2197, 0.3117, 0.3139, 0.3106, 0.2189, 0.4761, 0.2649, 0.0127, 0.2014, 0.1774, 0.1299, 0.0024, 0.4557, 0.3525)

6.3 Local Geary
---------------

Local Geary is a type of LISA that focuses on squared
differences/dissimilarity. A small value of the local geary
statistics suggest positive spatial autocorrelation, whereas
large values suggest negative spatial autocorrelation.
For more details, please read: http://geodacenter.github.io/workbook/6b_local_adv/lab6b.html#local-geary 

For example, we can call the function `local_geary()` with the
created Queen weights and the data “crm_prp” as
input parameters:
::

    >>> geary_crmprp = pygeoda.local_geary(queen_w, crm_prp)
    lisa object:
        lisa_values(): [7.39808330117836, 0.28361195650519017, 3.6988922226329906, 0.23250287024601668, 0.03509605454141339, 1.8488634321425461, 0.9456415438821265, 0.36881030678112625, 1.3990003912957896, 0.79132551685303, ...]
        lisa_pvalues(): [0.398, 0.027, 0.025, 0.126, 0.017, 0.314, 0.61, 0.141, 0.284, 0.11, ...]
        lisa_num_nbrs(): [4, 6, 6, 4, 3, 7, 3, 3, 5, 5, ...]
        lisa_clusters(): [0, 2, 4, 0, 3, 0, 0, 0, 0, 0, ...]
        lisa_labels(): ('Not significant', 'High-High', 'Low-Low', 'Other Positive', 'Negative', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#b2182b', '#ef8a62', '#fddbc7', '#67adc7', '#464646', '#999999')

To get the cluster indicators of the local Geary computation:
::

    >>> cats = geary_crmprp.lisa_clusters()
    >>> print(cats[:20])
    (0, 2, 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2)


To get the pseudo-p values of the local Geary computation:
::

    >>> geary_crmprp.lisa_pvalues()
    >>> print(pvals[:20])
    (0.398, 0.027, 0.025, 0.126, 0.017, 0.314, 0.61, 0.141, 0.284, 0.11, 0.559, 0.462, 0.211, 0.236, 0.249, 0.229, 0.069, 0.041, 0.205, 0.02)

6.4 Local Getis-Ord Statistics
------------------------------

There are two types of local Getis-Ord statistics: one is
computing a ratio of the weighted average of the values
in the neighboring locations, not including the value at
the location; while another type of statistic includes the
value at the location in both numerator and denominator.
For more details, please read: http://geodacenter.github.io/workbook/6b_local_adv/lab6b.html#getis-ord-statistics

A value larger than the mean suggests a high-high cluster
or hot spot, a value smaller than the mean indicates a
low-low cluster or cold spot.

For example, we can call the function `local_g()` with the
created Queen weights and the data “crm_prp” as
input parameters:
::

    >>> localg_crmprp = pygeoda.local_g(queen_w, crm_prp)
    >>> localg_crmprp
    lisa object:
        lisa_values(): [0.012077920687925825, 0.009924096129850856, 0.018753584525825453, 0.01178494623655914, 0.011774009933407884, 0.014402421020466018, 0.009913770717138606, 0.012754984853234634, 0.01079858461945127, 0.012624434594978189, ...] lisa_pvalues(): [0.414, 0.123, 0.001, 0.474, 0.452, 0.087, 0.243, 0.326, 0.299, 0.303, ...]
        lisa_num_nbrs(): [4, 6, 6, 4, 3, 7, 3, 3, 5, 5, ...]
        lisa_clusters(): [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ...]
        lisa_labels(): ('Not significant', 'High-High', 'Low-Low', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#FF0000', '#0000FF', '#464646', '#999999')

To get the cluster indicators of the local G computation:
::

    >>> cats = localg_crmprp.lisa_clusters()
    >>> print(cats[:20])
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0)


To get the pseudo-p values of the local G computation:
::

    >>> pvals = localg_crmprp.lisa_pvalues()
    >>> print(pvals[:20])
    (0.414, 0.123, 0.001, 0.474, 0.452, 0.087, 0.243, 0.326, 0.299, 0.303, 0.237, 0.46, 0.258, 0.018, 0.199, 0.188, 0.131, 0.004, 0.456, 0.342)


For the second type of local Getis-Ord statistics, we
can call the function `local_gstar()` with the created
Queen weights and the data “crm_prp” as input parameters:
::

    >>> localgstar_crmprp = pygeoda.local_gstar(queen_w, crm_prp)
    >>> localgstar_crmprp
    lisa object:
        lisa_values(): [0.014177043620524426, 0.0096136007223102, 0.017574324039034434, 0.01150147630889935, 0.011773152971874002, 0.014324040100669639, 0.010638678994617219, 0.01301062524443436, 0.009960482489792222, 0.012951662452195357, ...]
        lisa_pvalues(): [0.414, 0.123, 0.001, 0.474, 0.452, 0.087, 0.243, 0.326, 0.299, 0.303, ...]
        lisa_num_nbrs(): [4, 6, 6, 4, 3, 7, 3, 3, 5, 5, ...]
        lisa_clusters(): [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ...]
        lisa_labels(): ('Not significant', 'High-High', 'Low-Low', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#FF0000', '#0000FF', '#464646', '#999999')


6.5 Local Join Count
--------------------

Local Join Count is a method to identify local clusters
for binary data by using a local version of the so-called
BB join count statistic. The statistic is only meaningful
for those observations with value 1. For more details, please read 
http://geodacenter.github.io/workbook/6d_local_discrete/lab6d.html

For example, we can create a binary data manually by using the quantile 
breaks and the variable `Crm_prp`:
::

    >>> top_crmprp = [1 if i > 9584.5 else 0 for i in guerry['Crm_prp']]
    >>> top_crmprp
    [1, 0, 0, 0, 0, 1, ...]

If you are using geopandas, you can create such a variable using:
::

    >>> gdf = geopandas.read_file('./data/Guerry.shp')
    >>> top_crmprp = gdf['Crm_prp'] > 9584.5

Then, we can apply the function `local_joincount()` using a Queen weights and
the data “top_crmprp”:
::

    >>> ljc_topcrmprp = pygeoda.local_joincount(queen_w, top_crmprp)
    >>> ljc_topcrmprp
    lisa object:
        lisa_values(): [1.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 1.0, 0.0, 2.0, ...]
        lisa_pvalues(): [0.419, nan, nan, nan, nan, 0.376, nan, 0.442, nan, 0.257, ...]
        lisa_num_nbrs(): [4, 6, 6, 4, 3, 7, 3, 3, 5, 5, ...]
        lisa_clusters(): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...]
        lisa_labels(): ('Not significant', 'Significant', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#348124', '#464646', '#999999')

To get the number of neighbors of the local Join Count computation:
::

    >>> nn = ljc_topcrmprp.lisa_num_nbrs()
    >>> print(nn[:20])
    (4, 6, 6, 4, 3, 7, 3, 3, 5, 5, 7, 3, 3, 6, 5, 5, 6, 6, 7, 3)

6.6 Local Bivariate Join Count
----------------------------------------------

For demonstration of local bivariate or no-colocation join count, we create another binary data 
manually:
::

    >>> top_lit = [1 if i > 54.999999999999986 else 0 for i in guerry['Litercy']]

With no-colocation, two binary events can not be 1 at the same location.
::

    >>> top_lit
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    >>> top_crmprp
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

.. note::
    In case of co-location, a warning message will be raised "The bivariate local join count only applies on two variables with no-colocation." 
    , and one can use pygeoda.local_multijoincount() for co-location case.

Then, we can apply the function `local_bijoincount()`:
::

    >>> lbjc_topcrm_lit = pygeoda.local_bijoincount(queen_w, [topcrm, toplit])
    >>> lbjc_topcrm_lit
    lisa object:
        lisa_values(): [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...]
        lisa_pvalues(): [0.397, nan, nan, nan, nan, nan, nan, nan, nan, nan, ...]
        lisa_num_nbrs(): [4, 6, 6, 4, 3, 7, 3, 3, 5, 5, ...]
        lisa_clusters(): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...]
        lisa_labels(): ('Not significant', 'Significant', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#348124', '#464646', '#999999')

6.7 Local Multivariate Join Count
-----------------------------------------------

With co-location, both binary events have to be 1 at the same location more than once. 
For demonstration, we create the third binary data manually, and using the 3 binary data
together for the case of co-location:
::

    >>> top_infant = [1 if i > 10712.499999999996 else 0 for i in guerry['Donatns']]
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
    >>> lmjc = pygeoda.local_multijoincount(queen_w, [topcrm, toplit, topdon])


6.8 Quantile LISA
-----------------

The quantile local spatial autocorrelation converte the continuous variable 
to a binary variable that takes the value of 1 for a specific quantile. 
Then appaly a local join count to the data converted. Two input parameters, k and q,
need to be specified in the function `pygeoda.quantile_lisa()`: k is the number of quantiles 
(k > 2), and the q is the index of selected quantile lisa 
ranging from 1 to k.

For example, the examples in section 6.5 can be simply implemented as
::

    >>> ql = pygeoda.quantile_lisa(queen_w, crm_prp, 5, 5)
    lisa object:
        lisa_values(): [1.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 1.0, 0.0, 2.0, ...]
        lisa_pvalues(): [0.419, nan, nan, nan, nan, 0.376, nan, 0.442, nan, 0.257, ...]
        lisa_num_nbrs(): [4, 6, 6, 4, 3, 7, 3, 3, 5, 5, ...]
        lisa_clusters(): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...]
        lisa_labels(): ('Not significant', 'Significant', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#348124', '#464646', '#999999')


6.9 Multivariate Quantile LISA
------------------------------

For multiple variables, the Quantile LISA can automatiaclly detect if it is the case of
no-colocation, in which local_bijoincount() will be called internally, or the case of 
co-location, in which local_multijoincount() will be called internally.

For exmaple, the example in section 6.6 can be implemented using multivariate quantile lisa:
::

    >>> bql = pygeoda.local_multiquantilelisa(queen_w, [crm_prp, guerry['Litercy']], [5,5], [5,5])
    >>> bql
    lisa object:
        lisa_values(): [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...]
        lisa_pvalues(): [0.397, nan, nan, nan, nan, nan, nan, nan, nan, nan, ...]
        lisa_num_nbrs(): [4, 6, 6, 4, 3, 7, 3, 3, 5, 5, ...]
        lisa_clusters(): [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...]
        lisa_labels(): ('Not significant', 'Significant', 'Undefined', 'Isolated')
        lisa_colors(): ('#eeeeee', '#348124', '#464646', '#999999')

6.10 Neighbor Match Test
------------------------

The local neighbor match test is to assess the extent of overlap between 
k-nearest neighbors in geographical space and k-nearest neighbors in 
multi-attribute space.

For example, to apply the Neighbor Match Test on 6 variables: 
'Crm_prs','Crm_prp','Litercy','Donatns','Infants','Suicids' in multi-attribute space
and k=6 nearest neighbors in geographical space:
::

    >>> data = guerry[['Crm_prs','Crm_prp','Litercy','Donatns','Infants','Suicids']]
    >>> nm = pygeoda.neighbor_match_test(guerry, data, 6)
    >>> nm
    {'Cardinality': [2, 3,  ...],
     'Probability': [0.05263799873777295, 0.0037431465769082986, ...]
    }

`pygeoda.neighbor_match_test()` function returns a dict which has two keys "Cardinality" and "Probability".
