import xlrd # 读excel的包

file_name="F:\\BaiduNetdiskDownload\\game.xls"
data = xlrd.open_workbook(file_name)#文件名以及路径，如果路径或者文件名有中文给前面加一个 r
names = data.sheet_names()                  #返回book中所有工作表的名字

table = data.sheets()[0]                    #通过索引顺序获取
table = data.sheet_by_index(0)     #通过索引顺序获取
table = data.sheet_by_name("Sheet1")      #通过名称获取
# 以上三个函数都会返回一个xlrd.sheet.Sheet()对象



#行操作
nrows = table.nrows
# 获取该sheet中的行数，注，这里table.nrows后面不带().
for i in range(nrows):
    print(table.row(i))#二者等价，返回对象列表
    print(table.row_slice(i))
    print(table.row_values(i, start_colx=0, end_colx=None))#单纯的列表
    #     # 返回由该行中所有单元格的数据组成的列表


#列操作
ncols = table.ncols
# 获取列表的有效列数
for i in range(ncols):
    table.col(i, start_rowx=0, end_rowx=None)#这三个和上面的一样
    # 返回由该列中所有的单元格对象组成的列表
    table.col_slice(i, start_rowx=0, end_rowx=None)
    # 返回由该列中所有的单元格对象组成的列表
    table.col_values(i, start_rowx=0, end_rowx=None)
    # 返回由该列中所有单元格的数据组成的列表



table.cell(0,0)
    # 返回单元格对象
table.cell_value(0,0)
    # 返回对应位置单元格中的数据