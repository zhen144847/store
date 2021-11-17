import warnings
from unittest import  TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestTeacher(TestCase):

    # 教师管理查询
    def testCha(self):
        username = "jason"
        password = "admin"
        teacher = "曹士明"
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        # 隐性等待10秒
        chrome.implicitly_wait(10)
        expect = "曹士明"
        chrome.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/a[2]').click()
        chrome.find_element(By.XPATH,'//*[@id="loginname"]').send_keys(username)
        chrome.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
        chrome.find_element(By.XPATH,'//*[@id="submit"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="_easyui_tree_11"]/span[4]/a').click()
        chrome.find_element(By.XPATH, '//*[@id="sear_teaname"]').send_keys(teacher)
        chrome.find_element(By.XPATH, '//*[@id="search_user"]/span/span[1]').click()
        # 获取实际结果
        text = chrome.find_element(By.XPATH,'//*[@id="datagrid-row-r1-2-0"]/td[3]/div').text

        chrome.quit()
        # 断言
        self.assertEqual(expect,text)

    # 教师管理重置密码
    def testChong(self):
        warnings.simplefilter('ignore', ResourceWarning)
        username = "jason"
        password = "admin"
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        # 隐性等待10秒
        chrome.implicitly_wait(10)
        expect = "a4t8fa98sd8ag4ar8fd4a8s4df8a"
        chrome.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/a[2]').click()
        chrome.find_element(By.XPATH,'//*[@id="loginname"]').send_keys(username)
        chrome.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
        chrome.find_element(By.XPATH,'//*[@id="submit"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="_easyui_tree_11"]/span[4]/a').click()
        sleep(2)
        chrome.find_element(By.XPATH,'//*[@id="datagrid-row-r1-2-3"]/td[9]/div/a').click()
        sleep(1)
        # 获取实际结果
        text = chrome.switch_to.alert.text
        sleep(1)
        chrome.switch_to.alert.accept()

        sleep(1)
        chrome.quit()
        # 断言
        self.assertEqual(expect,text)



