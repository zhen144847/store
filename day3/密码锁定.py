count = 0
username = "root"  #登录用户名
user_password = "admin"   #登录密码

name = input("登录用户名：")

if name == username:
    while count <3:
        password = input("登录密码：")
        if name == username and password == user_password:
            print("欢迎%s!"%name)
            break
        else:
            print("账号和密码不匹配")
            count +=1
    else:
        print("对不起，您的账号连续输错三次密码已被锁定，请联系管理员。")
else:
    print("用户名不存在，请输入正确的用户名。")