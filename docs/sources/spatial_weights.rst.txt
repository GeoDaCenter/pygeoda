.. _spatial_weights_ref:

.. currentmodule:: pygeoda

4 Spatial Weights
=================

Spatial weights are central components in spatial data analysis.
The spatial weights represents the possible spatial interaction
between observations in space. Like GeoDa desktop software,
pygeoda provides a rich variety of methods to create several
different types of spatial weights:

* Contiguity Based Weights: `queen_weights()`, `rook_weights()`
* Distance Based Weights: `distance_weights()`
* K-Nearest Neighbor Weights: `knn_weights()`
* Kernel Weights: `kernel_weights()`

4.1 Queen Contiguity Weights
----------------------------

To create a Queen contiguity weights, we can call pygeoda's function
::

    pygeoda.weights.queen(gda, order=1, include_lower_order = False, precision_threshold = 0)

by passing the GeoDa object `guerry` we just created:
::

    >>> queen_w = pygeoda.weights.queen(guerry)
    >>> print(queen_w)
    Weights Meta-data:

    is symmetric:True
    sparsity:0.0
    density:5.813148788927336
    min neighbors:2
    mean neighbors:4.9411764705882355
    median neighbors:5.0
    max neighbors:8


The function `queen_weights()` returns an instance of
`Weight` object. One can access the meta data of the spatial
weights by accessing the attributes of `Weight` object:

4.2 Attributes of `Weight` object
---------------------------------

* num_obs
* GetWeightsType() 
* IsSymmetric()
* HasIsolates()
* GetSparsity()
* GetMinNbrs()
* GetMedianNbrs()
* GetMeanNbrs()
* GetMaxNbrs()
* GetDensity()
* [] GetNeighbors(idx)
* double SpatialLag(idx, [data])
* SaveToFile()

We can also access the details of the weights: e.g.
list the neighbors of a specified observation, which
is very helpful in exploratory spatial data analysis
::

    >>> nbrs = queen_w.GetNeighbors(0)
    >>> print("Neighbors of 0-st observation are:", nbrs)
    Neighbors of 0-st observation are: (35, 36, 66, 68)

We can also compute the spatial lag of a specified
observation by passing the values of the selected variable:
::

    >>> lag0 = queen_w.SpatialLag(0, crm_prp)
    >>> print("Spatial lag of 0-st observation is:", lag0)
    Spatial lag of 0-st observation is: 7899.25


4.3 Rook Contiguity Weights
---------------------------

To create a Rook contiguity weights, we can call pygeoda's function
::

    rook_weights(gda, order=1,include_lower_order=False, precision_threshold = 0)

by passing the geoda object `guerry` we just created:
::

    >>> rook_w = geoda.rook_weights(guerry)
    >>> print(rook_w)
    Weights Meta-data:

    is symmetric:True
    sparsity:0.0
    density:5.813148788927336
    min neighbors:2
    mean neighbors:4.9411764705882355
    median neighbors:5.0
    max neighbors:8

The weights we created are in memory, which makes it straight
forward for spatial data analysis and also are good for
programming your application. To save the weights to a file,
we can call Weight's function
::

    SaveToFile(ofname, layer_name, id_name, id_vec)

The `layer_name` is the layer name of loaded dataset. For a ESRI shapefile,
the layer name is the file name without the suffix (e.g. Guerry).

The `id_name` is a key (column name), which means the associated column
contains unique values, that makes sure that the weights are connected
to the correct observations in the data table.

The `id_vec` is the actual column data of `id_name`, it could be a tuple
of integer or string values.

For example, in Guerry dataset, the column "CODE_DE" can be used as a key
to save a weights file:
::

    >>> rook_w.SaveToFile('./Guerry_r.gal', 'Guerry', 'CODE_DE', guerry.GetIntegerCol('CODE_DE'))
    True

Then, we should find the file "Guerry_r.gal" in the output directory.

4.4 Distance Based Weights
--------------------------

To create a Distance based weights, we can call pygeoda's function
::

    pygeoda.weights.distance_weights(gda, dist_thres, power=1.0,  is_inverse=False, is_arc=False, is_mile=True)

by passing the geoda object `guerry` we just created and the value
of distance threshold. Like GeoDa, pygeoda provides a function to
help you find a optimized distance threshold that guarantees that
every observation has at least one neighbor:
::

    pygeoda.weights.min_distthreshold(GeoDa gda, bool is_arc = False, bool is_mile = True)

::

    >>> dist_thres = pygeoda.weights.min_distthreshold(guerry)
    >>> dist_w = pygeoda.weights.distance_weights(guerry, dist_thres)
    >>> print(dist_w)
    Weights Meta-data:

    is symmetric:False
    sparsity:0.0
    density:4.346020761245675
    min neighbors:1
    mean neighbors:3.6941176470588237
    median neighbors:4.0
    max neighbors:7

4.5 K-Nearest Neighbor Weights
------------------------------

A special case of distance based weights is K-Nearest neighbor
weights, in which every obersvation will have exactly k
neighbors. To create a KNN weights, we can call pygeoda's function:
::

    pygeoda.weights.knn_weights(gda, k, power = 1.0,is_inverse = False, is_arc = False, is_mile = True)

For example, to create a 6-nearest neighbor weights using Guerry dataset:
::

    >>> knn6_w = pygeoda.weights.knn_weights(guerry, 6)
    >>> print(knn6_w)
    Weights Meta-data:

    is symmetric:False
    sparsity:0.0
    density:7.0588235294117645
    min neighbors:6
    mean neighbors:6.0
    median neighbors:6.0
    max neighbors:6

4.6 Kernel Weights
------------------

Kernel weights apply kernel function to determine the distance
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

4.6.1 Kernel Weights with fixed bandwidth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a kernel weights with fixed bandwith:
::

    >>> kernel_w = pygeoda.weights.kernel_weights(guerry, dist_thres, "uniform")
    >>> print(kernel_w)
    Weights Meta-data:

    is symmetric:False
    sparsity:0.0
    density:4.346020761245675
    min neighbors:1
    mean neighbors:3.6941176470588237
    median neighbors:4.0
    max neighbors:7

Besides the options `is_inverse`, `power`, `is_arc` and
`is_mile` that are the same with the distance based weights,
this kernel weights function has another option:
::

    use_kernel_diagonals
    (optional) FALSE (default) or TRUE, apply kernel on the
    diagonal of weights matrix


4.6.2 Kernel Weights with adaptive bandwidth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a kernel weights with adaptive bandwidth or using
max KNN distance as bandwidth:
::

    >>> adptkernel_w = pygeoda.weights.kernel(guerry, 6, "uniform")
    >>> print(adptkernel_w)
    Weights Meta-data:

    is symmetric:False
    sparsity:0.0
    density:7.0588235294117645
    min neighbors:6
    mean neighbors:6.0
    median neighbors:6.0
    max neighbors:6

This kernel weights function two more options:
::

    adaptive_bandwidth
    (optional) TRUE (default) or FALSE: TRUE use adaptive bandwidth
    calculated using distance of k-nearest neithbors, FALSE use max
    distance of all observation to their k-nearest neighbors

    use_kernel_diagonals
    (optional) FALSE (default) or TRUE, apply kernel on the diagonal
    of weights matrix

