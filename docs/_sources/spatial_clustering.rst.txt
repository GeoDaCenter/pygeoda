.. _spatial_clustering_ref:

.. currentmodule:: pygeoda

6 Spatial Clustering
====================

Spatial clustering aims to group of a large number of
geographic areas or points into a smaller number of regions
based on similiarities in one or more variables.
Spatially constrained clustering is needed when clusters are
required to be spatially contiguous.

In pygeoda v0.0.4, there are three different approaches
explicitly incorporate the contiguity constraint in the
optimization process: SKATER, Redcap and Max-p.
More more details, please read the lab note that
Dr. Luc Anselin wrote:
http://geodacenter.github.io/workbook/8_spatial_clusters/lab8.html 

For example, to apply spatial clustering on the Guerry dataset,
we use the queen weights to define the spatial contiguity
and select 6 variables for similarity measure:
"Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids".

The following code is used to get a 2D data list for
the selected variables:
::

    >>> select_vars = ["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]
    >>> data = [guerry.GetRealCol(v) for v in select_vars]
    >>> data


6.1 SKATER
----------

The Spatial C(K)luster Analysis by Tree Edge Removal(SKATER)
algorithm introduced by Assuncao et al. (2006) is based on
the optimal pruning of a minimum spanning tree that reflects
the contiguity structure among the observations. It provides
an optimized algorithm to prune to tree into several clusters
that their values of selected variables are as similar as possible.

The SKATER function in pygeoda:
::

    pygeoda.skater(k, w, data, distance_method='euclidean', bound_vals = [],  min_bound = 0, random_seed=123456789)

.. note::
    The parameters `distance_method`, `bound_vals`, `min_bound` and `random_seed` are optional.

.. note::
    See [Max-p] for the usage of  `bound_vals` and `min_bound`.

For example, to create 4 spatially contiguous clusters using
`skater()` with Guerry dataset, the queen weights and the
values of the 6 selected variables:
::

    >>> skater_clusters = pygeoda.skater(4, queen_w, data)
    >>> print(skater_clusters)
    ((15, 74, 16, 55, 60, 39, 68, 33, 17, 82, 81, 0, 2, 40, 20, 80), (46, 50, 34, 38, 69, 47, 58, 19, 32, 41, 53, 26), (23, 79, 3, 29, 61, 21, 44, 11, 28, 13, 30, 35, 76, 77, 43, 9, 27, 45, 31, 78, 4, 10, 66, 37, 5, 14, 7, 63, 62), (49, 52, 72, 84, 8, 57, 56, 59, 42, 1, 25, 51, 48, 54, 64, 75, 18, 83, 73, 36, 24, 71, 6, 67, 65, 70, 22, 12))

This `skater()` function returns a 2D list, which represents
4 clusters. Each cluster is composed by several contiguity areas,
e.g. 15, 74, 16, 55, 60, 39, 68, 33, 17, 82, 81, 0, 2, 40, 20, 80

pygeoda also provides utility functions to compute some descriptive
statistics of the clustering results, e.g. to compute the ratio
of between to total sum of squares:
::

    >>> betweenss <- between_sumofsquare(skater_clusters, data)
    >>> totalss <- total_sumofsquare( data)
    >>> ratio <-  betweenss / totalss
    >>> print("The ratio of between to total sum of square:", ratio)
    The ratio of between to total sum of square: 0.3156446659311204
 


6.2 REDCAP
----------

REDCAP (Regionalization with dynamically constrained agglomerative
clustering and partitioning) is developed by D. Guo (2008).
Like SKATER, REDCAP starts from building a spanning tree with
3 different ways (single-linkage, average-linkage, and the complete-linkage).
The single-linkage way leads to build a minimum spanning tree.
Then,REDCAP provides 2 different ways (first‐order and full-order
constraining) to prune the tree to find clusters. The first-order
approach with a minimum spanning tree is exactly the same with SKATER.
In GeoDa and pygeoda, the following methods are provided:

* First-order and Single-linkage
* Full-order and Complete-linkage
* Full-order and Average-linkage
* Full-order and Single-linkage

For example, to find 4 clusters using the same dataset and weights
as above using REDCAP with Full-order and Complete-linkage method:
::

    >>> redcap_clusters = pygeoda.redcap(4, queen_w, data, "fullorder-completelinkage")
    >>> print(redcap_clusters)
    ((15, 74, 16, 55, 60, 39, 68, 33, 17, 82, 81, 0, 2, 40, 20, 80), (46, 50, 34, 38, 69, 47, 58, 19, 32, 41, 53, 26), (23, 79, 3, 29, 61, 21, 44, 11, 28, 13, 30, 35, 76, 77, 43, 9, 27, 45, 31, 78, 4, 10, 66, 37, 5, 14, 7, 63, 62), (49, 52, 72, 84, 8, 57, 56, 59, 42, 1, 25, 51, 48, 54, 64, 75, 18, 83, 73, 36, 24, 71, 6, 67, 65, 70, 22, 12))
    >>> betweenss = between_sumofsquare(redcap_clusters, data)
    >>> totalss = total_sumofsquare( data)
    >>> ratio = betweenss / totalss
    >>> print("The ratio of between to total sum of square:", ratio)
    The ratio of between to total sum of square: 0.1905641377254551


6.3 Max-p
---------

The so-called max-p regions model (outlined in Duque, Anselin, and Rey 2012)
uses a different approach and considers the regionalization problem as
an application of integer programming. In addition, the number of regions
is determined endogenously.

The algorithm itself consists of a search process that starts with an
initial feasible solution and iteratively improves upon it while
maintaining contiguity among the elements of each cluster. 
Like Geoda, pygeoda provides three different heuristic algorithms to
find an optimal solution for max-p:

* greedy
* Tabu Search
* Simulated Annealing

Unlike SKATER and REDCAP that one can specify the number of clusters
as an input paramter, max-p doesn't allow to specify the number of
clusters explicitly, but a constrained variable and the minimum bounding
value that each cluster should reach that are used to find an optimized
number of clusters.

For example, to use `greedy` algorithm in maxp function with the same
dataset and weights as above to find optimal clusters using max-p:

First, we need to specify, for example, every cluster must have
population >= 3236.67 thousands people:
::

    >>> bound_vals = guerry.GetRealCol("Pop1831")
    >>> min_bound = 3236.67 # 10% of Pop1831
    >>> print(bound_vals)
    (346.03, 513.0, 298.26, 155.9, 129.1, 340.73, 289.62, 253.12, 246.36, 270.13, 359.06, 359.47, 494.7, 258.59, 362.53, 445.25, 256.06, 294.83, 375.88, 598.87, 265.38, 482.75, 265.54, 299.56, 424.25, 278.82, 524.4, 357.38, 427.86, 312.16, 554.23, 346.3, 547.05, 245.29, 297.02, 550.26, 312.5, 281.5, 235.75, 391.22, 292.08, 470.09, 305.28, 283.83, 346.89, 140.35, 467.87, 591.28, 337.08, 249.83, 352.59, 415.57, 314.59, 433.52, 417.0, 282.52, 989.94, 397.73, 441.88, 655.22, 573.11, 428.4, 233.03, 157.05, 540.21, 424.26, 434.43, 338.91, 523.97, 457.37, 935.11, 693.68, 323.89, 448.18, 297.85, 543.7, 333.84, 242.51, 317.5, 239.11, 330.36, 282.73, 285.13, 397.99, 352.49)


Then, we can call the max-p function with "greedy" algorithm,
the bound values and minimum bound value:
::

    >>> maxp_clusters = pygeoda.maxp(queen_w, data, bound_vals, min_bound, "greedy")
    >>> betweenss = pygeoda.between_sumofsquare(maxp_clusters, data)
    >>> ratio = betweenss / totalss
    >>> print("The ratio of between to total sum of square:", ratio)
    The ratio of between to total sum of square: 0.507018079733202

We can also specify using `tabu search` algorithm in maxp function
with the parameter of tabu length:
::

    >>> maxp_tabu_clusters = maxp(queen_w, data, bound_vals, min_bound, "tabu", tabu_length=95)
    >>> betweenss = between_sumofsquare(maxp_tabu_clusters, data)
    >>> ratio = betweenss / totalss
    >>> print("The ratio of between to total sum of square:", ratio)
    The ratio of between to total sum of square: 0.5280299052291919


To apply `simulated annealing` algorithm in maxp function with
the parameter of cooling rate:
::

    >>> maxp_sa_clusters = maxp(queen_w, data, bound_vals, min_bound, "sa", cool_rate=0.75)
    >>> betweenss <- between_sumofsquare(maxp_sa_clusters, data)
    >>> ratio <- betweenss / totalss
    >>> print("The ratio of between to total sum of square:", ratio)
    The ratio of between to total sum of square: 0.5260248902417842


We can also increase the number of iterations for local search process by specifying the parameter `initial` (default value is 99):
::

    >>> maxp_clusters = pygeoda.maxp(queen_w, data, bound_vals, min_bound, "greedy", initial=1000)
    >>> betweenss = pygeoda.between_sumofsquare(maxp_clusters, data)
    >>> ratio = betweenss / totalss
    >>> print("Tratio of between to total sum of square:", ratio)
    The ratio of between to total sum of square: 0.5260248902417843
