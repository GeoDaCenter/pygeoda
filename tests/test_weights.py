import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestWeights(unittest.TestCase):
    def setUp(self):
        self.nat = pygeoda.open("./data/natregimes.shp")

    def test_queen_weights(self):
        w = pygeoda.weights.queen(self.nat)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.GetMinNbrs(), 1)
        self.assertEqual(w.GetMeanNbrs(), 5.8891410048622364)
        self.assertEqual(w.GetMaxNbrs(), 14)
        self.assertTrue(w.IsSymmetric())
        self.assertEqual(w.GetSparsity(), 0)
        self.assertEqual(w.GetDensity(), 0.19089598070866245)

    def test_rook_weights(self):
        w = pygeoda.weights.rook(self.nat)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.GetMinNbrs(), 1)
        self.assertEqual(w.GetMeanNbrs(), 5.571474878444084)
        self.assertEqual(w.GetMaxNbrs(), 13)
        self.assertTrue(w.IsSymmetric())
        self.assertEqual(w.GetSparsity(), 0)
        self.assertEqual(w.GetDensity(), 0.18059886153789576)

    def test_knn_weights(self):
        k = 4
        w = pygeoda.weights.knn(self.nat, k)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.GetMinNbrs(), 4)
        self.assertEqual(w.GetMeanNbrs(), 4)
        self.assertEqual(w.GetMaxNbrs(), 4)
        self.assertFalse(w.IsSymmetric())
        self.assertEqual(w.GetSparsity(), 0)
        self.assertEqual(w.GetDensity(), 0.12965964343598055)

    def test_distance_threshold_weights(self):
        dist_thres = pygeoda.weights.min_threshold(self.nat)
        w = pygeoda.weights.distance(self.nat, dist_thres)

        self.assertEqual(dist_thres, 1.4657759325950015)
        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.GetMinNbrs(), 1)
        self.assertEqual(w.GetMeanNbrs(), 36.833711507293351)
        self.assertEqual(w.GetMaxNbrs(), 85)
        self.assertFalse(w.IsSymmetric())
        self.assertEqual(w.GetSparsity(), 0)
        self.assertEqual(w.GetDensity(), 1.1939614751148575)

    def test_kernel_knn_weights(self):
        k = 15
        kernel = "triangular"
        w = pygeoda.weights.kernel(self.nat, k, kernel)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.GetMinNbrs(), 15)
        self.assertEqual(w.GetMeanNbrs(), 15)
        self.assertEqual(w.GetMaxNbrs(), 15)
        self.assertFalse(w.IsSymmetric())
        self.assertEqual(w.GetSparsity(), 0)
        self.assertEqual(w.GetDensity(), 0.48622366288492708)

    def test_kernel_distband_weights(self):
        bandwidth = pygeoda.weights.min_threshold(self.nat)
        kernel = "triangular"
        w = pygeoda.weights.kernel_bandwidth(self.nat, bandwidth, kernel)

        self.assertEqual(bandwidth, 1.4657759325950015)
        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.GetMinNbrs(), 1)
        self.assertEqual(w.GetMeanNbrs(), 36.83371150729335)
        self.assertEqual(w.GetMaxNbrs(), 85)
        self.assertFalse(w.IsSymmetric())
        self.assertEqual(w.GetSparsity(), 0)
        self.assertEqual(w.GetDensity(), 1.1939614751148575)
    
    def test_SaveToFile(self):
        w = pygeoda.weights.queen(self.nat)
        w.SaveToFile('D:/ttt/','natregimes.shp','POLY_ID',self.nat.GetIntegerCol("POLY_ID"))
        