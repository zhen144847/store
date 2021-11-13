import unittest

from HTMLTestRunner import HTMLTestRunner

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\python_pycharm\test\day13",pattern="Test*.py")

# 2.创建一个运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "计算器的测试报告",
    description= "这是计算器加减乘除的测试报告",
    verbosity=1,
    stream = open(file ="计算器.html",mode="w+",encoding="utf-8")
)

# 3.执行
runner.run(tests)

# 4.使用代码来使用邮箱发送这个测试报告
# 用户名，授权码：（163.com 开启smtp授权码），将测试报告发送到我的邮箱里。
# 多写几个减法，乘法，除法的算法

















