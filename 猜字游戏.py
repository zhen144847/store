#猜字游戏，开始5个金币，猜错一次减一个，金币为0时可以充值，一轮只有20次猜字机会

import random
randint=random.randint(10,20)
print(randint)

i=1
gold = 5
while i<=20:
    num = int(input("猜数提示：取值范围10-20："))
    print("\n")
    if num==randint:
        print("猜对了")
        break
    elif num<randint:
        print("猜小了")
        gold = gold-1
        i+=1
    else:
        print("猜大了")
        gold = gold-1
        i+=1
    if gold == 0:
        print("金币不足，请输入充值数量：")
        a=int(input())
        gold=gold+a
    if i == 20:
        print("抱歉，最多只能猜20次")
        break

