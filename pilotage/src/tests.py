from unittest import TestCase
from script import *


class Test(TestCase):
    def test_add1(self):
        self.assertEqual(add(2, 3), 5)
    def test_add2(self):
        self.assertEqual(add(3, 3), 6)
    def test_add3(self):
        self.assertEqual(add(1, 3), 4)
    def test_add4(self):
        self.assertEqual(add(2, 2), 4)

    def test_soustract1(self):
        self.assertEqual(soustraction(2, 3), -1)
    def test_soustract2(self):
        self.assertEqual(soustraction(2, 2), 0)
    def test_soustract3(self):
        self.assertEqual(soustraction(3,2), 1)
    def test_soustract4(self):
        self.assertEqual(soustraction(3, 3), 0)

    def test_multiplication1(self):
        self.assertEqual(multiplication(2, 3), 6)
    def test_multiplication2(self):
        self.assertEqual(multiplication(2, 2), 4)
    def test_multiplication3(self):
        self.assertEqual(multiplication(3,2), 6)
    def test_multiplication4(self):
        self.assertEqual(multiplication(3, 3), 9)

    def test_division1(self):
        self.assertEqual(division(2, 3), 0.6666666666666666)
    def test_division2(self):
        self.assertEqual(division(2, 2), 1)
    def test_division3(self):
        self.assertEqual(division(3,2), 1.5)
    def test_division4(self):
        self.assertEqual(division(3, 3), 1)

