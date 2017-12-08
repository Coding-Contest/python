import unittest

from spiral_matrix import spiral

# Tests are based on the version 1.0.0 of:
# https://github.com/exercism/problem-specifications/blob/master/exercises/spiral-matrix/canonical-data.json


class SpiralMatrixTest(unittest.TestCase):
    def test_spiral_matrix_of_0(self):
        self.assertEqual(spiral(0), [])

    def test_spiral_matrix_of_1(self):
        self.assertEqual(spiral(1), [[1]])

    def test_spiral_matrix_of_2(self):
        self.assertEqual(spiral(2), [[1, 2],
                                     [4, 3]])

    def test_spiral_matrix_of_3(self):
        self.assertEqual(spiral(3), [[1, 2, 3],
                                     [8, 9, 4],
                                     [7, 6, 5]])

    def test_spiral_matrix_of_4(self):
        self.assertEqual(spiral(4), [[1,  2,  3,  4],
                                     [12, 13, 14, 5],
                                     [11, 16, 15, 6],
                                     [10, 9,  8,  7]])

    def test_spiral_matrix_of_5(self):
        self.assertEqual(spiral(5), [[1,  2,  3,  4,  5],
                                     [16, 17, 18, 19, 6],
                                     [15, 24, 25, 20, 7],
                                     [14, 23, 22, 21, 8],
                                     [13, 12, 11, 10, 9]])


if __name__ == '__main__':
    unittest.main()
