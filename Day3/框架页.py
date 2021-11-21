'''
    自动化有些元素定位不到啥问题？
        1.页面有可能是框架页的方式进行开发，直接定位不行。
    为什么做最大化操作？
        不最大化，有的元素没法显示，就没法定位

    1.
        switch_to:
            alert:弹框
            frame:框架页
            windows:窗口
'''
from  selenium import webdriver

driver = webdriver.Chrome()


driver.get(r"F:/自动化测试20/练习的html/main.html")

driver.maximize_window()

driver.switch_to.frame("frame")


driver.find_element_by_xpath("//*[@id='input1']").send_keys("jason!")






















