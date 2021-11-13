deep = 20#井的深度
skip = 3#每次跳跃的高度
slide = 2#每次下滑的距离
day = 0#计数的变量
while 1:#跳出来才结束的循环
    deep -= skip#深度逐渐变小
    if deep < 0:#这里就默认认为完全出来才算出来
        break
    deep += slide#晚上往下滑
    day += 1#天数逐渐加一
print("第",day,"天能出来")

