from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://www.jd.com/")

driver.maximize_window()
driver.find_element_by_xpath("//*[@id='key']").send_keys("thinkpad E580")

driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()


time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img').click()

# 获取所有的窗口句柄
data = driver.window_handles #["s001","s002"]

driver.switch_to.window(data[1])

# 添加购物车
driver.find_element_by_xpath('//*[@id="InitCartUrl"]').click()

