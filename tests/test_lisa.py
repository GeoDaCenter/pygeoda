import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, Hang Zhang <zhanghanggis@163.com>, "

class TestLISA(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        self.crm_prp = self.guerry.GetIntegerCol("Crm_prp")
        slect_vars = ['Crm_prp','Crm_prs']
        self.data = [self.guerry.GetRealCol(v) for v in slect_vars]

    def test_quantile_lisa(self):
        lisa = pygeoda.quantile_lisa(self.queen_w, 7, 6, self.crm_prp)
        
        pvals = lisa.GetPValues()
        self.assertAlmostEqual(pvals[0], 0.434000)
        self.assertAlmostEqual(pvals[1], 0.031000)
        self.assertAlmostEqual(pvals[3], 0.428000)

        nnvals = lisa.GetNumNeighbors()
        self.assertEqual(nnvals[0], 4)
        self.assertEqual(nnvals[1], 6)
        self.assertEqual(nnvals[2], 6)
        
    def test_local_moran(self):
        lisa = pygeoda.local_moran(self.queen_w, self.crm_prp)

        lms = lisa.GetLISAValues()
        self.assertEqual(lms[0], 0.015431978309803657)
        self.assertEqual(lms[1], 0.3270633223656033)
        self.assertEqual(lms[2], 0.021295296214118884)

        pvals = lisa.GetPValues()
        self.assertEqual(pvals[0], 0.41399999999999998)
        self.assertEqual(pvals[1], 0.123)
        self.assertEqual(pvals[2], 0.001)

        cvals = lisa.GetClusterIndicators()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 0)
        self.assertEqual(cvals[2], 1)

    def test_local_geary(self):
        lisa = pygeoda.local_geary(self.queen_w, self.crm_prp)

        lvals = lisa.GetLISAValues()
        self.assertEqual(lvals[0], 7.3980833011783602)
        self.assertEqual(lvals[1], 0.28361195650519017)
        self.assertEqual(lvals[2], 3.6988922226329906)

        pvals = lisa.GetPValues()
        self.assertEqual(pvals[0], 0.39800000000000002)
        self.assertEqual(pvals[1], 0.027)
        self.assertEqual(pvals[2], 0.025)

        cvals = lisa.GetClusterIndicators()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 2)
        self.assertEqual(cvals[2], 4)

    def test_local_joincount(self):
        columbus = pygeoda.open("./data/columbus.shp")
        columbus_q = pygeoda.weights.queen(columbus)
        nsa = columbus.GetRealCol("nsa")

        lisa = pygeoda.local_joincount(columbus_q, nsa)

        lvals = lisa.GetLISAValues()
        self.assertEqual(lvals[0], 2)
        self.assertEqual(lvals[1], 3)
        self.assertEqual(lvals[2], 4)

        pvals = lisa.GetPValues()
        self.assertEqual(pvals[0], 0.21299999999999999)
        self.assertEqual(pvals[1], 0.070000000000000007)
        self.assertEqual(pvals[2], 0.017000000000000001)

        nnvals = lisa.GetNumNeighbors()
        self.assertEqual(nnvals[0], 2)
        self.assertEqual(nnvals[1], 3)
        self.assertEqual(nnvals[2], 4)

    def test_local_multijoincount(self):
        columbus = pygeoda.open("./data/columbus.shp")
        columbus_q = pygeoda.weights.queen(columbus)
        nsa = columbus.GetRealCol("nsa")
        nsb = columbus.GetRealCol("nsb")
        nndata = (nsa, nsb)

        lisa = pygeoda.local_multijoincount(columbus_q, nndata)

        lvals = lisa.GetLISAValues()
        self.assertEqual(lvals[0], 2)
        self.assertEqual(lvals[1], 3)
        self.assertEqual(lvals[2], 4)

        pvals = lisa.GetPValues()
        self.assertEqual(pvals[0], 0.213000)
        self.assertEqual(pvals[1], 0.070000)
        self.assertEqual(pvals[2], 0.017000)

        nnvals = lisa.GetNumNeighbors()
        self.assertEqual(nnvals[0], 2)
        self.assertEqual(nnvals[1], 3)
        self.assertEqual(nnvals[2], 4)

    def test_local_g(self):
        lisa = pygeoda.local_g(self.queen_w, self.crm_prp)

        lvals = lisa.GetLISAValues()
        self.assertEqual(lvals[0], 0.012077920687925825)
        self.assertEqual(lvals[1], 0.0099240961298508561)
        self.assertEqual(lvals[2], 0.018753584525825453)

        pvals = lisa.GetPValues()
        self.assertEqual(pvals[0], 0.414)
        self.assertEqual(pvals[1], 0.123)
        self.assertEqual(pvals[2], 0.001)

        cvals = lisa.GetClusterIndicators()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 0)
        self.assertEqual(cvals[2], 1)

    def test_local_gstar(self):
        lisa = pygeoda.local_gstar(self.queen_w, self.crm_prp)

        lvals = lisa.GetLISAValues()
        self.assertEqual(lvals[0], 0.014177043620524426)
        self.assertEqual(lvals[1], 0.0096136007223101994)
        self.assertEqual(lvals[2], 0.017574324039034434)

        pvals = lisa.GetPValues()
        self.assertEqual(pvals[0], 0.414)
        self.assertEqual(pvals[1], 0.123)
        self.assertEqual(pvals[2], 0.001)

        cvals = lisa.GetClusterIndicators()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 0)
        self.assertEqual(cvals[2], 1)

    def test_GetFDR(self):
        columbus = pygeoda.open("./data/columbus.shp")
        columbus_q = pygeoda.weights.queen(columbus)
        nsa = columbus.GetRealCol("nsa")

        lisa = pygeoda.local_moran(columbus_q, nsa)

        p = lisa.GetFDR(0.05)
        self.assertAlmostEqual(p, 0.0132653)