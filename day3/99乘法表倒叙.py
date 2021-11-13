


#   倒序
for i in range(9, 0, -1):
    for j in range(1, i+1, 1):
        print(str(i)+"X"+str(j)+"="+str(j*i),end=" ")
    print()

#   正序
for i in (1,2,3,4,5,6,7,8,9):
    for j in (1,2,3,4,5,6,7,8,9):
        print(i,"X",j,"=",i*j,sep="",end="\t")
        if j==i:
            break
    print("")

