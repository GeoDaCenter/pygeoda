import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestSpatialClustering(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.queen_weights(self.guerry)
        select_vars = ["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]
        self.data = [self.guerry.GetRealCol(v) for v in select_vars]
        self.bound_variable = self.guerry.GetRealCol("Pop1831")
        self.min_bound = 3236.67 # 10% of Pop1831

    def test_SKATER(self):
        k = 5
        clusters = pygeoda.skater(k, self.queen_w, self.data)

        self.assertAlmostEqual(clusters["Ratio"], 0.3763086809)

    def test_REDCAP_firstsingle(self):
        k = 5
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "firstorder-singlelinkage")

        self.assertAlmostEqual(clusters["Ratio"], 0.3763086808858706)

    def test_REDCAP_fullsingle(self):
        k = 5
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "fullorder-singlelinkage")

        self.assertAlmostEqual(clusters["Ratio"], 0.33931921310113483)

    def test_REDCAP_fullcomplete(self):
        k = 5
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "fullorder-completelinkage")

        self.assertAlmostEqual(clusters["Ratio"], 0.39420885009615186)

    def test_REDCAP_fullaverage(self):
        k = 5
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "fullorder-averagelinkage")

        self.assertAlmostEqual(clusters["Ratio"], 0.3854425827224785)

    def test_REDCAP_fullward(self):
        k = 5
        clusters = pygeoda.redcap(k, self.queen_w, self.data, "fullorder-wardlinkage")

        self.assertAlmostEqual(clusters["Ratio"], 0.42268567324507456)

    def test_MAXP_greedy(self):
        clusters = pygeoda.maxp_greedy(self.queen_w, self.data, self.bound_variable, self.min_bound)

        self.assertAlmostEqual(clusters["Ratio"], 0.4499671068)

    def test_MAXP_sa(self):
        cooling_rate = 0.85
        clusters = pygeoda.maxp_sa(self.queen_w, self.data, self.bound_variable, self.min_bound, cooling_rate)

        self.assertAlmostEqual(clusters["Ratio"], 0.4585352223)

    def test_MAXP_tabu(self):
        tabu_length = 10
        clusters = pygeoda.maxp_tabu(self.queen_w, self.data, self.bound_variable, self.min_bound, tabu_length)

        self.assertAlmostEqual(clusters["Ratio"], 0.4893668149)

    def test_AZP_greedy(self):
        p = 5
        clusters = pygeoda.azp_greedy(p, self.queen_w, self.data)

        self.assertAlmostEqual(clusters["Ratio"], 0.3598540983177219)

    def test_AZP_sa(self):
        p = 5
        cooling_rate = 0.85
        clusters = pygeoda.azp_sa(p, self.queen_w, self.data, cooling_rate)

        self.assertAlmostEqual(clusters["Ratio"], 0.42113629288)

    def test_AZP_tabu(self):
        p = 5
        tabu_length = 10
        clusters = pygeoda.azp_tabu(p, self.queen_w, self.data, tabu_length)

        self.assertAlmostEqual(clusters["Ratio"], 0.4222174)


    def test_SCHC(self):
        p = 5
        linkage_method = 'ward'
        clusters = pygeoda.schc(p, self.queen_w, self.data, linkage_method)

        self.assertAlmostEqual(clusters["Ratio"], 0.2147711255)