from unittest import  TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestHkr(TestCase):

    # 注册成功用例
    def testZhuCeSuccess1(self):
        # 准备数据
        username = "zhangzhen"
        name = "张振"
        password = "123456"
        age = "18"
        # sex = "男"
        # work = "Python自动化"
        email = "1448476433@qq.com"
        phone = "18501012535"
        # 期望数据
        expect = "注册成功!请返回登录!"

        # 执行测试
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        chrome.find_element(By.XPATH,"/html/body/div/div/div[1]/div[2]/a[1]").click()
        sleep(3)
        chrome.find_element(By.XPATH,"//*[@id='loginname']").send_keys(username)
        sleep(3)
        chrome.find_element(By.XPATH, "//*[@id='msform']/fieldset[1]/input[2]").send_keys(name)
        sleep(3)
        chrome.find_element(By.XPATH,"//*[@id='pwd']").send_keys(password)
        sleep(3)
        chrome.find_element(By.XPATH, "//*[@id='msform']/fieldset[1]/input[4]").send_keys(password)
        sleep(3)
        #点击下一步
        chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[1]/input[5]').click()
        sleep(3)
        chrome.find_element(By.XPATH,'//*[@id="valid_age"]').send_keys(age)
        sleep(3)
        # chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[2]/select[1]').send_keys(sex)
        # chrome.find_element(By.XPATH,'//*[@id="classname"]').send_keys(work)
        #点击下一步
        chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[2]/input[3]').click()
        sleep(3)
        chrome.find_element(By.XPATH,'//*[@id="reg_mail"]').send_keys(email)
        sleep(3)
        chrome.find_element(By.XPATH,'//*[@id="reg_phone"]').send_keys(phone)
        sleep(3)
        chrome.find_element(By.XPATH,'//*[@id="btn_reg"]').click()
        sleep(3)

        # 获取实际结果
        text = chrome.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]').text
        sleep(5)
        chrome.quit()

        #断言
        self.assertEqual(expect,text)

    # 年龄15-75岁验证
    def testZhuCeError2(self):
        # 准备数据
        username = "zhangzhen12"
        name = "张振"
        password = "123456"
        age = "14"
        # sex = "男"
        # work = "Python自动化"
        email = "1448436432@qq.com"
        phone = "18501012566"
        # 期望数据
        expect = "失败"

        # 执行测试
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        chrome.find_element(By.XPATH,"/html/body/div/div/div[1]/div[2]/a[1]").click()
        sleep(1)
        chrome.find_element(By.XPATH,"//*[@id='loginname']").send_keys(username)
        sleep(1)
        chrome.find_element(By.XPATH, "//*[@id='msform']/fieldset[1]/input[2]").send_keys(name)
        sleep(1)
        chrome.find_element(By.XPATH,"//*[@id='pwd']").send_keys(password)
        sleep(1)
        chrome.find_element(By.XPATH, "//*[@id='msform']/fieldset[1]/input[4]").send_keys(password)
        sleep(1)
        #点击下一步
        chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[1]/input[5]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="valid_age"]').send_keys(age)
        sleep(1)
        # chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[2]/select[1]').send_keys(sex)
        # chrome.find_element(By.XPATH,'//*[@id="classname"]').send_keys(work)
        #点击下一步
        chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[2]/input[3]').click()
        sleep(1)
        chrome.switch_to.alert.accept()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="reg_mail"]').send_keys(email)
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="reg_phone"]').send_keys(phone)
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="btn_reg"]').click()
        sleep(1)

        # 获取实际结果
        text = chrome.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]').text
        sleep(5)
        chrome.save_screenshot("年龄.jpg")
        sleep(5)
        chrome.quit()

        #断言
        self.assertEqual(expect,text)

    # 登录名重复验证
    def testZhuCeError3(self):
        # 准备数据
        username = "zhangzhen"
        name = "张振"
        password = "123456"
        age = "18"
        # sex = "男"
        # work = "Python自动化"
        email = "1448476423@qq.com"
        phone = "18501222536"
        # 期望数据
        expect = "该登录名已被人使用!"

        # 执行测试
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        chrome.find_element(By.XPATH,"/html/body/div/div/div[1]/div[2]/a[1]").click()
        sleep(1)
        chrome.find_element(By.XPATH,"//*[@id='loginname']").send_keys(username)

        chrome.find_element(By.XPATH, "//*[@id='msform']/fieldset[1]/input[2]").send_keys(name)

        chrome.find_element(By.XPATH,"//*[@id='pwd']").send_keys(password)

        chrome.find_element(By.XPATH, "//*[@id='msform']/fieldset[1]/input[4]").send_keys(password)

        #点击下一步
        chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[1]/input[5]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="valid_age"]').send_keys(age)

        # chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[2]/select[1]').send_keys(sex)
        # chrome.find_element(By.XPATH,'//*[@id="classname"]').send_keys(work)
        #点击下一步
        chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[2]/input[3]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="reg_mail"]').send_keys(email)
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="reg_phone"]').send_keys(phone)
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="btn_reg"]').click()
        sleep(1)

        # 获取实际结果
        text = chrome.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]').text
        sleep(3)
        chrome.quit()

        #断言
        self.assertEqual(expect,text)

    # 邮箱重复验证
    def testZhuCeError4(self):
        # 准备数据
        username = "zhangzhen"
        name = "张振"
        password = "123456"
        age = "18"
        # sex = "男"
        # work = "Python自动化"
        email = "1448476423@qq.com"
        phone = "18501222536"
        # 期望数据
        expect = "该邮箱已被人使用!"

        # 执行测试
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        chrome.find_element(By.XPATH,"/html/body/div/div/div[1]/div[2]/a[1]").click()
        sleep(1)
        chrome.find_element(By.XPATH,"//*[@id='loginname']").send_keys(username)

        chrome.find_element(By.XPATH, "//*[@id='msform']/fieldset[1]/input[2]").send_keys(name)

        chrome.find_element(By.XPATH,"//*[@id='pwd']").send_keys(password)

        chrome.find_element(By.XPATH, "//*[@id='msform']/fieldset[1]/input[4]").send_keys(password)

        #点击下一步
        chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[1]/input[5]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="valid_age"]').send_keys(age)

        # chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[2]/select[1]').send_keys(sex)
        # chrome.find_element(By.XPATH,'//*[@id="classname"]').send_keys(work)
        #点击下一步
        chrome.find_element(By.XPATH,'//*[@id="msform"]/fieldset[2]/input[3]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="reg_mail"]').send_keys(email)
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="reg_phone"]').send_keys(phone)
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="btn_reg"]').click()
        sleep(1)

        # 获取实际结果
        text = chrome.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]').text
        sleep(3)
        chrome.quit()

        #断言
        self.assertEqual(expect,text)

