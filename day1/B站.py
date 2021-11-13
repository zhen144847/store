from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()
#隐性等待10秒
chromeDriver.implicitly_wait(10)
# 打开B站网址
chromeDriver.get("https://www.bilibili.com/")
# 窗口最大化
chromeDriver.maximize_window()
#点击登录
chromeDriver.find_element(By.XPATH,"//*[@id='i_cecream']/div[1]/div[1]/ul[2]/li[1]/li/div/div").click()
handles2 = chromeDriver.window_handles
chromeDriver.switch_to.window(handles2[-1])
#输入用户名，密码
chromeDriver.find_element(By.XPATH,"//*[@id='login-username']").send_keys('15733047417')
chromeDriver.find_element(By.XPATH,"//*[@id='login-passwd']").send_keys('zhangzhen')
#点击登录按钮
chromeDriver.find_element(By.XPATH,"//*[@id='geetest-wrap']/div/div[5]/a[1]").click()
#点击鬼畜，进入鬼畜专区
chromeDriver.find_element(By.XPATH,"//*[@id='i_cecream']/div[1]/div[3]/div[2]/a[10]").click()
sleep(2)
#切换到新打开的窗口定位元素
handles = chromeDriver.window_handles
chromeDriver.switch_to.window(handles[-1])
sleep(2)
#寻找搜索输入框
chromeDriver.find_element(By.XPATH,"//*[@id='nav-searchform']/input").send_keys("【有何不可】【王司徒单曲】王朗的七夕献唱")
sleep(2)
# 点击搜索按钮
chromeDriver.find_element(By.XPATH,"//*[@id='nav-searchform']/div").click()
#切换到新打开的窗口定位元素
handles1 = chromeDriver.window_handles
chromeDriver.switch_to.window(handles1[-1])
sleep(3)
#选择鬼畜视频
chromeDriver.find_element(By.XPATH,"//*[@id='all-list']/div[1]/div[2]/ul/li[1]/div/div[1]/a").click()

sleep(350)
# 退出浏览器
chromeDriver.quit()