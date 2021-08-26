from unittest import  TestCase
from demo import  Calc
class TestCalc2(TestCase):
    def testAdd1(self):
        a = 60
        b = 5
        c = 12
        calc = Calc()
        sum = calc.devision(a,b)
        self.assertEqual(c,sum)

    def testAdd2(self):
        a = 10
        b = 20
        c = 0.5
        calc = Calc()
        sum = calc.devision(a,b)
        self.assertEqual(c,sum)

    def testAdd3(self):
        a = -60
        b = 5
        c = -12
        calc = Calc()
        sum = calc.devision(a,b)
        self.assertEqual(c,sum)

    def testAdd4(self):
        a = 60
        b = -5
        c = -12
        calc = Calc()
        sum = calc.devision(a,b)
        self.assertEqual(c,sum)

    def testAdd5(self):
        a = -60
        b = -5
        c = 12
        calc = Calc()
        sum = calc.devision(a,b)
        self.assertEqual(c,sum)