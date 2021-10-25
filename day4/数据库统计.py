# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
# ]
#
names=[["曹操","56","男","106","IBM","500","50"],
      ["大乔","19","女","203","微软","501","60",],
      ["小乔","19","女","210","Oracle","600","60"],
      ["许褚","45","男","230","Tencent","700","10"]
      ]
i=0
sum=0
while i<4:
    print(int(names[i][5]))
    sum=int(names[i][5])+sum
    i=i+1

a=sum/i
print("每个人的平均薪资为：%d"%a)

i=0
sum=0
while i<4:
    print(int(names[i][1]))
    sum=int(names[i][1])+sum
    i=i+1

a=sum/i
print("每个人的平均年龄为：%d"%a)

man = 0
woman = 0
j=0
while True:
    if names[j][2]=="男":
        man+=1
        j+=1
    elif names[j][2]=="女":
        woman+=1
        j+=1
    if j==len(names):
        break
print('公司男员工为%d名，女员工为%d名' %(man ,woman))