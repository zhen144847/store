import xlrd


class InitPage:
    # loginSuccessData = [
    #     {"username":"jason","password":"12345678","expect":"Student Login"},
    #     {"username":"admin1","password":"root","expect":"Student Login"},
    # ]
    loginSuccessData = xlrd.read(0)

    loginErrorData = xlrd.read(1)
    # [
    #     # id="msg_uname"
    #     {"username": "jason1", "password": "12345678", "expect": "账户名错误或密码错误!别瞎弄!"},
    #     {"username": "admin1", "password": "root1", "expect": "账户名错误或密码错误!别瞎弄!"},
    # ]






