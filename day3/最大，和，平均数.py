
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
num3 = float(input("请输入第三个数字："))
num4 = float(input("请输入第四个数字："))
num5 = float(input("请输入第五个数字："))
num6 = float(input("请输入第六个数字："))
num7 = float(input("请输入第七个数字："))
num8 = float(input("请输入第八个数字："))
num9 = float(input("请输入第九个数字："))
num10 = float(input("请输入第十个数字："))

list = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]

print("您输入的最大数为：",max(list))
print("您输入十个数字的和为：",sum(list))
print("您输入数字的平均数为：",sum(list)/len(list))
