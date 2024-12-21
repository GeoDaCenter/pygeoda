import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "


class TestSpatialClustering(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.queen_weights(self.guerry)
        self.data = self.guerry[["Crm_prs", "Crm_prp",
                                 "Litercy", "Donatns", "Infants", "Suicids"]]
        self.bound_variable = self.guerry.GetRealCol("Pop1831")
        self.min_bound = 3236.67  # 10% of Pop1831

    def test_makeSpatial(self):
        kmeans_c = [5, 2, 5, 1, 3, 6, 2, 5, 3, 1, 5, 3, 4, 5, 4, 4, 4, 4, 2, 6, 5, 1, 3, 1, 3, 3, 4, 1, 1, 1, 2, 1, 6, 4, 1, 1, 2, 4, 1, 5, 5,
                    1, 3, 1, 1, 1, 2, 2, 3, 2, 2, 2, 2, 4, 3, 4, 2, 2, 2, 3, 5, 1, 5, 1, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 4, 2, 1, 1, 1, 1, 6, 6, 4, 2, 3]
        result = pygeoda.make_spatial(kmeans_c, self.queen_w)

        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 2)
        self.assertEqual(result[2], 5)
        self.assertEqual(result[3], 1)

    def test_SpatialValidation(self):
        k = 6
        c = pygeoda.skater(k, self.queen_w, self.data)
        result = pygeoda.spatial_validation(
            self.guerry, c['Clusters'], self.queen_w)

        self.assertTrue(result.spatially_constrained)
        self.assertIsNone(result.cluster_fragmentation)
        self.assertAlmostEqual(
            result.fragmentation.entropy, 1.5302035777210896)
        self.assertAlmostEqual(
            result.fragmentation.std_entropy, 0.85402287751287753)
        self.assertAlmostEqual(
            result.fragmentation.simpson, 0.25619377162629758)
        self.assertAlmostEqual(
            result.fragmentation.std_simpson, 1.5371626297577856)

        self.assertAlmostEqual(result.diameter[0].steps, 7)
        self.assertAlmostEqual(result.diameter[0].ratio, 0.2413793103448276)
        self.assertAlmostEqual(result.diameter[1].steps, 7)
        self.assertAlmostEqual(result.diameter[1].ratio, 0.25)
        self.assertAlmostEqual(result.diameter[2].steps, 4)
        self.assertAlmostEqual(result.diameter[2].ratio, 0.36363636363636365)
        self.assertAlmostEqual(result.diameter[3].steps, 3)
        self.assertAlmostEqual(result.diameter[3].ratio, 0.375)
        self.assertAlmostEqual(result.diameter[4].steps, 3)
        self.assertAlmostEqual(result.diameter[4].ratio, 0.6)
        self.assertAlmostEqual(result.diameter[5].steps, 2)
        self.assertAlmostEqual(result.diameter[5].ratio, 0.5)

        self.assertAlmostEqual(
            result.compactness[0].isoperimeter_quotient, 0.0097723523876562887)
        self.assertAlmostEqual(result.compactness[0].area, 177914101737.5)
        self.assertAlmostEqual(
            result.compactness[0].perimeter, 15125528.512594011)
        self.assertAlmostEqual(
            result.compactness[1].isoperimeter_quotient, 0.0099144268567466272)
        self.assertAlmostEqual(result.compactness[1].area, 164582498646)
        self.assertAlmostEqual(
            result.compactness[1].perimeter, 14443184.236951336)
        self.assertAlmostEqual(
            result.compactness[2].isoperimeter_quotient, 0.029675044913002577)
        self.assertAlmostEqual(result.compactness[2].area, 72184135751)
        self.assertAlmostEqual(
            result.compactness[2].perimeter, 5528790.326552554)
        self.assertAlmostEqual(
            result.compactness[3].isoperimeter_quotient, 0.034800225315536358)
        self.assertAlmostEqual(result.compactness[3].area, 50339473596)
        self.assertAlmostEqual(
            result.compactness[3].perimeter, 4263519.3561323136)
        self.assertAlmostEqual(
            result.compactness[4].isoperimeter_quotient, 0.046733291357011458)
        self.assertAlmostEqual(result.compactness[4].area, 32318674158)
        self.assertAlmostEqual(
            result.compactness[4].perimeter, 2947939.1554776165)
        self.assertAlmostEqual(
            result.compactness[5].isoperimeter_quotient, 0.035828472477053515)
        self.assertAlmostEqual(result.compactness[5].area, 27445319943.5)
        self.assertAlmostEqual(
            result.compactness[5].perimeter, 3102593.9023676016)

        self.assertAlmostEqual(
            result.joincount_ratio[0].ratio, 0.8571428571428571)
        self.assertAlmostEqual(
            result.joincount_ratio[1].ratio, 0.89230769230769236)
        self.assertAlmostEqual(
            result.joincount_ratio[2].ratio, 0.58461538461538465)
        self.assertAlmostEqual(
            result.joincount_ratio[3].ratio, 0.54545454545454541)
        self.assertAlmostEqual(
            result.joincount_ratio[4].ratio, 0.38461538461538464)
        self.assertAlmostEqual(
            result.joincount_ratio[5].ratio, 0.66666666666666663)

    def test_SKATER(self):
        k = 5
        clusters = pygeoda.skater(k, self.queen_w, self.data)

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.3763086809)

    def test_REDCAP_firstsingle(self):
        k = 5
        clusters = pygeoda.redcap(
            k, self.queen_w, self.data, "firstorder-singlelinkage")

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.3763086808858706)

    def test_REDCAP_fullsingle(self):
        k = 5
        clusters = pygeoda.redcap(
            k, self.queen_w, self.data, "fullorder-singlelinkage")

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.33931921310113483)

    def test_REDCAP_fullcomplete(self):
        k = 5
        clusters = pygeoda.redcap(
            k, self.queen_w, self.data, "fullorder-completelinkage")

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.39420885009615186)

    def test_REDCAP_fullaverage(self):
        k = 5
        clusters = pygeoda.redcap(
            k, self.queen_w, self.data, "fullorder-averagelinkage")

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.3854425827224785)

    def test_REDCAP_fullward(self):
        k = 5
        clusters = pygeoda.redcap(
            k, self.queen_w, self.data, "fullorder-wardlinkage")

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.42268567324507456)

    def test_MAXP_greedy(self):
        clusters = pygeoda.maxp_greedy(
            self.queen_w, self.data, self.bound_variable, self.min_bound)

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.44574207)

    def test_MAXP_sa(self):
        cooling_rate = 0.85
        clusters = pygeoda.maxp_sa(
            self.queen_w, self.data, self.bound_variable, self.min_bound, cooling_rate)

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.4899529029)

    def test_MAXP_tabu(self):
        tabu_length = 10
        clusters = pygeoda.maxp_tabu(
            self.queen_w, self.data, self.bound_variable, self.min_bound, tabu_length)

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.478018129)

    def test_AZP_greedy(self):
        p = 5
        clusters = pygeoda.azp_greedy(p, self.queen_w, self.data)

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.3598540983177219)

    def test_AZP_sa(self):
        p = 5
        cooling_rate = 0.85
        clusters = pygeoda.azp_sa(p, self.queen_w, self.data, cooling_rate)

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.424288839)

    def test_AZP_tabu(self):
        p = 5
        tabu_length = 10
        clusters = pygeoda.azp_tabu(p, self.queen_w, self.data, tabu_length)

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.4222174)

    def test_SCHC(self):
        p = 5
        linkage_method = 'ward'
        clusters = pygeoda.schc(p, self.queen_w, self.data, linkage_method)

        self.assertAlmostEqual(
            clusters["The ratio of between to total sum of squares"], 0.2147711255)
