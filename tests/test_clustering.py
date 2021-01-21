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

    def test_REDCAP_firstsingle(self):
        k = 4
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "firstorder-singlelinkage")
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.3156446659311204)

    def test_REDCAP_fullsingle(self):
        k = 4
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "fullorder-singlelinkage")
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.29002543000953057)

    def test_REDCAP_fullcomplete(self):
        k = 4
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "fullorder-completelinkage")
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.35109901091774076)

    def test_REDCAP_fullaverage(self):
        k = 4
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "fullorder-averagelinkage")
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.30578249025454063)

    def test_REDCAP_fullward(self):
        k = 4
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "fullorder-wardlinkage")
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.379025557025986)

    def test_MAXP_greedy(self):
        clusters = pygeoda.maxp_greedy(self.queen_w, self.data, self.bound_vals, self.min_bound)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.4499671067502017)

    def test_MAXP_sa(self):
        cooling_rate = 0.85
        clusters = pygeoda.maxp_sa(self.queen_w, self.data, self.bound_vals, self.min_bound, cooling_rate)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.4585352223033848)

    def test_MAXP_tabu(self):
        tabu_length = 10
        clusters = pygeoda.maxp_tabu(self.queen_w, self.data, self.bound_vals, self.min_bound, tabu_length)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.4893668149272537)

    def test_AZP_greedy(self):
        p = 4
        clusters = pygeoda.azp_greedy(p, self.queen_w, self.data, self.bound_vals, self.min_bound)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.34772404545345587)

    def test_AZP_sa(self):
        p = 4
        cooling_rate = 0.85
        clusters = pygeoda.azp_sa(p, self.queen_w, self.data, self.bound_vals, self.min_bound, cooling_rate)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.3806147863501549)

    def test_AZP_tabu(self):
        p = 4
        tabu_length = 10
        clusters = pygeoda.azp_tabu(p, self.queen_w, self.data, self.bound_vals, self.min_bound, tabu_length)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.3674042224788964)


    def test_SCHC(self):
        p = 4
        linkage_method = 'ward'
        clusters = pygeoda.schc(p, self.queen_w, self.data, linkage_method)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = pygeoda.total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertAlmostEqual(ratio, 0.3805127681618678)