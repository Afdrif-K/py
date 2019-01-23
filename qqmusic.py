#encoding=utf-8
import requests
import json
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36','Cookie':'pgv_info=ssid=s8864928176; pgv_pvid=7028255569; pac_uid=0_36cc29c99adaf; _qpsvr_localtk=0.8822797579589687; pgv_pvi=9799422976; pgv_si=s4191964160; pt2gguin=o0461301365; uin=o0461301365; RK=yMYwxidkNy; ptcz=1363f9d617b8668a85147a26d14f5183f75c0a1663c73010ad20a8cb0798e06f; ptisp=cm; skey=@fGtcNYEpj; yqq_stat=0; ts_uid=2506187689; qqmusic_fromtag=66; yq_index=0; yq_playschange=0; yq_playdata=; player_exist=1; yplayer_open=1'}
name=input("输入歌名:")
url="https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61356799038869969&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}&g_tk=1982918511&loginUin=461301365&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0".format(name)
res=requests.get(url).text
js=json.loads(res)
lt=js['data']['song']['list']
songs=[]
names=[]
for num in range(len(lt)):
    lt2 = js['data']['song']['list'][num]
    print(str(num+1)+ ">>>" + str(lt2['name'])+ "---" + str(lt2['singer'][0]['name']))
    songs.append((num+1,lt2['mid']))
    names.append(lt2['name'])
# print(songs)
# print(names)
get_mid=int(input("输入序号："))
names=names[get_mid-1]
mid=songs[get_mid-1][1]
# print(mid)
get_song='''https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey060478060368589937&g_tk=1982918511&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"7028255569","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7028255569","songmid":["%s"],"songtype":[0],"uin":"","loginflag":1,"platform":"20"}},"comm":{"format":"json","ct":20,"cv":0}} ''' %mid
ress=requests.get(get_song).text
jss=json.loads(ress)
ltt=jss['req_0']['data']['midurlinfo'][0]['purl']
# print(ltt)
download_url='http://dl.stream.qqmusic.qq.com/'+ltt
# print(type(download_url))
response=requests.get(download_url,headers=header).content
# print(response)
with open(names + ".m4a", "wb") as file:
    file.write(response)
print("\n######嘿嘿嘿，下载完成啦！######\n\n\n")