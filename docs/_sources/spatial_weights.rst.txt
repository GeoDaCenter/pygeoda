.. _spatial_weights_ref:

.. currentmodule:: pygeoda

5 Spatial Weights
=================

Spatial weights are a key component in any cross-sectional analysis of 
spatial dependence. They are an essential element in the construction of 
spatial autocorrelation statistics, and provide the means to create 
spatially explicit variables, such as spatially lagged variables and spatially smoothed rates.

The spatial weights represents the possible spatial interaction
between observations in space. Like GeoDa desktop software,
pygeoda provides a rich variety of methods to create several
different types of spatial weights:

* Contiguity Based Weights: `queen_weights()`, `rook_weights()`
* Distance Based Weights: `distance_weights()`
* K-Nearest Neighbor Weights: `knn_weights()`
* Kernel Weights: `kernel_weights()`

5.1 Queen Contiguity Weights
----------------------------

To create a Queen contiguity weights, we can call pygeoda's function
::

    pygeoda.queen_weights(gda, order=1, include_lower_order = False, precision_threshold = 0)

by passing the geoda object `guerry` created using `pygeoda.open()`:
::

    >>> queen_w = pygeoda.queen_weights(guerry)
    >>> queen_w
    Weights Meta-data:
     number of observations:                   85
               is symmetric:                 True
                   sparsity:  0.05813148788927336
            # min neighbors:                    2
            # max neighbors:                    8
           # mean neighbors:   4.9411764705882355
         # median neighbors:                  5.0
               has isolates:                False


The function `queen_weights()` returns an instance of
`Weight` object. One can access the meta data of the spatial
weights by accessing the attributes of `Weight` object:

5.2 Attributes of `Weight` object
---------------------------------

* num_obs
* is_symmetric()
* has_isolates()
* weights_sparsity()
* min_neighbors()
* median_neighbors()
* mean_neighbors()
* max_neighbors()
* get_neighbors()
* spatial_lag()
* save_weights()

We can access the details of the weights: e.g.
get the neighbors of a specified observation, which
is useful in exploratory spatial data analysis
::

    >>> nbrs = queen_w.get_neighbors(0)
    >>> print("Neighbors of 0-st observation are:", nbrs)
    Neighbors of 0-st observation are: (35, 36, 66, 68)

We can also compute the spatial lag of a specified
observation by passing the values of the selected variable:
::

    >>> lag = queen_w.SpatialLag(guerry['Crm_prp'])
    >>> print("Spatial lagged values of Crm_prp:", lag)
    Spatial lagged values of Crm_prp: [7899.25, 6593.5,...]


5.3 Rook Contiguity Weights
---------------------------

To create a Rook contiguity weights, we can call pygeoda's function
::

    rook_weights(gda, order=1, include_lower_order=False, precision_threshold = 0)

by passing the geoda object `guerry` we just created:
::

    >>> rook_w = geoda.rook_weights(guerry)
    >>> print(rook_w)
    Weights Meta-data:
     number of observations:                   85
               is symmetric:                 True
                   sparsity:  0.05813148788927336
            # min neighbors:                    2
            # max neighbors:                    8
           # mean neighbors:   4.9411764705882355
         # median neighbors:                  5.0
               has isolates:                False

To save the weights to a file, we can call pygeoda's function
::

    save_weights(ofname, layer_name, id_name, id_vec)

The `layer_name` is the layer name of loaded dataset. For a ESRI shapefile,
the layer name is the file name without the suffix (e.g. Guerry).

The `id_name` is a key column, which contains unique values to represent observations.

The `id_vec` is the actual column data of `id_name`, it could be a tuple
of integer or string values.

For example, in Guerry dataset, the column "CODE_DE" can be used as a key
to save a weights file:
::

    >>> rook_w.save_weights('./Guerry_r.gal', 'Guerry', 'CODE_DE', guerry['CODE_DE'])
    True

Then, we should find the file "Guerry_r.gal" in the output directory.

5.4 Distance Based Weights
--------------------------

To create a Distance based weights, we can call pygeoda's function
::

    pygeoda.distance_weights(gda, dist_thres, power=1.0,  is_inverse=False, is_arc=False, is_mile=True)

by passing the geoda object `guerry` we just created and the value
of distance threshold. Like GeoDa, pygeoda provides a function to
help you find a optimized distance threshold that guarantees that
every observation has at least one neighbor:
::

    pygeoda.min_distthreshold(GeoDa gda, bool is_arc = False, bool is_mile = True)

::

    >>> dist_thres = pygeoda.min_distthreshold(guerry)
    >>> dist_w = pygeoda.distance_weights(guerry, dist_thres)
    >>> dist_w
    Weights Meta-data:
     number of observations:                   85
               is symmetric:                 True
                   sparsity: 0.043460207612456746
            # min neighbors:                    1
            # max neighbors:                    7
           # mean neighbors:   3.6941176470588237
         # median neighbors:                  4.0
               has isolates:                False

5.5 K-Nearest Neighbor Weights
------------------------------

A special case of distance based weights is K-Nearest neighbor
weights, in which every obersvation will have exactly k
neighbors. To create a KNN weights, we can call pygeoda's function:
::

    pygeoda.weights.knn_weights(gda, k, power = 1.0,is_inverse = False, is_arc = False, is_mile = True)

For example, to create a 6-nearest neighbor weights using Guerry dataset:
::

    >>> knn6_w = pygeoda.knn_weights(guerry, 6)
    >>> print(knn6_w)
    Weights Meta-data:
     number of observations:                   85
               is symmetric:                False
                   sparsity:  0.07058823529411765
            # min neighbors:                    6
            # max neighbors:                    6
           # mean neighbors:                  6.0
         # median neighbors:                  6.0
               has isolates:                False

5.6 Kernel Weights
------------------

Kernel Weights applies kernel function to determine the distance
decay in the derived continuous weights kernel. The kernel weights
are defined as a function K(z) of the ratio between the distance
dij from i to j, and the bandwidth hi, with z=dij/hi.

The kernl functions include:
* triangular
* uniform
* quadratic
* epanechnikov
* quartic
* gaussian

Two functions are provided in pygeoda to create kernel weights:

5.6.1 Kernel Weights with fixed bandwidth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a kernel weights with fixed bandwith:
::

    >>> kernel_w = pygeoda.kernel_weights(guerry, dist_thres, "uniform")
    >>> print(kernel_w)
    Weights Meta-data:
     number of observations:                   85
               is symmetric:                False
                   sparsity: 0.043460207612456746
            # min neighbors:                    1
            # max neighbors:                    7
           # mean neighbors:   3.6941176470588237
         # median neighbors:                  4.0
               has isolates:                False

Besides the options `is_inverse`, `power`, `is_arc` and
`is_mile` that are the same with the distance based weights,
this kernel weights function has another option:
::

    use_kernel_diagonals
    (optional) FALSE (default) or TRUE, apply kernel on the
    diagonal of weights matrix


5.6.2 Kernel Weights with adaptive bandwidth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a kernel weights with adaptive bandwidth or using
max KNN distance as bandwidth:
::

    >>> adptkernel_w = pygeoda.kernel_knn_weights(guerry, 6, "uniform")
    >>> print(adptkernel_w)
    Weights Meta-data:
     number of observations:                   85
               is symmetric:                False
                   sparsity:  0.07058823529411765
            # min neighbors:                    6
            # max neighbors:                    6
           # mean neighbors:                  6.0
         # median neighbors:                  6.0
               has isolates:                False

This kernel weights function two more options:
::

    adaptive_bandwidth
    (optional) TRUE (default) or FALSE: TRUE use adaptive bandwidth
    calculated using distance of k-nearest neithbors, FALSE use max
    distance of all observation to their k-nearest neighbors

    use_kernel_diagonals
    (optional) FALSE (default) or TRUE, apply kernel on the diagonal
    of weights matrix

