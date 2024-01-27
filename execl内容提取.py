import xlrd  #读取
import xlwt  #写入
import os,sys
print(os.getcwd())
xlsx = xlrd.open_workbook(r'E:\code\Python\2.文件操作\提取\1.xls') #打开xls
table = xlsx.sheet_by_index(0)  #找到工作表，第几表，如0,还可以用名称,如Sheet1
lieshu = table.ncols   #获取列数
hangshu = table.nrows #获取列数

#table.row_values(3)
cols = table.col_values(1) #获取第2列内容(数组)
print(cols)
print(table.cell(1,1).value) #第二种写法，table.cell(行,列).value
#table = xlsx.sheet_by_name("Sheet1") #根据名称来打开表，如Sheet1
#print(table.cell_value(0,0)) #第0行第0列，table.cell_value(行,列)

#--------------------写入--------------------

new = xlwt.Workbook()#新建一个工作簿
sheet = new.add_sheet('gongzuobu')#新建一个工作表，表名也可以不用写，不写就是默认的

for i in range(0,len(cols)):  #从0到尾

    sheet.write(i,0,cols[i])  
#sheet.write(0,0,'test') #第0行第0列写入test
new.save(r'C:\Users\Administrator\Desktop\123.xls')#保存并新建文件



