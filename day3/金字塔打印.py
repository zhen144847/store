row = 1
while row <= 7:
    # 空格
    k = 6
    while k >= row:
        print(' ', end='')
        k -= 1
    # 星星
    x = 1
    while x <= row:
        print('*', end=' ')
        x += 1
    row += 1
    print()  # 换行
