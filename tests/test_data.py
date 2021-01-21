import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, Hang Zhang <zhanghanggis@163.com>, "

class TestTransform(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        select_vars = ["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]
        self.data = [self.guerry.GetRealCol(v) for v in select_vars]
        self.Crm_prs = self.guerry.GetRealCol('Crm_prs')
        self.Crm_prp = self.guerry.GetRealCol('Crm_prp')

    def test_DEMEAN(self):
        results = pygeoda.demean(self.data)
        self.assertAlmostEqual(results[0][0], 8909.058823529413)
        self.assertAlmostEqual(results[1][0], 8008.658823529412)
        self.assertAlmostEqual(results[2][0], -2.141176470588235)
        self.assertAlmostEqual(results[3][0], -1625.3176470588232)
        self.assertAlmostEqual(results[4][0], 14137.070588235296)
        self.assertAlmostEqual(results[5][0], -1477.800000000003)

    def test_STANDARDIZE(self):
        results = pygeoda.standardize(self.data)
        self.assertAlmostEqual(results[0][0], 1.220545786363259)
        self.assertAlmostEqual(results[1][0], 2.626982441141971)
        self.assertAlmostEqual(results[2][0], -0.12281377647044796)
        self.assertAlmostEqual(results[3][0], -0.3342044000744191)
        self.assertAlmostEqual(results[4][0], 1.5973093769164821)
        self.assertAlmostEqual(results[5][0], -0.04691678974541437)

    def test_MAD(self):
        results = pygeoda.mad(self.data)
        self.assertAlmostEqual(results[0][0], 1.4834982357401478)
        self.assertAlmostEqual(results[1][0], 3.657995001677823)
        self.assertAlmostEqual(results[2][0], -0.14598471265452484)
        self.assertAlmostEqual(results[3][0], -0.43856444476347173)
        self.assertAlmostEqual(results[4][0], 2.288114647653677)
        self.assertAlmostEqual(results[5][0], -0.06627296020171916)