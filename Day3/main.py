from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")


runner = HTMLTestRunner.HTMLTestRunner(
    title = "HKR测试报告",
    description="login测试报告",
    verbosity=1,
    stream=open(file="hkr.html",mode="w+",encoding="utf-8")
)

runner.run(tests)



















