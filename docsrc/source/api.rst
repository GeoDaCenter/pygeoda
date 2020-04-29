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
   pygeoda.local_moran
   pygeoda.local_geary
   pygeoda.local_joincount
   pygeoda.local_g
   pygeoda.local_gstar


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
