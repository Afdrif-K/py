#encoding=utf-8
import pymysql
from time import sleep

class mysql:

    def __init__(self, username='root', passname='12345678', ip='localhost', datebasename='wk'):
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


    def query(self, table='eng', queryby=''):
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
            sql = 'select * from '+table+' '+queryby
            # print(sql)
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

    def insert(self, proc='insert_groupinfo', insertlist=[],table='eng',tables='DATES'):
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
            # cursor.callproc(proc, insertlist)
            sqls = ('INSERT INTO ' + 'eng' + '(id,Studentname,Teacher,Class,Classtime,day,赠送课时,赠送记录)VALUES' + "(" +"%s"+ ","+"\""+"%s"+"\""+","+"\""+"%s"+"\""+","+"\""+"%s"+"\""+","+"\""+"%s"+"\""+","+"\""+"%s" +"\""+","+"%s" +","+"\""+"%s" +"\""+ ")" ";" )%(insertlist[0],insertlist[1],insertlist[2],insertlist[3],insertlist[4],insertlist[5],insertlist[6],insertlist[7])
            print(sqls)
            cursor.execute(sqls)
            sleep(2)
            inser='ALTER TABLE '+tables+ ' add ' + insertlist[1] + " enum('1','2','Q1','Q2','S1','S2');"
            cursor.execute(inser)
            cursor.connection.commit()
            cursor.close()
            cursor = ''
        except pymysql.Error as e:
            self.insertStatus = e
        finally:
            if cursor:
                cursor.close()

    def update(self, proc='update_groupinfo', updatelist=[]):
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
            sql = ("UPDATE ENG SET " + "id=" + "%s" + "," + "Studentname=" + "\"" + "%s" + "\"" + "," + "Teacher=" + "\"" + "%s" + "\"" + "," + "Class=" + "\"" + "%s" + "\"" + "," + "Classtime=" + "\"" + "%s" + "\"" + "," + "day=" + "\"" + "%s" + "\""+ "," +"赠送课时=" + "\"" + "%s" + "\""+ "," +"赠送记录=" + "\"" + "%s" + "\"" + " WHERE " + "id=" + "%s" + ";") % (updatelist[1], updatelist[2], updatelist[3], updatelist[4], updatelist[5], updatelist[6],updatelist[7],updatelist[8],updatelist[0])
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

    def delete(self, deleteby, table='eng',tables='DATES',name=''):
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
            sql = 'DELETE FROM ' + 'eng ' + 'WHERE ' + deleteby +";"
            cursor.execute(sql)
            sleep(1)
            de='ALTER TABLE '+tables+ ' drop column ' + name + ";"
            cursor.execute(de)
            cursor.connection.commit()
            cursor.close()
            cursor = ''
        except pymysql.Error as e:
            self.deleteStatus = e
        finally:
            if cursor:
                cursor.close()

    def querys(self, table='DATES', querybys=[]):
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
            sql = 'SELECT DATE,WEEK,' + querybys[1] + ' FROM ' + table + ";"
            # print(sql)
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

    def Ri(self,table='DATES', querybys='',a=''):
        self.queryStatusr = 0
        result = ''
        cursor = ''
        title = ''
        try:
            sql = 'SELECT DATE,WEEK,' + querybys + ' FROM ' + table + ' WHERE '+ 'DATE' +' REGEXP\''+a+"\';"
            print(sql)
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            title = [i[0] for i in cursor.description]
            cursor.close()
            cursor = ''
        except pymysql.Error as e:
            self.queryStatusr = e
        finally:
            if cursor:
                cursor.close()
            return result, title


    def gos_update(self, table='DATES', updatelist='',name='',num=''):
        self.updateStatusg = 0
        cursor = ''
        print(name)
        try:
            cursor = self.__conn.cursor()
            sql ='UPDATE '+ table +' SET '+ name +'=\''+ num + '\''+' WHERE DATE=\''+updatelist[0]+'\';'
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            cursor = ''
        except pymysql.Error as e:
            self.updateStatusg = e
        finally:
            if cursor:
                cursor.close()