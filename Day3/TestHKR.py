from unittest import TestCase
from ddt import  ddt
from ddt import data
from ddt import unpack
import time
from InitPage import InitPage
from LoginOperation import LoginOperation
from selenium import webdriver


@ddt
class TestHKR(TestCase):

    @data(*InitPage.loginSuccessData)
    def testLoginSuccess(self,testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]


        driver = webdriver.Chrome()
        driver.get("http://localhost:8081/HKR")
        driver.maximize_window()
        # 执行登陆逻辑
        login = LoginOperation(driver)
        time.sleep(2)
        login.login(username,password)
        time.sleep(2)
        # 获取实际结果
        result = login.getSuccessResult()

        driver.quit()

        # 断言
        self.assertEqual(result,expect)



    @data(*InitPage.loginErrorData)
    def testLoginError(self,testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]


        driver = webdriver.Chrome()
        driver.get("http://localhost:8081/HKR")
        driver.maximize_window()
        # 执行登陆逻辑
        login = LoginOperation(driver)
        time.sleep(3)
        login.login(username,password)
        time.sleep(2)
        # 获取实际结果
        result = login.getErrorResult()

        if result != expect:
            driver.save_screenshot("失败.jpg")
            xlwt.write("测试不通过！")

        driver.quit()

        # 断言
        self.assertEqual(result,expect)
















