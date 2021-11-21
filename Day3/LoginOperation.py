
'''
    将测试数据采用excel表的方式进行参数化。
    将测试结果回写到excel表中，
    使用邮件自动化发送附件。

    框架部署在window上，bat文件，定时执行这个框架的main.py文件。
        python.exe  mian.py
'''

class LoginOperation:

    # 在创建LoginOperation对象的时候，将driver对象申明为全局driver对象
    def __init__(self,driver):
        self.driver = driver


    def login(self,username,password):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)

        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

        self.driver.find_element_by_xpath("//*[@id='submit']").click()


    def getSuccessResult(self):
        return self.driver.title



    def getErrorResult(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text








