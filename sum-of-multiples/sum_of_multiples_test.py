import unittest

from sum_of_multiples import SumOfMultiples


class SumOfMultiplesTest(unittest.TestCase):
    def test_sum_to_1(self):
        self.assertEqual(0, SumOfMultiples().to(1))

    def test_sum_to_4(self):
        self.assertEqual(3, SumOfMultiples().to(4))

    def test_sum_to_10(self):
        self.assertEqual(23, SumOfMultiples().to(10))

    def test_sum_to_1000(self):
        self.assertEqual(233168, SumOfMultiples().to(1000))

    def test_configurable_7_13_17_to_20(self):
        self.assertEqual(51, SumOfMultiples(7, 13, 17).to(20))

    def test_configurable_43_47_to_10000(self):
        self.assertEqual(2203160, SumOfMultiples(43, 47).to(10000))

    def test_configurable_20_24_25_to_800(self):
        self.assertEqual(36144, SumOfMultiples(20, 24, 25).to(800))

    def test_configurable_0_to_10(self):
        self.assertEqual(0, SumOfMultiples(0).to(10))

    def test_configurable_0_1_to_10(self):
        self.assertEqual(45, SumOfMultiples(0, 1).to(10))


if __name__ == '__main__':
    unittest.main()
