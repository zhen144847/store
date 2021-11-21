from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


import time

url = "127.0.0.1:4723/wd/hub"

param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}

driver = webdriver.Remote(url, param)


time.sleep(10)
driver.find_element(By.ID, 'com.ss.android.ugc.aweme:id/bdb').click()

while True:
    time.sleep(15)

    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.85
    y2 = l['width'] * 0.5

    driver.swipe(x1, y1, x1, y2, 50)