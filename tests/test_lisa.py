import unittest
import math
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, Hang Zhang <zhanghanggis@163.com>, "

class TestLISA(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.queen_weights(self.guerry)
        self.crm_prp = self.guerry.GetIntegerCol("Crm_prp")
        self.crm_prs = self.guerry.GetIntegerCol("Crm_prs")
        self.litercy = self.guerry.GetIntegerCol("Litercy")
        slect_vars = ['Crm_prp','Crm_prs']
        self.data = [self.guerry.GetRealCol(v) for v in slect_vars]

    def test_batch_moran(self):
        blm = pygeoda.batch_local_moran(self.queen_w, self.data)

        # get results for first variable: Crm_prp
        lms = blm.lisa_values(0) 
        self.assertAlmostEqual(lms[0], 0.015431978309803657)
        self.assertAlmostEqual(lms[1], 0.3270633223656033)
        self.assertAlmostEqual(lms[2], 0.021295296214118884) 

        pvals = blm.lisa_pvalues(0)
        self.assertAlmostEqual(pvals[0], 0.41399999999999998)
        self.assertAlmostEqual(pvals[1], 0.123)
        self.assertAlmostEqual(pvals[2], 0.001)

        # get results from second variable: Crm_prs
        lms = blm.lisa_values(1) 
        self.assertAlmostEqual(lms[0], 0.516120231288079)
        self.assertAlmostEqual(lms[1], 0.818275138495031)
        self.assertAlmostEqual(lms[2], 0.794086559694542) 

        pvals = blm.lisa_pvalues(1)
        self.assertAlmostEqual(pvals[0], 0.197000000000000)
        self.assertAlmostEqual(pvals[1], 0.013000000000000)
        self.assertAlmostEqual(pvals[2], 0.023000000000000)

    def test_quantile_lisa(self):
        lisa = pygeoda.local_quantilelisa(self.queen_w, self.guerry["Crm_prp"], 7, 7)
        
        pvals = lisa.lisa_pvalues()
        self.assertAlmostEqual(pvals[0], 0.434000)

        nnvals = lisa.lisa_num_nbrs()
        self.assertEqual(nnvals[0], 4)
        self.assertEqual(nnvals[1], 6)
        self.assertEqual(nnvals[2], 6)
        
    def test_multiquantile_lisa(self):
        k = (4, 4)
        q = (1, 1)

        data = self.guerry[['Crm_prs','Crm_prp']]

        lisa = pygeoda.local_multiquantilelisa(self.queen_w, data, k, q)
        
        pvals = lisa.lisa_pvalues()
        self.assertAlmostEqual(pvals[11], 0.244)

    def test_local_moran(self):
        lisa = pygeoda.local_moran(self.queen_w, self.crm_prp, permutation_method="complete")

        lms = lisa.lisa_values()
        self.assertEqual(lms[0], 0.015431978309803657)
        self.assertEqual(lms[1], 0.3270633223656033)
        self.assertEqual(lms[2], 0.021295296214118884)

        pvals = lisa.lisa_pvalues()
        self.assertEqual(pvals[0], 0.41399999999999998)
        self.assertEqual(pvals[1], 0.123)
        self.assertEqual(pvals[2], 0.001)

        cvals = lisa.lisa_clusters()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 0)
        self.assertEqual(cvals[2], 1)

    def test_local_bimoran(self):
        lisa = pygeoda.local_bimoran(self.queen_w, self.crm_prs, self.litercy, permutation_method="complete")

        lms = lisa.lisa_values()
        self.assertEqual(lms[0], 0.39266344763810573)
        self.assertEqual(lms[1], 0.75613610603433934)
        self.assertEqual(lms[2], -0.87851057571266755)

        pvals = lisa.lisa_pvalues()
        self.assertEqual(pvals[0], 0.269)
        self.assertEqual(pvals[1], 0.021)
        self.assertEqual(pvals[2], 0.001)

    def test_local_geary(self):
        lisa = pygeoda.local_geary(self.queen_w, self.crm_prp)

        lvals = lisa.lisa_values()
        self.assertEqual(lvals[0], 7.3980833011783602)
        self.assertEqual(lvals[1], 0.28361195650519017)
        self.assertEqual(lvals[2], 3.6988922226329906)

        pvals = lisa.lisa_pvalues()
        self.assertEqual(pvals[0], 0.39800000000000002)
        self.assertEqual(pvals[1], 0.027)
        self.assertEqual(pvals[2], 0.025)

        cvals = lisa.lisa_clusters()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 2)
        self.assertEqual(cvals[2], 4)

    def test_local_multigeary(self):
        self.crm_prs = self.guerry.GetIntegerCol("Crm_prs")
        data = [self.crm_prp, self.crm_prs]
        lisa = pygeoda.local_multigeary(self.queen_w, data)

        lvals = lisa.lisa_values()
        self.assertAlmostEqual(lvals[0], 4.192904310228536)
        self.assertAlmostEqual(lvals[1], 0.560978550546873)
        self.assertAlmostEqual(lvals[2], 2.200847073745350)

        pvals = lisa.lisa_pvalues()
        self.assertAlmostEqual(pvals[0], 0.226000000000000)
        self.assertAlmostEqual(pvals[1], 0.015000000000000)
        self.assertAlmostEqual(pvals[2], 0.111000000000000)

        cvals = lisa.lisa_clusters()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 1)
        self.assertEqual(cvals[2], 0)

    def test_local_joincount(self):
        columbus = pygeoda.open("./data/columbus.shp")
        columbus_q = pygeoda.queen_weights(columbus)
        nsa = columbus.GetRealCol("nsa")

        lisa = pygeoda.local_joincount(columbus_q, nsa)

        lvals = lisa.lisa_values()
        self.assertEqual(lvals[0], 2)
        self.assertEqual(lvals[1], 3)
        self.assertEqual(lvals[2], 4)

        pvals = lisa.lisa_pvalues()
        self.assertEqual(pvals[0], 0.21299999999999999)
        self.assertEqual(pvals[1], 0.070000000000000007)
        self.assertEqual(pvals[2], 0.017000000000000001)

        nnvals = lisa.lisa_num_nbrs()
        self.assertEqual(nnvals[0], 2)
        self.assertEqual(nnvals[1], 3)
        self.assertEqual(nnvals[2], 4)

    def test_local_bijoincount(self):
        columbus = pygeoda.open("./data/columbus.shp")
        columbus_q = pygeoda.queen_weights(columbus)
        nsa = columbus.GetRealCol("nsa")
        nsa_inv = [1-i for i in nsa]
        lisa = pygeoda.local_bijoincount(columbus_q, [nsa, nsa_inv])

        jc = lisa.lisa_values()
        self.assertEqual(jc[7], 0)
        self.assertEqual(jc[8], 1)
        self.assertEqual(jc[9], 1)

        pvals = lisa.lisa_pvalues()
        self.assertEqual(pvals[8], 0.002)
        self.assertEqual(pvals[9], 0.034)

        nn = lisa.lisa_num_nbrs()
        self.assertEqual(nn[0], 2)
        self.assertEqual(nn[1], 3)
        self.assertEqual(nn[2], 4)

    def test_local_multijoincount(self):
        columbus = pygeoda.open("./data/columbus.shp")
        columbus_q = pygeoda.queen_weights(columbus)
        nsa = columbus.GetRealCol("nsa")
        nsb = columbus.GetRealCol("nsb")
        nndata = (nsa, nsb)

        #The following two lines will raise warning to use local_bijoincount()
        #nsa_inv = [1-i for i in nsa]
        #lisa = pygeoda.local_multijoincount(columbus_q, (nsa, nsa_inv))

        lisa = pygeoda.local_multijoincount(columbus_q, nndata)

        lvals = lisa.lisa_values()
        self.assertEqual(lvals[0], 2)
        self.assertEqual(lvals[1], 3)
        self.assertEqual(lvals[2], 4)

        pvals = lisa.lisa_pvalues()
        self.assertEqual(pvals[0], 0.213000)
        self.assertEqual(pvals[1], 0.070000)
        self.assertEqual(pvals[2], 0.017000)

        nnvals = lisa.lisa_num_nbrs()
        self.assertEqual(nnvals[0], 2)
        self.assertEqual(nnvals[1], 3)
        self.assertEqual(nnvals[2], 4)

    def test_local_g(self):
        lisa = pygeoda.local_g(self.queen_w, self.crm_prp)

        lvals = lisa.lisa_values()
        self.assertEqual(lvals[0], 0.012077920687925825)
        self.assertEqual(lvals[1], 0.0099240961298508561)
        self.assertEqual(lvals[2], 0.018753584525825453)

        pvals = lisa.lisa_pvalues()
        self.assertEqual(pvals[0], 0.414)
        self.assertEqual(pvals[1], 0.123)
        self.assertEqual(pvals[2], 0.001)

        cvals = lisa.lisa_clusters()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 0)
        self.assertEqual(cvals[2], 1)

    def test_local_gstar(self):
        lisa = pygeoda.local_gstar(self.queen_w, self.crm_prp)

        lvals = lisa.lisa_values()
        self.assertEqual(lvals[0], 0.014177043620524426)
        self.assertEqual(lvals[1], 0.0096136007223101994)
        self.assertEqual(lvals[2], 0.017574324039034434)

        pvals = lisa.lisa_pvalues()
        self.assertEqual(pvals[2], 0.001)

        cvals = lisa.lisa_clusters()
        self.assertEqual(cvals[0], 0)
        self.assertEqual(cvals[1], 0)
        self.assertEqual(cvals[2], 1)

    def test_GetFDR(self):
        lm = pygeoda.local_moran(self.queen_w, self.crm_prp)

        p = lm.lisa_fdr(0.05)
        self.assertAlmostEqual(p, 0.000588235)

    def test_NeighborMatchTest(self):
        data = self.guerry[['Crm_prs','Crm_prp','Litercy','Donatns','Infants','Suicids']]
        rst = pygeoda.neighbor_match_test(self.guerry, data, 6)

        self.assertAlmostEqual(rst["Probability"][0], 0.052638)
        self.assertAlmostEqual(rst["Cardinality"][0], 2)