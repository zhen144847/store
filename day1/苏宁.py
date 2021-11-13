from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()
#隐性等待10秒
chromeDriver.implicitly_wait(10)

# 打开苏宁网址
chromeDriver.get("https://www.suning.com/")

# 窗口最大化
chromeDriver.maximize_window()

#寻找搜索输入框
chromeDriver.find_element(By.ID,"searchKeywords").send_keys("手机")
# 点击搜索按钮
chromeDriver.find_element(By.ID,"searchSubmit").click()
#点击商品,打开新的窗口
chromeDriver.find_element(By.NAME,"ssdsn_search_pro_name03-1_0_0_12282645493_0000000000").click()
time.sleep(3)
#切换到新打开的窗口定位元素，两种方法
handles = chromeDriver.window_handles
chromeDriver.switch_to.window(handles[-1])
# window_1 = chromeDriver.current_window_handle
# windows = chromeDriver.window_handles
# for current_window in windows:
#     if current_window != window_1:
#         chromeDriver.switch_to.window(current_window)
time.sleep(3)
#点击加入购物车
chromeDriver.find_element(By.NAME,"item_12282645493_gmq_buy01").click()
#点击去购物车结算
chromeDriver.find_element(By.NAME,"cart1_go").click()
#点击结算
chromeDriver.find_element(By.NAME,"icart1_ope_buy01").click()
time.sleep(10)
#关闭当前页面
chromeDriver.close()
time.sleep(5)
# 退出浏览器
chromeDriver.quit()