

A = 56
B = 78
def swap02(A, B):
    print("开始A为%d，B为%d" % (A, B))
    A = A + B
    B = A - B
    A = A - B
    print("结束B为%d，A为%d" % (A, B))
swap02(A,B)
