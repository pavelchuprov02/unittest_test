import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 5), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3], None, None), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], None, 2), [1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, None), [1, 2, 3])
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2, None), [2, 3])
