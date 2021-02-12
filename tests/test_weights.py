import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestWeights(unittest.TestCase):
    def setUp(self):
        self.nat = pygeoda.open("./data/natregimes.shp")
        self.poly_id = self.nat.GetIntegerCol("POLY_ID")
        
    def test_queen_weights(self):
        w = pygeoda.weights.queen(self.nat)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 1)
        self.assertEqual(w.mean_neighbors(), 5.8891410048622364)
        self.assertEqual(w.max_neighbors(), 14)
        self.assertTrue(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 0.19089598070866245)

    def test_queen2_weight(self):

        w = pygeoda.weights.queen(self.nat,order = 2, include_lower_order = True, precision_threshold = 1.0)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 2)
        self.assertEqual(w.mean_neighbors(), 18.574392220421394)
        self.assertEqual(w.max_neighbors(), 40)
        self.assertTrue(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 0.6020872680849723)

    def test_rook_weights(self):
        w = pygeoda.weights.rook(self.nat)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 1)
        self.assertEqual(w.mean_neighbors(), 5.571474878444084)
        self.assertEqual(w.max_neighbors(), 13)
        self.assertTrue(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 0.18059886153789576)

    def test_rook2_weights(self):
        w = pygeoda.weights.rook(self.nat, order=2, include_lower_order = True, precision_threshold = 2.0)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 2)
        self.assertEqual(w.mean_neighbors(), 18.574392220421394)
        self.assertEqual(w.max_neighbors(), 40)
        self.assertTrue(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 0.6020872680849723)

    def test_knn_weights(self):
        k = 4
        #w = pygeoda.weights.knn(self.nat, k, **{'power': 2.0})
        w = pygeoda.weights.knn(self.nat, k, power=2.0)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 4)
        self.assertEqual(w.mean_neighbors(), 4)
        self.assertEqual(w.max_neighbors(), 4)
        self.assertFalse(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 0.12965964343598055)

    def test_knn2_weights(self):
        k = 6
        w = pygeoda.weights.knn(self.nat, k, power = 2.0, is_inverse = True, is_arc = True, is_mile = False)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 6)
        self.assertEqual(w.mean_neighbors(), 6.00)
        self.assertEqual(w.max_neighbors(), 6)
        self.assertFalse(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 0.19448946515397084)


    def test_distance_threshold_weights(self):
        dist_thres = pygeoda.weights.min_threshold(self.nat)
        w = pygeoda.weights.distance(self.nat, dist_thres)

        self.assertEqual(dist_thres, 1.4657759325950015)
        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 1)
        self.assertEqual(w.mean_neighbors(), 36.833711507293351)
        self.assertEqual(w.max_neighbors(), 85)
        self.assertFalse(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 1.1939614751148575)

    def test_distance2_threshold_weights(self):
        dist_thres = pygeoda.weights.min_threshold(self.nat)
        w = pygeoda.weights.distance(self.nat, dist_thres, power = 2.0, is_inverse = True)

        self.assertEqual(dist_thres, 1.4657759325950015)
        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 1)
        self.assertEqual(w.mean_neighbors(), 36.83371150729335)
        self.assertEqual(w.max_neighbors(), 85)
        self.assertFalse(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 1.1939614751148575)

    def test_kernel_knn_weights(self):
        k = 15
        kernel = "triangular"
        w = pygeoda.weights.kernel(self.nat, k, kernel)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 15)
        self.assertEqual(w.mean_neighbors(), 15)
        self.assertEqual(w.max_neighbors(), 15)
        self.assertFalse(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 0.48622366288492708)

    def test_kernel2_knn_weights(self):
        k = 12
        kernel = "gaussian"
        w = pygeoda.weights.kernel(self.nat, k, kernel, use_kernel_diagonals = True)

        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 12)
        self.assertEqual(w.mean_neighbors(), 12)
        self.assertEqual(w.max_neighbors(), 12)
        self.assertFalse(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 0.3889789303079417)

    def test_kernel_distband_weights(self):
        bandwidth = pygeoda.weights.min_threshold(self.nat)
        kernel = "triangular"
        w = pygeoda.weights.kernel_bandwidth(self.nat, bandwidth, kernel)

        self.assertEqual(bandwidth, 1.4657759325950015)
        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 1)
        self.assertEqual(w.mean_neighbors(), 36.83371150729335)
        self.assertEqual(w.max_neighbors(), 85)
        self.assertFalse(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 1.1939614751148575)

    def test_kernel2_distband_weights(self):
        bandwidth = pygeoda.weights.min_threshold(self.nat)
        kernel = "quartic"
        w = pygeoda.weights.kernel_bandwidth(self.nat, bandwidth, kernel, use_kernel_diagonals = True)

        self.assertEqual(bandwidth, 1.4657759325950015)
        self.assertEqual(w.num_obs, 3085)
        self.assertEqual(w.min_neighbors(), 1)
        self.assertEqual(w.mean_neighbors(), 36.83371150729335)
        self.assertEqual(w.max_neighbors(), 85)
        self.assertFalse(w.is_symmetric())
        self.assertEqual(w.weights_sparsity(), 1.1939614751148575)


    """
    def test_SaveToFile(self):
        w = pygeoda.weights.queen(self.nat)
        w.SaveToFile('D:/ttt/','natregimes.shp','POLY_ID',self.nat.GetIntegerCol("POLY_ID"))
    """