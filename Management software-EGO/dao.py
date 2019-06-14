#coding=utf-8
import xlwt
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='12345678',db='wk')
cursor=conn.cursor()
count = cursor.execute('select * from eng;')
print('has %s record' % count  )
#重置游标位置
cursor.scroll(0,mode='absolute')
#搜取所有结果
results = cursor.fetchall()
print(results)
#测试代码，print results
#获取MYSQL里的数据字段
fields = cursor.description
print(fields)
#将字段写入到EXCEL新表的第一行
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('ENG',cell_overwrite_ok=True)
for ifs in range(0,len(fields)):
    sheet.write(0,ifs,fields[ifs][0])
ics=1
jcs=0
for ics in range(1,len(results)+1):
    for jcs in range(0,len(fields)):
        sheet.write(ics,jcs,results[ics-1][jcs])
wbk.save('./学生信息表.xls')