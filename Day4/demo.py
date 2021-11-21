'''
el3 = driver.find_element_by_accessibility_id("发现")
el3.click()
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.ViewFlipper/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.EditText")
el6.send_keys("黄渤")
el7 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"搜索图标\"])[2]")
el7.click()
el8 = driver.find_element_by_id("com.sina.weibo:id/tv_search_keyword")
el8.send_keys("黄渤")
el9 = driver.find_element_by_id("com.sina.weibo:id/tag_content_layout")
el9.click()

'''

from appium import webdriver
import time

url = "127.0.0.1:4723/wd/hub"

param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "appPackage": "com.sina.weibo",
  "appActivity": "com.sina.weibo.SplashActivity"
}

driver = webdriver.Remote(url,param)
time.sleep(15)

el3 = driver.find_element_by_accessibility_id("发现")
el3.click()

el7 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc=\"搜索图标\"])[2]")
el7.click()
time.sleep(3)
el8 = driver.find_element_by_id("com.sina.weibo:id/tv_search_keyword")
el8.send_keys("黄渤")
time.sleep(2)
el9 = driver.find_element_by_id("com.sina.weibo:id/tag_content_layout")
el9.click()






























