#encoding=utf-8
import xlrd
import pymysql
from xlutils.copy import copy
import os

def out():
    conn=pymysql.connect(host='localhost',user='root',passwd='12345678',db='wk')
    cursor=conn.cursor()
    count = cursor.execute('select Studentname from eng;')
    print('has %s record' % count  )
    #重置游标位置
    cursor.scroll(0,mode='absolute')
    #搜取所有结果
    results = cursor.fetchall()
    # print(results)
    #获取MYSQL里的数据字段
    fields = cursor.description
    print(fields)
    wbk = xlrd.open_workbook('./dates.xls')
    wb =copy(wbk)
    ws = wb.get_sheet(0)
    # sheet = ws.add_sheet('ENG',cell_overwrite_ok=True)
    jcs=2
    for jcs in range(2,len(results)+2):
        ws.write(0,jcs,results[jcs-2][0])
    wb.save('../dates.xls')
    os.remove('./dates.xlsx')
    os.remove('./dates.xls')