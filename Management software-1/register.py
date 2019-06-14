# coding=utf-8
import pymysql
from tkinter import *

class loginPage(object):
    def __init__(self, master, info='欢迎进入注册页面'):
        self.master = master
        self.mainlabel = Label(master, text=info, justify=CENTER)
        self.mainlabel.grid(row=0, columnspan=3)

        self.user = Label(master, text='注册用户名：', borderwidth=3)
        self.user.grid(row=1, sticky=W)

        self.pwd = Label(master, text='注册密码：', borderwidth=3)
        self.pwd.grid(row=2, sticky=W)

        self.userEntry = Entry(master)
        self.userEntry.grid(row=1, column=1, columnspan=3)
        self.userEntry.focus_set()

        self.pwdEntry = Entry(master, show='*')
        self.pwdEntry.grid(row=2, column=1, columnspan=3)

        self.loginButton = Button(master, text='确定注册', borderwidth=2, command=self.login)
        self.loginButton.grid(row=3, column=1)

        self.clearButton = Button(master, text='清除', borderwidth=2, command=self.clear)
        self.clearButton.grid(row=3, column=2)

    def login(self):
        self.username = self.userEntry.get().strip()
        self.passwd = self.pwdEntry.get().strip()
        db = pymysql.connect("localhost", "root", "12345678", "wk")
        cursor = db.cursor()
        # sql = "INSERT INTO user(name, pwd) VALUES ('%s', '%s')" % (self.username, self.passwd)
        sql="CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" % (self.username, self.passwd)
        print(sql)
        try:
            cursor.execute(sql)
            print ("数据插入成功！！！")
            cursor.execute("GRANT GRANT OPTION ON *.* TO '%s'@'localhost';" % (self.username))
            cursor.execute("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER ON *.* TO '%s'@'localhost';" % (self.username))
            db.commit()
            from tkinter import messagebox
            messagebox.showinfo(title='成功注册', message='成功注册 ')
            root.destroy()
        except:
            print ("数据插入失败！！！")
            db.rollback()
        db.close()

    def clear(self):
        self.userEntry.delete(0, END)
        self.pwdEntry.delete(0, END)

if __name__ == '__main__':
    root = Tk()
    root.title("注册")
    root.geometry('250x120+650+330')
    myLogin = loginPage(root)
    mainloop()
