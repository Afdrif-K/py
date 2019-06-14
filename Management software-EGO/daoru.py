import xlrd
import pymysql
#读取EXCEL中内容到数据库中
wb = xlrd.open_workbook('./dates.xls')
sh = wb.sheet_by_index(0)
dfun=[]
nrows = sh.nrows  #行数
ncols = sh.ncols  #列数
fo=[]

fo.append(sh.row_values(0))
for i in range(1,nrows):
      dfun.append(sh.row_values(i))

conn=pymysql.connect(host='localhost',user='root',passwd='12345678',db='wk')
cursor=conn.cursor()
#创建table
cursor.execute("create table dates("+fo[0][0]+" varchar(100),primary key(date));")
#创建table属性
for i in range(1,ncols):
    if i ==1:
        cursor.execute("alter table dates add "+fo[0][i]+" varchar(100);")
    else:
        cursor.execute("alter table dates add " + fo[0][i] + " enum('1','2','Q1','Q2','S1','S2');")
val=''
for i in range(0,ncols):
    val = val+'%s,'
print (dfun)

cursor.executemany("insert into dates values("+val[:-1]+");" ,dfun)
conn.commit()