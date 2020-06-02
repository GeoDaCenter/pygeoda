import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, Hang Zhang <zhanghanggis@163.com>, "

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("./data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        select_vars = ["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]
        self.data = [self.guerry.GetRealCol(v) for v in select_vars]
        self.Crm_prs = self.guerry.GetRealCol('Crm_prs')
        self.Crm_prp = self.guerry.GetRealCol('Crm_prp')

    def test_dada_mds(self):
        Rt_Nc = pygeoda.mds(self.data,6)
        self.assertAlmostEqual(Rt_Nc[0][0],-111.87257059039554)
        self.assertAlmostEqual(Rt_Nc[1][0],15015.23673870141)
        self.assertAlmostEqual(Rt_Nc[2][0],-7873.386080811686)
        self.assertAlmostEqual(Rt_Nc[3][0],5595.705423843862)
        self.assertAlmostEqual(Rt_Nc[4][0],-5424.030975546458)
        self.assertAlmostEqual(Rt_Nc[5][0],13.250852266896509)