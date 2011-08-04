#-*- coding:utf-8 -*-
import unittest
from should_dsl import should, should_not

from neuronio import Neuronio

class TestNeuronio(unittest.TestCase):

    def setUp(self):
        w = {'w0': 0, 'w1':0, 'w2': 0}
        self.neuronio = Neuronio(**w)

    def test_neuronio(self):
        self.neuronio.w0 |should| equal_to(0)
        self.neuronio.w1 |should| equal_to(0)
        self.neuronio.w2 |should| equal_to(0)

if __name__ == '__main__':
    unittest.main()
