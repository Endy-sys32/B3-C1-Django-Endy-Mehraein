from unittest import TestCase
from script import *


class Test(TestCase):
    def test_add1(self):
        self.assertEqual(add(2, 3), 6)
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