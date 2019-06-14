#encoding=utf-8
import pymysql
from time import sleep
import datetime
import tkinter.messagebox

class mysql:

    def __init__(self, username='root', passname='12345678', ip='localhost', datebasename='yule'):
        """
        :param username: 连接数据库的用户名
        :param passname: 连接数据库的密码
        :param ip: 数据库ip
        :param datebasename:数据库名
        :param ipport: 数据库端口
        :desc: 初始化函数用于完成数据库连接，可以通过self.connStatus判断是否连接成功，成功则参数为0，不成功则返回错误详情
        """
        try:
            self.connStatus = '未连接'    # 连接状态
            self.queryStatus = 0    # 查询状态
            self.updateStatus = 0   # 更新状态
            self.deleteStatus = 0   # 删除状态
            self.insertStatus = 0   # 插入状态
            self.queryStatuss = 0
            self.queryStatusr = 0
            self.updateStatusg = 0
            self.__conn = ''
            self.__conStr = ip
            self.__conn = pymysql.connect(self.__conStr,username, passname, datebasename)
            self.connStatus = 0
        except pymysql.Error as e:
            self.connStatus = e


    def query(self, table='namelist', queryby=''):
        """
        :param table: 查询表名
        :param queryby: 查询条件，支持完整where, order by, group by 字句
        :return:返回数据集，列名
        """
        self.queryStatus = 0
        result = ''
        cursor = ''
        title = ''
        try:
            sql = 'select * from '+table+' '+queryby+';'
            print(sql)
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            title = [i[0] for i in cursor.description]
            cursor.close()
            cursor = ''
        except pymysql.Error as e:
            self.queryStatus = e
        finally:
            if cursor:
                cursor.close()
            return result, title

    def insert(self, insertlist=[]):
        """
        :param proc: 过程名
        :param insertlist: 参数集合，主键不能为空，参数必须与列对应，数量一致
        :desc: 此方法通过调用过程完成插入，需要在sql上完成存储过程，可以通过insertstatus的值判断是否成功
        """
        self.insertStatus = 0
        cursor = ''
        print(insertlist)
        print(insertlist[1])
        print(type(insertlist[1]))
        try:
            cursor = self.__conn.cursor()
            sqls = ('INSERT INTO ' + 'namelist' + '(Name,telephone,money,day)VALUES' + "(" +"\""+"%s"+"\""+","+"\""+"%s"+"\""+","+"\""+"%s"+"\""+","+"\""+"%s"+"\""+ ")" ";" )%(insertlist[1],insertlist[2],insertlist[3],insertlist[4])
            print(sqls)
            cursor.execute(sqls)
            sql_account= ('INSERT INTO '+'account'+'(telephone,changes,project,days)VALUES'+"("+"\""+"%s"+"\""+","+"\""+"%s"+"\""+","+"\""+"%s"+"\""+","+"\""+"%s"+"\""+ ")" ";" )%(insertlist[2],insertlist[3],'充值',insertlist[4])
            print(sql_account)
            cursor.execute(sql_account)
            cursor.connection.commit()
            cursor.close()
            cursor = ''
        except pymysql.Error as e:
            self.insertStatus = e
        finally:
            if cursor:
                cursor.close()

    def update(self, updatelist=[]):
        """
        :param proc: 存储过程名
        :param updatelist: 更新的集合，第一个为查询主键，后面的参数为对应的列，可以更新主键。
        :desc: 此方法通过调用存储过程完成更新操作，可以通过updatestatus的值判断是否成功
        """
        self.updateStatus = 0
        cursor = ''
        try:
            cursor = self.__conn.cursor()
            # cursor.callproc(proc, updatelist)
            sql = ("UPDATE namelist SET " + "No=" + "%s" + "," + "Name=" + "\"" + "%s" + "\"" + "," + "telephone=" + "\"" + "%s" + "\"" + "," + "money=" + "\"" + "%s" + "\"" + "," + "day=" + "\"" + "%s" + "\""  + " WHERE " + "No=" + "%s" + ";") % (updatelist[1], updatelist[2], updatelist[3], updatelist[4], updatelist[5], updatelist[0])
            print(sql)
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            cursor = ''
        except pymysql.Error as e:
            self.updateStatus = e
        finally:
            if cursor:
                cursor.close()

    def delete(self, deleteby, table='namelist'):
        """
        :param deleteby: 删除的条件，除where关键字以外的内容
        :param table: 要删除的表名
        :desc:可以通过deletestatus判断是否成功删除
        """
        self.deleteStatus = 0
        cursor = ''
        # print(name)
        try:
            cursor = self.__conn.cursor()
            sql = 'DELETE FROM ' + 'namelist ' + 'WHERE ' + deleteby +";"
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            cursor = ''
        except pymysql.Error as e:
            self.deleteStatus = e
        finally:
            if cursor:
                cursor.close()

    def querys(self, table='account', querybys=[]):
        """
        :param table: 查询表名
        :param queryby: 查询条件，支持完整where, order by, group by 字句
        :return:返回数据集，列名
        """
        self.queryStatuss = 0
        result = ''
        cursor = ''
        title = ''
        try:
            sql = 'SELECT *'  + ' FROM ' + table + " WHERE telephone=" + querybys[2]+";"
            print(sql)
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            title = [i[0] for i in cursor.description]
            cursor.close()
            cursor = ''
        except pymysql.Error as e:
            self.queryStatuss = e
        finally:
            if cursor:
                cursor.close()
            return result, title

    def update_account(self, updatelist=[],up={}):
        """
        :param proc: 存储过程名
        :param updatelist: 更新的集合，第一个为查询主键，后面的参数为对应的列，可以更新主键。
        :desc: 此方法通过调用存储过程完成更新操作，可以通过updatestatus的值判断是否成功
        """
        self.updateStatus = 0
        cursor = ''
        try:
            cursor = self.__conn.cursor()
            # cursor.callproc(proc, updatelist)
            q=int(updatelist[1])
            w=30*int(updatelist[2])
            e=35*int(updatelist[3])
            r=10*int(updatelist[4])
            o=int(updatelist[5])
            a=q-w-e-r+o
            if int(a)<0:
                aa = tkinter.messagebox.askokcancel('余额不足', '会员余额不足，请充值')
            else:
                # a=int((int(updatelist[1])) - (35*int(updatelist[2])) - (45*int(updatelist[3])) - (10*updatelist[4]) + (int(updatelist[5])))
                sql_a= ("UPDATE namelist SET " + "money=" + "%d" + " WHERE " + "telephone=" + "%s")%(a,updatelist[0])
                cursor.execute(sql_a)
                T=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(up)
                if up['喂鱼'] != '0':
                    sql = ("INSERT INTO "+ "account(telephone,changes,project,days)VALUES("+"%s"+","+"%s"+","+"\'"+"%s"+"\'"+","+"\'"+"%s"+"\'"+");")%(updatelist[0],'-'+str(30*int(up['喂鱼'])),'喂鱼',T)
                    print(sql)
                    cursor.execute(sql)
                if up['捞鱼'] != '0':
                    sql = ("INSERT INTO "+ "account(telephone,changes,project,days)VALUES("+"%s"+","+"%s"+","+"\'"+"%s"+"\'"+","+"\'"+"%s"+"\'"+");")%(updatelist[0],'-'+str(35*int(up['捞鱼'])),'捞鱼',T)
                    print(sql)
                    cursor.execute(sql)
                if up['鱼盒'] != '0':
                    sql = ("INSERT INTO "+ "account(telephone,changes,project,days)VALUES("+"%s"+","+"%s"+","+"\'"+"%s"+"\'"+","+"\'"+"%s"+"\'"+");")%(updatelist[0],'-'+str(10*int(up['鱼盒'])),'鱼盒',T)
                    print(sql)
                    cursor.execute(sql)
                if up['充值'] != '0':
                    sql = ("INSERT INTO "+ "account(telephone,changes,project,days)VALUES("+"%s"+","+"%d"+","+"\'"+"%s"+"\'"+","+"\'"+"%s"+"\'"+");")%(updatelist[0],int(up['充值']),'充值',T)
                    print(sql)
                    cursor.execute(sql)
                cursor.connection.commit()
                cursor.close()
                cursor = ''
        except pymysql.Error as e:
            self.updateStatus = e
        finally:
            if cursor:
                cursor.close()