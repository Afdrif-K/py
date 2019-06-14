#encoding=utf-8
from guiPy import *
from register import *
import pymysql
from tkinter import *
import os

def inset_get():
    mysql_host = text_iddr.get()
    mysql_user = text_user.get()
    mysql_pwd = text_pwd.get()
    print(mysql_host, mysql_user, mysql_pwd)
    try:
        global db_login
        db_login = pymysql.connect(host="%s" % mysql_host, user="%s" % mysql_user, passwd="%s" % mysql_pwd, db="wk",charset="utf8")
        init_window.destroy()
        MainWindow()
    except:
        print("ERROR:mysql not connect")
        from tkinter import messagebox
        messagebox.showinfo(title='login faild', message='登录失败，请重新登录 ')

def center_windowas(roots, width, height):
    screenwidth = roots.winfo_screenwidth()
    screenheight = roots.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    roots.geometry(size)

def register_info():
    roots = Tk()
    roots.title("注册")
    center_windowas(roots,250,120)
    # roots.geometry('250x120+650+330')
    loginPage(roots)

def center_windowa(init_window, width, height):
    screenwidth = init_window.winfo_screenwidth()
    screenheight = init_window.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    init_window.geometry(size)

init_window=Tk()
init_window.title("数据库的连接")
center_windowa(init_window,700,400)
# init_window.geometry('700x400+440+200')

canvas = Canvas(init_window, height=150, width=430)
canvas.pack(side=TOP)
pa=os.path.dirname(os.path.realpath(__file__))
image_file = PhotoImage(file=pa+'\\timg.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)

#mysql 地址
labe_iddr = Label(init_window, text="mysql地址")
labe_iddr.pack()
text_iddr_default = StringVar()
text_iddr = Entry(init_window, textvariable = text_iddr_default)
text_iddr_default.set("localhost")
text_iddr.pack()
#账户
labe_user = Label(init_window, text="账户")
labe_user.pack()
text_user_default = StringVar()
text_user = Entry(init_window, textvariable = text_user_default)
text_user_default.set("")
text_user.pack()
#密码
labe_pwd = Label(init_window, text="密码")
labe_pwd.pack()
text_pwd_default = StringVar()
text_pwd = Entry(init_window, textvariable = text_pwd_default)
text_pwd_default.set("")
text_pwd.pack()

labe_users = Label(init_window, text="")
labe_users.pack()
button_sure = Button(init_window, text="确定", width=15, height=2, command=inset_get)
button_sure.pack()

bt_register = Button(init_window, text=u'注册',command=register_info)
bt_register.pack(side=BOTTOM)
init_window.mainloop()