from unittest import  TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestHkr(TestCase):

    # 登录成功用例
    def testLoginSuccess(self):
        # 准备数据
        username = "jason"
        password = "1234567"
        # 期望数据
        expect = "Student Login"

        # 执行测试
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()

        chrome.find_element(By.XPATH,"//*[@id='loginname']").send_keys(username)
        chrome.find_element(By.XPATH,"//*[@id='password']").send_keys(password)

        chrome.find_element(By.XPATH,"//*[@id='submit']").click()


        # 获取实际结果
        title = chrome.title


        chrome.quit()

        #断言
        self.assertEqual(expect,title)



    # 登录失败用例
    def testLoginError(self):
        # 准备数据
        username = "jason"
        password = "123456789"
        # 期望数据
        expect = "账户名错误或密码错误!别瞎弄!"  # id=n=msg_uname



        # 执行测试
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()

        chrome.find_element(By.XPATH,"//*[@id='loginname']").send_keys(username)
        chrome.find_element(By.XPATH,"//*[@id='password']").send_keys(password)

        chrome.find_element(By.XPATH,"//*[@id='submit']").click()


        # 获取实际结果
        text = chrome.find_element(By.XPATH,"//*[@id='msg_uname']").text

        chrome.quit()

        #断言
        self.assertEqual(expect,text)
























