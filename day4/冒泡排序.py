

a = [5,2,4,7,9,1,3,5,4,0,6,1,3]

print(a)
for i in range(len(a)-1):   #表示i要做0到8共9轮循环
    for j in range(len(a)-1-i):   #表示每轮循环中j都要从0到8-i循环
        if a[j]>a[j+1]:
            q=a[j]
            a[j]=a[j+1]
            a[j+1]=q
print(a)