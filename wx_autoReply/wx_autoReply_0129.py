import itchat
from itchat.content import *
import time
import re
import threading
from time import sleep
import datetime


#自动回复开关
SWITCH_REPLY=False
#延迟回复开关
SWITCH_DELAY=False
#延迟时间
DELAY_TIME=120
#消息前缀开关
SWITCH_PREFIX=True
#消息前缀内容
PREFIX_CONTENT="[自动回复]"
#回复内容字典
REPLY_DICT={}
#延迟回复字典
DELAY_REPLY_DICT={}
ttt="hi,我有事暂未看到消息，稍后回复(•ω•`)"
Time=False
Timestr={}
r_Timestr={}

def fr():
    global q
    friends = itchat.get_friends(update=True)
    # print(friends)
    f=[]
    g=[]
    for i in range(len(friends)):
        f.append(friends[i]['NickName'])
        g.append(i)
    q=dict(zip(g,f))

@itchat.msg_register([TEXT,PICTURE,RECORDING,VIDEO,SHARING],isGroupChat=False)
def auto_reply(msg):
    global SWITCH_REPLY
    global SWITCH_DELAY
    global DELAY_TIME
    global SWITCH_PREFIX
    global PREFIX_CONTENT
    global REPLY_DICT
    global DELAY_REPLY_DICT
    global ttt
    global Time
    global Timestr
    global r_Timestr

    if msg['ToUserName']=='filehelper':
        args=re.compile(' ').split(msg['Text'])
        # print(args)
        # print(msg)
        try:
            if args[0]=='/help':
                reply_content='''
                【功能列表】
                1./help             显示功能列表
                2./switch on        打开自动回复
                3./switch off       关闭自动回复
                4./prefix on        打开消息前缀
                5./prefix off       关闭消息前缀
                6./prefix set [T]   设置前缀内容
                7./delay on         打开延迟回复
                8./delay off        关闭延时回复
                9./delay set [T]    设置延迟时间
                10./dict set [序号] [T] 定制好友回复
                11./dict show [序号]    显示好友回复
                12./friend           显示好友列表
                13./ttt show            显示默认自动回复内容
                14./ttt set [T]      修改默认自动回复内容
                15./j on              定时发送信息开启
                16./j off             定时发送信息关闭
                17./j set [序号]      定时发送信息(指定人)
                18./j del [序号] [时间]
                19./j show  
                20./txt [time] [txt]  编辑发送信息（格式(例如)：/txt 2019-01-29-05:45:00 xxxx）
                '''
            elif args[0]=='/txt':
                Timestr[str(args[1])]=str(args[2])
                reply_content = "【系统消息】内容已设置为：" + str(Timestr)
            elif args[0]=='/j':
                if args[1]=='on':
                    Time=True
                    reply_content="【系统消息】定时发送信息已开启"

                elif args[1]=='off':
                    Time=False
                    reply_content="【系统消息】定时发送信息已关闭"

                elif args[1]=='set':
                    global jj
                    # REPLY_DICT[str(q[int(args[2])])] = {'2019-01-29-05:45:00':'[定时发送]该出门了！','2019-01-29-06:10:00':'[定时发送]上地铁啦！','2019-01-29-07:00:00':'[定时发送]准备上火车啦！'}
                    r_Timestr[str(q[int(args[2])])] = Timestr
                    reply_content = "【系统消息】内容已设置为：" + str(r_Timestr[str(q[int(args[2])])])
                    jj = str(q[int(args[2])])
                elif args[1]=='del':
                    del r_Timestr[str(q[int(args[2])])][args[3]]
                    reply_content = "【系统消息】内容已更新为：" + str(r_Timestr[str(q[int(args[2])])])
                elif args[1]=='show':
                    reply_content = "【系统消息】内容为：" + str(r_Timestr)

            elif args[0]=='/ttt':
                if args[1]=='set':
                    ttt=args[2]
                    reply_content = "【系统消息】默认自动回复内容已设置为："+ttt
                elif args[1]=='show':
                    reply_content = ttt
                else:
                    reply_content="【系统消息】未知指令"

            elif args[0]=='/friend':
                reply_content=str(q)

            elif args[0]=='/switch':
                if args[1]=='on':
                    SWITCH_REPLY=True
                    reply_content="【系统消息】自动回复已开启"

                elif args[1]=='off':
                    SWITCH_REPLY=False
                    reply_content="【系统消息】自动回复已关闭"

                else:
                    reply_content="【系统消息】未知指令"

            elif args[0]=='/prefix':
                if args[1]=='on':
                    SWITCH_PREFIX=True
                    reply_content = "【系统消息】回复前缀已开启"

                elif args[1]=='off':
                    SWITCH_PREFIX=False
                    reply_content="【系统消息】回复前缀已关闭"

                elif args[1]=='set':
                    PREFIX_CONTENT="["+args[2]+"]"
                    reply_content = "【系统消息】回复前缀已设置为："+PREFIX_CONTENT

                else:
                    reply_content = "【系统消息】未知指令"

            elif args[0]=='/delay':
                if args[1]=='on':
                    SWITCH_DELAY=True
                    reply_content="【系统消息】延迟回复已开启"

                elif args[1]=='off':
                    SWITCH_DELAY=False
                    reply_content="【系统消息】延迟回复已关闭"

                elif args[1]=='set':
                    DELAY_TIME=args[2]
                    reply_content="【系统消息】延迟时间被设置为："+DELAY_TIME

                else:
                    reply_content = "【系统消息】未知指令"

            elif args[0]=='/dict':
                if args[1]=='show':
                    if REPLY_DICT.__contains__(q[int(args[2])]):
                        reply_content="【系统消息】好友["+q[int(args[2])]+"]的自动回复为："+REPLY_DICT[q[int(args[2])]]
                    else:
                        reply_content="【系统消息】好友["+q[int(args[2])]+"]的自动回复暂未设置"

                elif args[1]=='set':
                    REPLY_DICT[q[int(args[2])]]=args[3]
                    reply_content="【系统消息】好友["+q[int(args[2])]+"]的自动回复已设置为："+REPLY_DICT[q[int(args[2])]]
                else:
                    reply_content = "【系统消息】未知指令"
            else:
                reply_content = "【系统消息】未知指令"


        except:
            reply_content="【系统消息】系统异常"
            itchat.send(reply_content, toUserName='filehelper')
            raise

        itchat.send(reply_content, toUserName='filehelper')

        # time_ke = '2019-01-29-11:50:00'
        # time_ke1 = '2019-01-29-11:16:00'
        # time_ke2 = '2019-01-29-11:17:00'
        # users = itchat.search_friends(jj)
        # userName = users[0]['UserName']
        # print(userName)
        #
        # while True:
        #     now = datetime.datetime.now()
        #     print(now)
        #     if now.strftime('%Y-%m-%d-%H:%M:%S') == time_ke:
        #         itchat.send(REPLY_DICT[jj]['2019-01-29-05:45:00'], toUserName=userName)
        #         break
        #     elif now.strftime('%Y-%m-%d-%H:%M:%S') == time_ke1:
        #         itchat.send(REPLY_DICT[jj]['2019-01-29-06:10:00'], toUserName=userName)
        #         sleep(3)
        #     elif now.strftime('%Y-%m-%d-%H:%M:%S') == time_ke2:
        #         itchat.send(REPLY_DICT[jj]['2019-01-29-07:00:00'], toUserName=userName)
        #         sleep(3)
        #         break

    else:
        target_friend=itchat.search_friends(userName = msg['FromUserName'])
        # print(target_friend)
        # print
        if target_friend:
            nickName=target_friend['NickName']
            if not REPLY_DICT.__contains__(nickName):
                REPLY_DICT[nickName]=ttt

            if SWITCH_REPLY:
                if SWITCH_DELAY:
                    localtime = time.time()
                    DELAY_REPLY_DICT[nickName]=[localtime,msg['FromUserName']]
                    # print (DELAY_REPLY_DICT)

                if not SWITCH_DELAY:
                    if SWITCH_PREFIX:
                        reply_content = PREFIX_CONTENT + REPLY_DICT[nickName]
                    else:
                        reply_content = REPLY_DICT[nickName]
                    itchat.send(reply_content, toUserName=msg['FromUserName'])
def ti():
    global Time
    # print('q')
    if Time:
        users = itchat.search_friends(jj)
        userName = users[0]['UserName']
        print(userName)
        for i in range(len(Timestr)):
            while True:
                now = datetime.datetime.now()
                print(now)
                if now.strftime('%Y-%m-%d-%H:%M:%S') == str(list(Timestr.keys())[i]):
                    itchat.send(r_Timestr[jj][str(list(Timestr.keys())[i])], toUserName=userName)
                    break
        Timestr.clear()
        del r_Timestr[jj]
        Time = False

    global timer3
    timer3 = threading.Timer(1, ti)
    timer3.start()


def delay_reply():
    global DELAY_REPLY_DICT
    if SWITCH_DELAY:
        while len(DELAY_REPLY_DICT)>0:
            print("开始执行")
            sleep(int(DELAY_TIME))
            localtime = time.time()
            # print (localtime)
            # print (DELAY_REPLY_DICT[item][0])
            # print (int(DELAY_TIME))
            for item in list(DELAY_REPLY_DICT.keys()):
                # print(list(DELAY_REPLY_DICT.keys()))
                if SWITCH_REPLY:
                    reply_content = item + "," + str(int(DELAY_TIME)) + "秒过去了，" + REPLY_DICT[item]
                    itchat.send(reply_content, toUserName=DELAY_REPLY_DICT[item][1])
                    del DELAY_REPLY_DICT[item]
            # print (DELAY_REPLY_DICT)

    global timer1
    timer1=threading.Timer(1,delay_reply)
    timer1.start()

def keep_alive():
    text="保持登录"
    itchat.send(text, toUserName="filehelper")
    global timer2
    timer2 = threading.Timer(3600,keep_alive)
    timer2.start()

if __name__ == '__main__':
    timer1=threading.Timer(1,delay_reply)
    timer1.start()
    timer2=threading.Timer(3600,keep_alive)
    timer2.start()
    timer3=threading.Timer(1,ti)
    timer3.start()
    itchat.auto_login()
    fr()
    itchat.send('输入/help打开功能列表（默认自动回复关/延迟回复关/延迟时间120s）', toUserName='filehelper')
    itchat.run()