import xlwings as xw
app = xw.App(visible=True,add_book=False)#新建工作簿 (如果不接下一条代码的话，Excel只会一闪而过，卖个萌就走了）
wb = app.books.add()