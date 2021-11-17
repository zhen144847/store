# F:/自动化测试20/day01/练习的html/滑动验证/mousedrag.html
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time
driver = webdriver.Chrome()

driver.get(r"F:/自动化测试20/day01/练习的html/滑动验证/mousedrag.html")

driver.maximize_window()


# 1.driver浏览器交给ActionChains来进行管理

ac = ActionChains(driver)


ele = driver.find_element_by_xpath('//*[@id="box"]/div[3]')

ac.click_and_hold(ele).move_by_offset(300,0).perform()

ac.release()

