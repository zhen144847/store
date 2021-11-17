'''
    鼠标的操作：
        1.悬停，滑动，拖动......
    ActionChians 事件链对象。
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time
driver = webdriver.Chrome()

driver.get(r"https://www.jd.com/")

driver.maximize_window()


# 1.driver浏览器交给ActionChains来进行管理

ac = ActionChains(driver)

ele = driver.find_element_by_link_text("我的京东")


ac.move_to_element(ele).perform() # 悬停

time.sleep(7)
ac.release() # 释放鼠标
