import requests
import pytest

def test_115sign():
    #定义请求头
    headers = {
        "Host":"web.api.115.com",
        "Content-Length":"0",
        "Pragma":"no-cache",
        "Cache-Control":"no-cache",
        "Accept":"*/*",
        "Origin":"http://web.api.115.com",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; MI 4W Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 115disk/7.3.0.20171018.1931",
        "Referer":"http://web.api.115.com/bridge_2.0.html?namespace=FS.DataSrv&api=UDataAPI&_t=v5",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,en-US;q=0.8"
        #"Cookie":"ssov_4283298=1_4283298_8bd19e7e43e864501b26141f3097cd39; OOFA=UID=4283298_F1_1508503643; UID=4283298_F1_1508503643; CID=7de5c9f8bfccd67eff53b31e8ebc4bed;115_lang=zh"
    }

    #定义url
    url = "http://web.api.115.com/user/sign"

    #定义cookie
    cookies = "ssov_4283298=1_4283298_8bd19e7e43e864501b26141f3097cd39; OOFA=UID=4283298_F1_1508503643; UID=4283298_F1_1508503643; CID=7de5c9f8bfccd67eff53b31e8ebc4bed; SEID=e16995efaaaf89428a04dd626b295e7eaad54a815cdb59c485f91bb596a346476480e0313190d691b44dbd41461d1222750d8b529363d9930e73c7f5; 115_lang=zh;"
    jar = requests.cookies.RequestsCookieJar()
    for cookie in cookies.split("；"):
        key,value = cookie.split("=",1)
        jar.set(key,value)

    #请求签到接口
    r = requests.post(url=url,headers=headers,cookies=jar)

    #输出接口返回的json内容
    print(r.json())
    
    #根据接口返回的state状态判断是否签到成功
    s = r.json()
    if s["state"] == True:
        print("签到成功")
    else:
        print("签到失败")
            



