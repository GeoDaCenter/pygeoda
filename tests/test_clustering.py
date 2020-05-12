import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestSpatialClustering(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        select_vars = ["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]
        self.data = [self.guerry.GetRealCol(v) for v in select_vars]
        self.bound_vals = self.guerry.GetRealCol("Pop1831")
        self.min_bound = 3236.67 # 10% of Pop1831

    def test_SKATER(self):
        k = 4
        clusters = pygeoda.skater(k, self.queen_w, self.data)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.3156446659311205)

    def test_REDCAP(self):
        k = 4
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "fullorder-completelinkage")
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.25712705781933565)

    def test_MAXP(self):
        method = "greedy"
        clusters = pygeoda.maxp(self.queen_w, self.data, self.bound_vals, self.min_bound, method)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        # todo, should add a n_cpu option for maxp so the result can be replicated in travis
        self.assertAlmostEqual(ratio, 0.5092391813101834)