.. _spatial_clustering_ref:

.. currentmodule:: pygeoda

6 Spatial Clustering
====================

Spatial clustering aims to group of a large number of
geographic areas or points into a smaller number of regions
based on similiarities in one or more variables.
Spatially constrained clustering is needed when clusters are
required to be spatially contiguous.

In pygeoda, there are three different approaches
explicitly incorporate the contiguity constraint in the
optimization process: SKATER, Redcap and Max-p.
For more details, please read: 
* http://geodacenter.github.io/workbook/9c_spatial3/lab9c.html
* http://geodacenter.github.io/workbook/9d_spatial4/lab9d.html

For example, to apply spatial clustering on the Guerry dataset,
we use the queen weights to define the spatial contiguity
and select 6 variables for similarity measure:
"Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids":
::

    >>> data = guerry[["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]]
    >>> data


7.1 SKATER
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
    >>> skater_clusters
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': [57.890768263715266,
    59.95241669262987,
    28.725706194374844,
    69.3802999471999,
    62.30781060793979,
    66.65808666485573],
    'Total within-cluster sum of squares': 159.0849116292847,
    'The ratio of between to total sum of squares': 0.3156446659311204,
    'Clusters': (3, 2, 3, 1, 1, 1, 2, 1,...)
    }

This skater() function returns a names list with names “Clusters”, 
“Total sum of squares”, “Within-cluster sum of squares”, 
“Total within-cluster sum of squares”, and “The ratio of between 
to total sum of squares”.


7.2 REDCAP
----------

REDCAP (Regionalization with dynamically constrained agglomerative
clustering and partitioning) is developed by D. Guo (2008).
Like SKATER, REDCAP starts from building a spanning tree with
4 different ways (single-linkage, average-linkage, complete-linkage and wards-linkage).
Then,REDCAP provides 2 different ways (first‐order and full-order
constraining) to prune the tree to find clusters. The first-order
approach with a minimum spanning tree is exactly the same with SKATER.
In GeoDa and pygeoda, the following methods are provided:

* First-order and Single-linkage
* Full-order and Complete-linkage
* Full-order and Average-linkage
* Full-order and Single-linkage
* Full-order and Wards-linkage

For example, to find 4 clusters using the same dataset and weights
as above using REDCAP with Full-order and Complete-linkage method:
::

    >>> redcap_clusters = pygeoda.redcap(4, queen_w, data, "fullorder-completelinkage")
    >>> redcap_clusters
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': [59.33033487635985,
    55.0157958268228,
    28.202717566163827,
    68.5897406247226,
    61.2723190783986,
    54.63519052499109],
    'Total within-cluster sum of squares': 176.95390150254138,
    'The ratio of between to total sum of squares': 0.35109901091774076,
    'Clusters': (1, 2, 1, 3, 3, 1, 2,...)
    }

7.3 Spatially Constrained Hierarchical Clucstering
--------------------------------------------------

Spatially constrained hierarchical clustering is a special form of constrained clustering, 
where the constraint is based on contiguity (common borders). The method builds up the 
clusters using agglomerative hierarchical clustering methods: single linkage, 
complete linkage, average linkage and Ward's method (a special form of centroid linkage). 
Meanwhile, it also maintains the spatial contiguity when merging two clusters.

For example, to find 4 spatially constrained clusters using the same dataset and weights
as above using Complete-linkage method:
::

    >>> schc_clusters = pygeoda.schc(4, queen_w, data, "complete")
    >>> schc
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': [78.13831458170165,
    54.758683422512384,
    81.49770916157574,
    63.48674702445253,
    80.60111094248678,
    65.74388628224132],
    'Total within-cluster sum of squares': 79.77354858502969,
    'The ratio of between to total sum of squares': 0.15828085036712236,
    'Clusters': (1,1,1,1,1,1,...)
    }


7.3 AZP
---------

The automatic zoning procedure (AZP) was initially outlined in Openshaw (1977) as 
a way to address some of the consequences of the modifiable areal unit problem 
(MAUP). In essence, it consists of a heuristic to find the best set of 
combinations of contiguous spatial units into p regions, minimizing the 
within-sum of squares as a criterion of homogeneity. The number of regions 
needs to be specified beforehand, as in most other clustering methods considered so far.

pygeoda provides three different heuristic algorithms to find an optimal solution for AZP:

* greedy
* Tabu Search
* Simulated Annealing

7.3.1 AZP greedy
^^^^^^^^^^^^^^^^

The original AZP heuristic is a local optimization procedure that cycles through
 a series of possible swaps between spatial units at the boundary of a set 
 of regions. The process starts with an initial feasible solution, i.e., 
 a grouping of n spatial units into p contiguous regions. This initial 
 solution can be constructed in several different ways. The initial 
 solution must satisfy the contiguity constraints. For example, this 
 can be accomplished by growing a set of contiguous regions from p 
 randomly selected seed units by adding neighboring locations until 
 the contiguity constraint can no longer be met.
::

    >>> azp_clusters = pygeoda.azp_greedy(5, queen_w, data)
    >>> azp_clusters
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': [47.20702629865675,
    60.10164576171729,
    32.71213364540346,
    57.69759599152196,
    59.4167280770582,
    65.49840467351049],
    'Total within-cluster sum of squares': 181.3664655521319,
    'The ratio of between to total sum of squares': 0.3598540983177219,
    'Clusters': (5, 2, 3, 1, 1, 1, ...)
    }

7.3.2 AZP Simulated Annealing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To call AZP simulate annealing algorithm, one needs to specify cooling_rate (default: 0.85):
::

    >>> azp_clusters = pygeoda.azp_sa(5, queen_w, data, cooling_rate=0.85)
    >>> azp_clusters
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': [55.44537005496083,
    44.49165717470521,
    31.26639087099905,
    44.79845917679877,
    61.49413146833172,
    54.251299642381724],
    'Total within-cluster sum of squares': 212.25269161182268,
    'The ratio of between to total sum of squares': 0.42113629288060045,
    'Clusters': (5, 2, 5, 1, 1, 1, 2, 1, ...}
    }

7.3.3 AZP Tabu Search
^^^^^^^^^^^^^^^^^^^^^

To call AZP Tabu search algorithm, one needs to specify tabu_length (deafult: 10) , 
or conv_tabu (default: 10):
::

    >>> azp_clusters = pygeoda.azp_tabu(5, queen_w, data, tabu_length = 10, conv_tabu = 10)
    >>> azp_clusters
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': [52.20795794704135,
    39.86439151302456,
    30.75532090551626,
    54.95105937296297,
    54.004395690763246,
    59.41930677822133],
    'Total within-cluster sum of squares': 212.79756779247032,
    'The ratio of between to total sum of squares': 0.4222173964136315,
    'Clusters': (4, 1, 2, 3, 3, 3, ...)
    }

.. note::
    NOTE: the AZP algorithm is very sensitive to the initial positions for constructing final solutions.
    Therefore, the random seed, which is used to determine the initial positions, could be used 
    to execute several rounds of max-p algorithms for sensitive analysis.

7.4 Max-p
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

7.4.1 Max-p greedy
^^^^^^^^^^^^^^^^^^

For example, to use `greedy` algorithm in maxp function with the same
dataset and weights as above to find optimal clusters using max-p:

First, we need to specify, for example, every cluster must have
population >= 3236.67 thousands people:
::

    >>> bound_vals = guerry["Pop1831"]
    >>> min_bound = 3236.67 # 10% of Pop1831
    >>> print(bound_vals)
    (346.03, 513.0, 298.26, 155.9, 129.1, 340.73, 289.62, 253.12, 246.36, 270.13, 359.06, 359.47, 494.7, 258.59, 362.53, 445.25, 256.06, 294.83, 375.88, 598.87, 265.38, 482.75, 265.54, 299.56, 424.25, 278.82, 524.4, 357.38, 427.86, 312.16, 554.23, 346.3, 547.05, 245.29, 297.02, 550.26, 312.5, 281.5, 235.75, 391.22, 292.08, 470.09, 305.28, 283.83, 346.89, 140.35, 467.87, 591.28, 337.08, 249.83, 352.59, 415.57, 314.59, 433.52, 417.0, 282.52, 989.94, 397.73, 441.88, 655.22, 573.11, 428.4, 233.03, 157.05, 540.21, 424.26, 434.43, 338.91, 523.97, 457.37, 935.11, 693.68, 323.89, 448.18, 297.85, 543.7, 333.84, 242.51, 317.5, 239.11, 330.36, 282.73, 285.13, 397.99, 352.49)


Then, we can call the max-p function with "greedy" algorithm,
the bound values and minimum bound value:
::

    >>> maxp_clusters = pygeoda.maxp_greedy(queen_w, data, bound_vals, min_bound)
    >>> maxp_clusters
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': [58.53340105931292,
    44.29869690985993,
    26.788351483048764,
    50.6761352058351,
    50.075425319038615,
    46.844568220802984],
    'Total within-cluster sum of squares': 226.7834218021017,
    'The ratio of between to total sum of squares': 0.4499671067502017,
    'Clusters': (4,8,6,3,4,3,...)
    }

7.4.2 Max-p Tabu Search
^^^^^^^^^^^^^^^^^^^^^^^

We can also specify using `Tabu Search` algorithm in maxp function
with the parameter of tabu length:
::

    >>> maxp_tabu_clusters = pygeoda.maxp_tabu(queen_w, data, bound_vals, min_bound,  tabu_length=10, conv_tabu=10)
    >>> maxp_tabu_clusters
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': [41.67029875441199,
    38.07924627625834,
    26.226691715076896,
    52.738669711271385,
    44.51343645827698,
    54.13078236136856],
    'Total within-cluster sum of squares': 246.6408747233359,
    'The ratio of between to total sum of squares': 0.4893668149272537,
    'Clusters': (6,2,6,1,1,6,2,1,3,...)


7.4.3 Max-p Simulated Annealing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To apply `simulated annealing` algorithm in maxp function with
the parameter of cooling rate:
::

    >>> maxp_sa_clusters = pygeoda.maxp_sa(queen_w, data, bound_vals, min_bound, cooling_rate=0.85, sa_maxit=1)
    >>> maxp_sa_clusters
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': [49.54630063745117,
    52.715283326199796,
    31.389297593661983,
    47.57063859231485,
    44.96761523907647,
    46.709112570389934],
    'Total within-cluster sum of squares': 231.10175204090598,
    'The ratio of between to total sum of squares': 0.4585352223033848,
    'Clusters': (2,8,5,2,2,4,8,...)
    }



We can also increase the number of iterations for local search process by specifying the parameter `initial` (default value is 99):
::

    >>> maxp_clusters = pygeoda.maxp_greedy(queen_w, data, bound_vals, min_bound, iterations=199)
    >>> maxp_clusters
    {'Total sum of squares': 504.0000000000001,
    'Within-cluster sum of squares': (50.454710071353645,
    42.41705106362629,
    23.35406627133095,
    52.46200977080593,
    47.809353880636685,
    46.88761433133685),
    'Total within-cluster sum of squares': 240.61519461090978,
    'The ratio of between to total sum of squares': 0.4774111004184717,
    'Clusters': (2,7,4,2,2,2,7,...)
    }

.. note::
    NOTE: the max-p algorithm is very sensitive to the initial positions for constructing final solutions.
    Therefore, the random seed, which is used to determine the initial positions, could be used 
    to execute several rounds of max-p algorithms for sensitive analysis.
