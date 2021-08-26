from unittest import  TestCase
from demo import  Calc
class TestCalc2(TestCase):
    def testAdd1(self):
        a = 6
        b = 7
        c = 42
        calc = Calc()
        sum = calc.multi(a,b)
        self.assertEqual(c,sum)

    def testAdd2(self):
        a = -6
        b = 7
        c = -42
        calc = Calc()
        sum = calc.multi(a,b)
        self.assertEqual(c,sum)

    def testAdd3(self):
        a = 6
        b = -7
        c = -42
        calc = Calc()
        sum = calc.multi(a,b)
        self.assertEqual(c,sum)

    def testAdd4(self):
        a = -6
        b = -7
        c = 42
        calc = Calc()
        sum = calc.multi(a,b)
        self.assertEqual(c,sum)

    def testAdd5(self):
        a = 6999999999999
        b = -7
        c = -48999999999993
        calc = Calc()
        sum = calc.multi(a,b)
        self.assertEqual(c,sum)

