from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()
#隐性等待10秒
chromeDriver.implicitly_wait(10)
# 打开京东网址
chromeDriver.get("https://www.jd.com/")
# 窗口最大化
chromeDriver.maximize_window()
#寻找搜索输入框
chromeDriver.find_element(By.ID,"key").send_keys("小米手机")
# 点击搜索按钮
chromeDriver.find_element(By.CLASS_NAME,"button").click()
#选择CPU型号骁龙855plus
chromeDriver.find_element(By.XPATH,"//*[@id='J_selector']/div[1]/div/div[2]/div[1]/ul/li[2]/a").click()
#点击商品，打开新的窗口，进入详情界面
chromeDriver.find_element(By.XPATH,"//*[@id='J_goodsList']/ul[1]/li[1]/div/div[4]/a/em").click()
#切换到新打开的窗口定位元素
handles = chromeDriver.window_handles
chromeDriver.switch_to.window(handles[-1])

time.sleep(10)
# 退出浏览器
chromeDriver.quit()