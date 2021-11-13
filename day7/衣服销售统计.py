

import xlrd

# 读表
wb = xlrd.open_workbook(filename='2020年每个月的销售情况.xlsx',encoding_override=True)

# 获取所有表格
sheets = wb.sheet_names()
print(sheets)
total = 0
num = 0
money = 0

down_jacket = 0
jeans = 0
dust_coat = 0
fur = 0
T_shirt = 0
best = 0
suits = 0
fur_clothing = 0
casual_pants = 0
fleece = 0
blouse = 0
cotton = 0
pencil_pants = 0
for i in range(wb.nsheets):
    sheet = wb.sheet_by_index(i)

    for x in range(1, sheet.nrows):
        total += int(sheet.cell_value(rowx=x, colx=4))
        money += int(sheet.cell_value(rowx=x, colx=4)) * float(sheet.cell_value(rowx=x, colx=2))
        if sheet.cell_value(rowx=x, colx=1) == '羽绒服':
            down_jacket += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '牛仔裤':
            jeans += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '风衣':
            dust_coat += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '皮草':
            fur += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == 'T血':
            T_shirt += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '马甲':
            best += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '皮衣':
            fur_clothing += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '小西装':
            suits += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '休闲裤':
            casual_pants += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '卫衣':
            fleece += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '衬衫':
            blouse += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '棉衣':
            cotton += int(sheet.cell_value(rowx=x, colx=4))
        elif sheet.cell_value(rowx=x, colx=1) == '铅笔裤':
            pencil_pants += int(sheet.cell_value(rowx=x, colx=4))

    num += sheet.nrows
    avg = total / num

print('总销售额', money)

print('平均每日销售数量', avg)

print('羽绒服月销量占比','{:.2%}'.format(down_jacket/total))
print('牛仔裤月销量占比','{:.2%}'.format(jeans/total))
print('风衣月销量占比','{:.2%}'.format(dust_coat/total))
print('皮草月销量占比','{:.2%}'.format(fur/total))
print('T血月销量占比','{:.2%}'.format(T_shirt/total))
print('马甲月销量占比','{:.2%}'.format(best/total))
print('小西装月销量占比','{:.2%}'.format(suits/total))
print('皮衣月销量占比','{:.2%}'.format(fur_clothing/total))
print('休闲裤月销量占比','{:.2%}'.format(casual_pants/total))
print('卫衣月销量占比','{:.2%}'.format(fleece/total))
print('衬衫月销量占比','{:.2%}'.format(blouse/total))
print('棉衣月销量占比','{:.2%}'.format(cotton/total))
print('铅笔裤月销量占比','{:.2%}'.format(pencil_pants/total))