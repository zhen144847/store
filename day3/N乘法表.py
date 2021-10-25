

def f(N):
    i = 1
    while i<= N:
        j = 1
        while j <= i:
            print("%d*%d=%d" % (j, i, j * i), end="\t")
            j += 1
        print()
        i += 1
N= int(input("请输入N的值："))
f(N)