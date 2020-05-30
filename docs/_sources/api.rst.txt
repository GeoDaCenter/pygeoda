.. _api_ref:

.. currentmodule:: pygeoda

pygeoda API reference
======================

pygeoda (I/O)
-------------

.. autosummary::
   :toctree: generated/

   pygeoda.open
   pygeoda.geopandas_to_geoda
   pygeoda.geoda_to_geopandas
   pygeoda.geoda


pygeoda.weights
---------------

.. autosummary::
   :toctree: generated/

   pygeoda.weights.Weight
   pygeoda.weights.queen
   pygeoda.weights.rook
   pygeoda.weights.distance
   pygeoda.weights.knn
   pygeoda.weights.kernel


pygeoda (spatial autocorrelation)
---------------------------------

.. autosummary::
   :toctree: generated/

   pygeoda.lisa
   pygeoda.batchlisa
   pygeoda.local_moran
   pygeoda.batch_local_moran
   pygeoda.local_geary
   pygeoda.local_multigeary
   pygeoda.local_joincount
   pygeoda.local_multijoincount
   pygeoda.local_g
   pygeoda.local_gstar
   pygeoda.quantile_lisa


pygeoda (spatial clustering)
----------------------------

.. autosummary::
   :toctree: generated/

   pygeoda.skater
   pygeoda.redcap
   pygeoda.maxp
   pygeoda.between_sumofsquare
   pygeoda.total_sumofsquare
   pygeoda.within_sumofsquare


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

   pygeoda.mds
   pygeoda.PCA