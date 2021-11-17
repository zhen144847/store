import warnings
from unittest import  TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestHkr(TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

    # 修改头像用例
    def testXiuGai1(self):
        username = "zhangzhen"
        password = "123456"
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        # 隐性等待10秒
        chrome.implicitly_wait(10)
        expect = "成功修改头像!"
        chrome.find_element(By.XPATH,'//*[@id="loginname"]').send_keys(username)
        chrome.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
        chrome.find_element(By.XPATH,'//*[@id="submit"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="img"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="ul_pic"]/li[4]/img').click()
        sleep(1)

        # 获取实际结果
        chrome.save_screenshot("修改头像.jpg")
        text = chrome.find_element(By.CLASS_NAME, 'messager-body_panel-body_panel-body-noborder_window-body').text
        sleep(2)
        chrome.quit()

        #断言
        self.assertEqual(expect,text)

    # 上传头像用例
    def testShangChuan(self):
        username = "zhangzhen"
        password = "123456"
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        # 隐性等待10秒
        chrome.implicitly_wait(10)
        expect = "成功修改头像!"

        chrome.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(username)
        chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        chrome.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(1)
        chrome.find_element(By.XPATH, '//*[@id="img"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="lablefile"]').click()
        chrome.find_element(By.XPATH,'').send_keys(r"C:\fakepath\10条数据显示竖直滚动条.jpg")
        chrome.find_element(By.XPATH,'//*[@id="pic_btn"]').click()
        # 获取实际结果
        chrome.save_screenshot("修改头像.jpg")
        text = chrome.find_element(By.CLASS_NAME, '').text
        sleep(2)
        chrome.quit()

        #断言
        self.assertEqual(expect,text)

    # 提交今日评价
    def testTijiao1(self):
        time = "9(上晚自习)"
        teacher = "贾生"
        username = "zhangzhen"
        password = "123456"
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        # 隐性等待10秒
        chrome.implicitly_wait(10)
        expect = "提交成功!"

        chrome.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(username)
        chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        chrome.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[2]/td[2]/select').send_keys(time)
        chrome.find_element(By.XPATH,'//*[@id="tea_td"]/select').send_keys(teacher)
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[5]/td[3]/div/label[4]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[6]/td[2]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[7]/td[3]/div/label[4]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[8]/td[2]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[9]/td[2]/div/label[4]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[10]/td[3]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[11]/td[2]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[12]/td[2]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="textarea"]').send_keys("蹦蹦蹦")
        chrome.find_element(By.XPATH,'//*[@id="subtn"]').click()

        text = chrome.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[2]').text

        chrome.quit()

        # 断言
        self.assertEqual(expect, text)

    # 重复提交评价
    def testTijiao2(self):
        time = "9(上晚自习)"
        teacher = "贾生"
        username = "zhangzhen"
        password = "123456"
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        # 隐性等待10秒
        chrome.implicitly_wait(10)
        expect = "您今日已对该老师进行了评价,请勿重复评价！"

        chrome.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(username)
        chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        chrome.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[2]/td[2]/select').send_keys(time)
        chrome.find_element(By.XPATH,'//*[@id="tea_td"]/select').send_keys(teacher)
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[5]/td[3]/div/label[4]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[6]/td[2]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[7]/td[3]/div/label[4]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[8]/td[2]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[9]/td[2]/div/label[4]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[10]/td[3]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[11]/td[2]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="form_table"]/tbody/tr[12]/td[2]/div/label[2]/div').click()
        chrome.find_element(By.XPATH,'//*[@id="textarea"]').send_keys("蹦蹦蹦")
        chrome.find_element(By.XPATH,'//*[@id="subtn"]').click()

        text = chrome.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[2]').text

        chrome.quit()

        # 断言
        self.assertEqual(expect, text)

    # 修改个人信息
    def testGeRen(self):
        username = "zhangzhen"
        password = "123456"
        age = "66"
        sex = "女"
        dizhi = "北京市昌平区南邵镇北邵洼村"
        email = "zhang_zhenjob@163.com"
        ming = "层楼终究误少年，自由早晚乱余生。" \
               "你我山前没相逢，山后别想见。"
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        # 隐性等待10秒
        chrome.implicitly_wait(10)
        expect = "修改个人信息成功!"

        chrome.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(username)
        chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        chrome.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="_easyui_tree_8"]/span[4]/a').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="info"]/table/tbody/tr[1]/td[2]/input').send_keys(username)
        chrome.find_element(By.XPATH,'//*[@id="info"]/table/tbody/tr[3]/td[2]/input').send_keys(password)
        chrome.find_element(By.XPATH,'//*[@id="_easyui_textbox_input1"]').send_keys(age)
        chrome.find_element(By.XPATH, '//*[@id="info"]/table/tbody/tr[5]/td[2]/select').send_keys(sex)
        chrome.find_element(By.XPATH, '//*[@id="info"]/table/tbody/tr[6]/td[2]/input').send_keys(dizhi)
        chrome.find_element(By.XPATH, '//*[@id="info"]/table/tbody/tr[8]/td[2]/input').send_keys(email)
        chrome.find_element(By.XPATH, '//*[@id="info"]/table/tbody/tr[9]/td[2]/textarea').send_keys(ming)
        chrome.find_element(By.XPATH, '//*[@id="btn_modify"]').click()

        text = chrome.find_element(By.XPATH, '').text

        chrome.quit()

        # 断言
        self.assertEqual(expect, text)

    # 查询所有好友
    def testChaXun(self):
        username = "zhangzhen"
        password = "123456"
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        # 隐性等待10秒
        chrome.implicitly_wait(10)
        expect = "所有好友"

        chrome.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(username)
        chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        chrome.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="_easyui_tree_10"]/span[4]/a').click()

        text = chrome.find_element(By.XPATH,'//*[@id="tt"]/div[1]/div[3]/ul/li[2]/a[1]/span[1]').text

        chrome.quit()

        # 断言
        self.assertEqual(expect, text)

    # 退出
    def testTuiChu(self):
        username = "zhangzhen"
        password = "123456"
        chrome = webdriver.Chrome()
        chrome.get("http://localhost:8081/HKR")
        chrome.maximize_window()
        # 隐性等待10秒
        chrome.implicitly_wait(10)
        expect = "HKR.狼腾测试员综合办公系统"

        chrome.find_element(By.XPATH, '//*[@id="loginname"]').send_keys(username)
        chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        chrome.find_element(By.XPATH, '//*[@id="submit"]').click()
        sleep(1)
        chrome.find_element(By.XPATH,'//*[@id="top"]/div/a[2]/img').click()

        title = chrome.title

        chrome.quit()

        # 断言
        self.assertEqual(expect, title)













