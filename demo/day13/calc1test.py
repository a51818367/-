from unittest import  TestCase
from demo import  Calc
class TestCalc1(TestCase):
    def testAdd1(self):
        a = 6
        b = 7
        c = -1
        calc = Calc()
        sum = calc.subs(a,b)
        self.assertEqual(c,sum)

    def testAdd2(self):
        a = 7
        b = 6
        c = 1
        calc = Calc()
        sum = calc.subs(a,b)
        self.assertEqual(c,sum)

    def testAdd3(self):
        a = -7
        b = 6
        c = -13
        calc = Calc()
        sum = calc.subs(a,b)
        self.assertEqual(c,sum)

    def testAdd4(self):
        a = -7
        b = -6
        c = -1
        calc = Calc()
        sum = calc.subs(a,b)
        self.assertEqual(c,sum)

    def testAdd5(self):
        a = 7
        b = -6
        c = 13
        calc = Calc()
        sum = calc.subs(a,b)
        self.assertEqual(c,sum)






















