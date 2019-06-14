#encoding=utf-8
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
print("~~~现仅支持腾讯视频：电视剧/电影/动漫（其他的频道可能会有问题）~~~")
# urls='https://jx.618g.com/?url='
urls='http://jiexi.92fz.cn/player/vip.php?url='
while True:
    name=input("输入名称：")
    url = "https://v.qq.com/x/search/?q=%s" %name
    res=requests.get(url).text
    tree=BeautifulSoup(res,"html.parser")
    # print(tree)
    new=tree.find_all("div",class_=" result_item result_item_v ")
    # print(len(new))

    ress=tree.find_all("h2",class_="result_title")
    # print(ress)
    ti = tree.find_all("h2", class_="result_title")
    # print(ti)
    txt=[]
    txt_nl=[]
    for xxx in range(len(ti)):
        if 'type' in str(ti[xxx]):
            txt.append(ti[xxx])
    # print(txt)
    for txt_n in range(len(txt)):
        txt_num=txt[txt_n].a['href']
        txt_nl.append(txt_num)
    # print(txt_nl)
    # print(len(txt))
    for i in range(len(txt)):
        tii = txt[i].get_text()
        print(str(i + 1) + ">>>" + tii)
    while True:
        try:
            nummm = int(input("输入对应序号："))
        except ValueError:
            continue
        break
    if txt[nummm-1].find("span",class_="type").string=='电影':
        if 'item' in str(new[nummm-1].find("div",class_="item")):
            # print(str(new[nummm-1].find_all("div",class_="item")))
            idss = new[nummm - 1]['data-id']
            new_id = new[nummm - 1].find("div", class_="result_link_list cf").get('r-props')
            # print(new_id)
            new_ids = re.findall(r"range: '(.*)';", new_id)[0]
            # print(new_ids)
            url_g = 'http://s.video.qq.com/get_playsource?id=%s&plat=2&type=4&data_type=2&video_type=2&range=%s ' % (
            idss, new_ids)
            # print(url_g)
            get = requests.get(url_g).text
            gett = BeautifulSoup(get, "html.parser")
            # print(gett)
            ra = gett.find_all("playurl" or "playUrl")
            # print(ra)
            gett_listtt = []
            for i in range(len(ra)):
                gett_listt = gett.find_all("playurl" or "playUrl")[i].string
                gett_listtt.append(gett_listt)
            # print(gett_listtt)
            # gett_list=gett.videoPlayList.playUrl.string
            # print(gett_list)
            ra_title = gett.find_all("episode_number")
            # print(ra_title)
            gett_title = []
            for i in range(len(ra_title)):
                gett_titl = gett.find_all("episode_number")[i].string
                gett_title.append(gett_titl)
            print(gett_title)
            num_list = dict(zip(gett_title, gett_listtt))
            # print(num_list)
            while True:
                try:
                    try:
                        numm = str(input("输入'-1'退出程序，输入'-2'重新搜索\n输入观看哪一集："))
                        if int(numm) == -1:
                            exit()
                    except ValueError:
                        continue
                    if int(numm) == -2:
                            break
                    urlss = urls + num_list[numm]
                except KeyError:
                    continue
                # print(urlss)
                driver = webdriver.Chrome()
                driver.get(urlss)

            if numm == -2 :
                continue

        else:
            ress_f=tree.find_all("div",class_="_playlist")
            # print(ress_f[1])
            t_f=ress_f[nummm-1].find_all("span",class_="icon_text")
            # print(t_f)
            t_ff=[]
            for i in range(len(t_f)):
                xx=t_f[i].string
                t_ff.append(xx)
            t_ff.remove(None)
            # print(t_ff)
            t_fi = ress_f[nummm-1].find_all("a")
            # print(len(t_fi))
            t_ffi = []
            l_fi = {}
            for index,ii in enumerate(t_ff):
                l_fi.setdefault(str(index),ii)
                print(str(index+1),">>>",ii)
            # print(l_fi)
            for i in range(len(t_fi)):
                xx = t_fi[i]['href']
                t_ffi.append(xx)
            t_ffi.remove('javascript:;')
            # print(t_ffi)
            num_l=dict(zip(t_ff,t_ffi))
            # print(num_l)
            while True:
                try:
                    try:
                        nummss = int(input("输入'-1'退出程序，输入'-2'重新搜索\n输入观看版本序号："))
                        if int(nummss) == -1:
                            exit()
                    except ValueError:
                        continue
                    if int(nummss) == -2:
                        break
                    nummss = l_fi[str(nummss-1)]
                except KeyError:
                    continue
                urlssss = urls + num_l[nummss]
                driver = webdriver.Chrome()
                driver.get(urlssss)
            if nummss == -2:
                continue

    else:
        # a=ress[0]
        # # print(len(ress))
        # # print(a)
        # list=[]
        # b=[]
        # d=[]
        # for i in range(len(ress)):
        #     # z=ress[i]
        #     # print(z)
        #     a=re.sub('( .*?)href=',"",str(ress[i])).replace('<h2',"")
        #     b.append(a)
        #     c=re.sub('target(.*)class="hl"',"",str(b[i]))
        #     d.append(c)
        #     if 'span' in str(d[i]):
        #         q=d[i].replace('</em',"").replace('span class="sub"',"").replace('/span><span class="type"',"").replace('/span></a></h2>',"")
        #         qq=q.replace(" ","")
        #         qqq=qq.replace('>',",").replace("<","").replace('"',"")
        #         qqqq=qqq.split(",")
        #         # print(qqqq)
        #         list.append(qqqq)
        #     else:
        #         f=re.sub('/em(.*)',"",str(d[i]))
        #         ff=f.replace(" ","")
        #         fff=ff.replace('>', ",").replace("<", "").replace('"',"")
        #         ffff=fff.split(',')
        #         # print(ffff)
        #         list.append(ffff)
        # print(list)
        # for ii in range(len(list)):
        #     print("\n")
        #     print(str(ii + 1) + ">>>")
        #     for iii in range(len(list[ii])):
        #         print(list[ii][iii]+"-",end='')
        # print('\n')
        # num=int(input("序号："))
        # get_url=list[num-1][0]
        get_url=txt_nl[nummm-1]
        # print(get_url)
        reee=requests.get(get_url).text
        tre=BeautifulSoup(reee,"html.parser")
        ccc = tre.find_all('script')
        ccccc=[]
        for nu in range(len(ccc)):
            if 'window.__g' in str(ccc[nu]):
                ccccc.append(ccc[nu])
        ddd=ccccc[0].get_text()
        # print(ddd)
        # print(type(ddd))
        dddd=ddd.replace("\n","").replace("\t","").split("=")
        # print(type(dddd))
        ddddd=dddd[1]
        # print(ddddd)
        query=1
        cccc=eval(ddddd)
        # print(cccc)
        # print(type(cccc))
        ids=cccc[1][id]
        # print(ids)
        # print(tre)
        tr=tre.find("div",class_="mod_episode")
        # print(tr)

        if 'item_all' in str(tr):
            aaa=tr.find("span",class_="item item_all")
            bbb=aaa.a['data-range']
            # print(bbb)
            url_g='http://s.video.qq.com/get_playsource?id=%s&plat=2&type=4&data_type=2&video_type=2&range=%s '%(ids,bbb)
            # print(url_g)
            get=requests.get(url_g).text
            gett=BeautifulSoup(get,"html.parser")
            # print(gett)
            ra=gett.find_all("playurl"or"playUrl")
            # print(ra)
            gett_listtt=[]
            for i in range(len(ra)):
                gett_listt=gett.find_all("playurl"or"playUrl")[i].string
                gett_listtt.append(gett_listt)
            # print(gett_listtt)
            # gett_list=gett.videoPlayList.playUrl.string
            # print(gett_list)
            ra_title=gett.find_all("episode_number")
            # print(ra_title)
            gett_title=[]
            for i in range(len(ra_title)):
                gett_titl=gett.find_all("episode_number")[i].string
                gett_title.append(gett_titl)
            print(gett_title)
            num_list=dict(zip(gett_title,gett_listtt))
            # print(num_list)
            while True:
                try:
                    try:
                        numm=str(input("输入'-1'退出程序，输入'-2'重新搜索\n输入观看哪一集："))
                        if int(numm) == -1:
                            exit()
                    except ValueError:
                        continue
                    if int(numm) == -2:
                        break
                    urlss=urls+num_list[numm]
                except KeyError:
                    continue
                # print(urlss)
                driver = webdriver.Chrome()
                driver.get(urlss)
            if numm == -2:
                continue

        else:
            aaaa = tr.find_all("span",class_="item")
            # print(aaaa)
            l=[]
            ll=[]
            for i in range(len(aaaa)):
                aaaaa=aaaa[i].find("a").find('span').string
                l.append(aaaaa)
                aaaaaa=aaaa[i].find("a")['href']
                ll.append(aaaaaa)
                num_lists=dict(zip(l,ll))
            print(l)
            while True:
                try:
                    try:
                        numms = str(input("输入'-1'退出程序，输入'-2'重新搜索\n输入观看哪一集："))
                        if int(numms)==-1:
                            exit()
                    except ValueError:
                        continue
                    if int(numms)==-2:
                        break
                    urlsss = urls + num_lists[numms]
                except KeyError:
                    continue
                # print(urlsss)
                driver = webdriver.Chrome()
                driver.get(urlsss)
            if numms == -2:
                continue