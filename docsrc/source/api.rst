.. _api_ref:

.. currentmodule:: pygeoda

pygeoda API reference
======================

pygeoda (I/O)
-------------

.. autosummary::
   :toctree: generated/

   pygeoda.open
   pygeoda.geoda


pygeoda.weights
---------------

.. autosummary::
   :toctree: generated/

   pygeoda.Weight
   pygeoda.queen_weights
   pygeoda.rook_weights
   pygeoda.min_distthreshold
   pygeoda.distance_weights
   pygeoda.knn_weights
   pygeoda.kernel_weights
   pygeoda.kernel_knn_weights


pygeoda (LISA)
---------------------------------

.. autosummary::
   :toctree: generated/

   pygeoda.lisa
   pygeoda.local_moran
   pygeoda.local_bimoran
   pygeoda.local_geary
   pygeoda.local_multigeary
   pygeoda.local_joincount
   pygeoda.local_bijoincount
   pygeoda.local_multijoincount
   pygeoda.local_g
   pygeoda.local_gstar
   pygeoda.local_quantilelisa
   pygeoda.local_multiquantilelisa
   pygeoda.neighbor_match_test
   pygeoda.batchlisa
   pygeoda.batch_local_moran


pygeoda (spatial clustering)
----------------------------

.. autosummary::
   :toctree: generated/

   pygeoda.skater
   pygeoda.redcap
   pygeoda.schc
   pygeoda.azp_greedy
   pygeoda.azp_sa
   pygeoda.azp_tabu
   pygeoda.maxp_greedy
   pygeoda.maxp_sa
   pygeoda.maxp_tabu
   pygeoda.spatial_validation
   pygeoda.Fragmentation
   pygeoda.Diameter
   pygeoda.Compactness
   pygeoda.JoinCountRatio
   pygeoda.ValidationResult
   pygeoda.make_spatial


pygeoda (classify)
----------------------------

.. autosummary::
   :toctree: generated/

   pygeoda.hinge15_breaks
   pygeoda.hinge30_breaks
   pygeoda.natural_breaks
   pygeoda.quantile_breaks
   pygeoda.percentile_breaks
   pygeoda.stddev_breaks


pygeoda (data)
----------------------------

.. autosummary::
   :toctree: generated/

   pygeoda.demean
   pygeoda.standardize
   pygeoda.mad