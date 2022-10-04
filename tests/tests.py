from email.mime import image
from calc import Calculator
import unittest

calc = Calculator()

class TestCalc(unittest.TestCase) :

    def test_add_1(self):
        assert calc.add(2, 3) == 5

    def test_add_2(self):
        assert calc.add(-1, 1) == 0

    def test_sub_1(self):
        assert calc.sub(5, 2) == 3

    def test_sub_2(self):
        assert calc.sub(8, 8) == 0

    def test_mul_1(self):
        assert calc.mul(2, 3) == 6

    def test_mul_2(self):
        assert calc.mul(0, 1000) == 0

    def test_div_1(self):
        assert calc.div(6, 3) == 2

    def test_div_2(self):
        assert calc.div(9, 1) == 1