import random

print("*****************************")
print("*    中国工商银行           *")
print("*    账户管理系统           *")
print("*****************************")
print(" ")
print("*1、开户                    *")
print("*2、存钱                    *")
print("*3、取钱                    *")
print("*4、转账                    *")
print("*5、查询                    *")
print("*6、Bye!                    *")
print("*****************************")
# 初始化银行
bank = {}
# 'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
# 定义一个开户银行
bank_name = "皮燕子银行"


# 定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd(account, name, password, country, province, steert, door):
    if len(bank) >= 100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name] = {
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "steert": steert,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        return 1


# 定义存钱
def saveadd(name):
    if name in bank:
        print("您的余额为：%d" % bank[name]["money"])
        money = int(input("请输入您要存入的金额：")) + bank[name]["money"]
        bank[name]["money"] = money
        return True
    else:
        return False


# 定义取钱
def withdrawaladd(name, password):
    if name in bank and password == bank[name]["password"]:
        print("您的余额为%d" % bank[name]["money"])
        money = bank[name]["money"] - int(input("请输入您要取款的金额："))
        if money >= 0:
            bank[name]["money"] = money
            return 0
        elif money < 0:
            return 3
    elif name not in bank:
        return 1
    elif name in bank:
        if password != bank[name]["password"]:
            return 2


# 定义转账
def transferadd(zhuanru_name, zhuanchu_name, password):
    if zhuanru_name in bank and zhuanchu_name in bank:
        if password == bank[zhuanchu_name]["password"]:
            zhuanru_money = int(input("请输入您要转账的金额："))
            money = bank[zhuanchu_name]["money"] - zhuanru_money
            if money >= 0:
                bank[zhuanchu_name]['money'] = money
                bank[zhuanru_name]['money'] = zhuanru_money
                return 0
            elif money < 0:
                return 3


    elif zhuanchu_name not in bank or zhuanru_name not in bank:
        return 1
    elif password != bank[zhuanchu_name]['password']:
        return 2


# 定义查询
def inquireadd(name, password):
    if name in bank and password == bank[name]["password"]:
        return 1
    else:
        return 0


# 定义用户入参
def useradd():
    account = random.randint(10000000, 99999999)
    name = input("请输入您的名称")
    password = input("请输入您的密码")
    print("请输入你的详细信息")
    country = input("\t\t请输入您的国籍")  # \t ==tab
    province = input("\t\t请输入您的省份")
    steert = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    num = bankadd(account, name, password, country, province, steert, door)
    if num == 3:
        print("本银行已满请到其他银行开户")
    elif num == 2:
        print("用户已存在")
    elif num == 1:
        print("恭喜你开户成功，以下是您的详细信息")
        info = '''
                   ------------个人信息------------
                   用户名:%s
                   账号：%s
                   密码：*****
                   国籍：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (name, account, country, province, steert, door, bank[name]["money"], bank_name))


def cqadd():
    name = input("请输入您的名称：")
    cq = saveadd(name)
    if cq == True:
        info = '''
                ------------个人信息------------
                用户名:%s
                密码：*****
                余额：%s
                开户行名称：%s
        '''
        # 每个元素都可传入%
        print(info % (name, bank[name]["money"], bank_name))
    elif cq == False:
        print("用户名无效")


def qqadd():
    name = input("请输入您的名称：")
    password = input("请输入您的密码：")
    qq = withdrawaladd(name, password)

    if qq == 1:
        print("账号不存在")
    elif qq == 2:
        print("密码输入错误")
    elif qq == 3:
        print("账号余额不足")
    elif qq == 0:
        info = '''
               ------------个人信息------------
               用户名:%s               
               密码：*****
               余额：%s
               开户行名称：%s
           '''
        # 每个元素都可传入%
        print(info % (name, bank[name]["money"], bank_name))


def zzadd():
    zhuanchu_name = input("请输入您要转出的账户：")
    zhuanru_name = input("请输入您要转入的账户：")
    password = int(input("请输入您的用户密码："))
    zz = transferadd(zhuanchu_name, zhuanru_name, password)

    if zz == 1:
        print("转出或转入的账号不存在")
    elif zz == 2:
        print("转出账户的密码输入错误")
    elif zz == 3:
        print("转出账户的余额不足")
    elif zz == 0:
        info = '''
               ------------个人信息------------
               用户名:%s               
               密码：*****
               余额：%s
               开户行名称：%s
           '''
        # 每个元素都可传入%
        print(info % (zhuanchu_name, bank[zhuanchu_name]["money"], bank_name))
        info = '''
               ------------个人信息------------
               用户名:%s               
               密码：*****
               余额：%s
               开户行名称：%s
           '''
        # 每个元素都可传入%
        print(info % (zhuanru_name, bank[zhuanru_name]["money"], bank_name))


def cxadd():
    name = input("请输入您的姓名：")
    password = int(input("请输入您的用户密码："))
    cx = inquireadd(name, password)

    if cx == 1:
        print("账户信息不存在")
    elif cx == 2:
        print("密码输入错误")
    elif cx == 0:
        info = '''
                          ------------个人信息------------
                          用户名:%s
                          账号：%s
                          密码：%s
                          国籍：%s
                          省份：%s
                          街道：%s
                          门牌号：%s
                          余额：%s
                          开户行名称：%s
                      '''
        # 每个元素都可传入%

        print(info % (name, bank[name]['account'], bank[name]['password'], bank[name]['country'], bank[name]['province'],
        bank[name]['steert'], bank[name]['door'], bank[name]["money"], bank_name))


while False == 0:
    index = int(input("请输入您要办理的业务"))
    if index == 1:
        print("开户")
        useradd()
        print(bank)
    elif index == 2:
        print("存钱")
        cqadd()
    elif index == 3:
        print("取钱")
        qqadd()
    elif index == 4:
        print("转账")
        zzadd()
    elif index == 5:
        print("查询")
        cxadd()
    elif index == 6:
        print("Bey!")
        break
