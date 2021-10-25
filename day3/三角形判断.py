



a = float(input("请输入第一条边：\n"))
b = float(input("请输入第二条边：\n"))
c = float(input("请输入第三条边：\n"))
if a+b>=c and a+c>=b and b+c>=a:
    print ("a=%s, b=%s, c=%s 可以构成三角形" % (a, b, c))
    if a == b == c:
        print ("a=%s, b=%s, c=%s 构成等边三角形" % (a, b, c))
    elif a == b and b == c and a == c:
        print ("a=%s, b=%s, c=%s 构成等腰三角形" % (a, b, c))
        if max([a, b, c]) ** 2 == min([a, b, c]) ** 2 * 2:
            print ("a=%s, b=%s, c=%s 构成直角三角形" % (a, b, c))
else:
    print ("a=%s, b=%s, c=%s 不可以构成三角形" % (a, b, c))


