'''
    单元测试框架：
        unittest
        1.大量的数据问题
        2.重复的操作问题
        3.将所有的测试结果总结到测试报告里。
    1.unittest提供TestCase
        HTMLTestRunner  运行器框架，生成测试报告
    2.子类继承TestCase
    3.写测试用例：testXxxx
'''
from unittest import TestCase
from Calc import Calc

class TestCalc(TestCase):

    def testAdd1(self):
        # 1.造数据
        a = -6
        b = -5
        s = -11

        # 2.执行测试
        calc = Calc()
        result = calc.add(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testAdd2(self):
        # 1.造数据
        a = 6
        b = 5
        s = 11

        # 2.执行测试
        calc = Calc()
        result = calc.add(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testAdd3(self):
        # 1.造数据
        a = -6
        b = 5
        s = -1

        # 2.执行测试
        calc = Calc()
        result = calc.add(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testAdd4(self):
        # 1.造数据
        a = 6
        b = -5
        s = 1

        # 2.执行测试
        calc = Calc()
        result = calc.add(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testAdd5(self):
        # 1.造数据
        a = 0
        b = -5
        s = -5

        # 2.执行测试
        calc = Calc()
        result = calc.add(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testAdd6(self):
        # 1.造数据
        a = 0
        b = 5
        s = 5

        # 2.执行测试
        calc = Calc()
        result = calc.add(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testAdd7(self):
        # 1.造数据
        a = 10000000000000000000000000000000000000000000000000000000000000000000
        b = 5
        s = 10000000000000000000000000000000000000000000000000000000000000000005

        # 2.执行测试
        calc = Calc()
        result = calc.add(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testminus1(self):
        # 1.造数据
        a = -6
        b = -5
        s = -1

        # 2.执行测试
        calc = Calc()
        result = calc.minus(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testminus2(self):
        # 1.造数据
        a = 6
        b = 5
        s = 1

        # 2.执行测试
        calc = Calc()
        result = calc.minus(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testminus3(self):
        # 1.造数据
        a = -6
        b = 5
        s = -11

        # 2.执行测试
        calc = Calc()
        result = calc.minus(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testminus4(self):
        # 1.造数据
        a = 6
        b = -5
        s = 11

        # 2.执行测试
        calc = Calc()
        result = calc.minus(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testminus5(self):
        # 1.造数据
        a = 0
        b = -5
        s = 5

        # 2.执行测试
        calc = Calc()
        result = calc.minus(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testminus6(self):
        # 1.造数据
        a = 0
        b = 5
        s = -5

        # 2.执行测试
        calc = Calc()
        result = calc.minus(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testminus7(self):
        # 1.造数据
        a = 100000000000000
        b = 50000000000000
        s = 50000000000000

        # 2.执行测试
        calc = Calc()
        result = calc.minus(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testmulti1(self):
        # 1.造数据
        a = -6
        b = -5
        s = 30

        # 2.执行测试
        calc = Calc()
        result = calc.multi(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testmulti2(self):
        # 1.造数据
        a = 6
        b = 5
        s = 30

        # 2.执行测试
        calc = Calc()
        result = calc.minus(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testmulti3(self):
        # 1.造数据
        a = -6
        b = 5
        s = -30

        # 2.执行测试
        calc = Calc()
        result = calc.multi(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testmulti4(self):
        # 1.造数据
        a = 6
        b = -5
        s = 30

        # 2.执行测试
        calc = Calc()
        result = calc.multi(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testmulti5(self):
        # 1.造数据
        a = 0
        b = -5
        s = 0

        # 2.执行测试
        calc = Calc()
        result = calc.multi(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testmulti6(self):
        # 1.造数据
        a = 0
        b = 5
        s = 0

        # 2.执行测试
        calc = Calc()
        result = calc.multi(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testmulti7(self):
        # 1.造数据
        a = 10000
        b = 5000
        s = 50000000

        # 2.执行测试
        calc = Calc()
        result = calc.multi(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testdevision1(self):
        # 1.造数据
        a = -6
        b = -5
        s = 1.2

        # 2.执行测试
        calc = Calc()
        result = calc.devision(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testdevision2(self):
        # 1.造数据
        a = 6
        b = 5
        s = 1.2

        # 2.执行测试
        calc = Calc()
        result = calc.devision(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testdevision3(self):
        # 1.造数据
        a = -6
        b = 5
        s = -1.2

        # 2.执行测试
        calc = Calc()
        result = calc.devision(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testdevision4(self):
        # 1.造数据
        a = 6
        b = -5
        s = -1.2

        # 2.执行测试
        calc = Calc()
        result = calc.devision(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testdevision5(self):
        # 1.造数据
        a = 0
        b = -5
        s = 0

        # 2.执行测试
        calc = Calc()
        result = calc.devision(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testdevision6(self):
        # 1.造数据
        a = 0
        b = 5
        s = 0

        # 2.执行测试
        calc = Calc()
        result = calc.devision(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

    def testdevision7(self):
        # 1.造数据
        a = 1000000000
        b = 5000
        s = 200000

        # 2.执行测试
        calc = Calc()
        result = calc.devision(a,b)

        # 3.比对实际结果与期望结果是否一致，
        self.assertEqual(result,s)

