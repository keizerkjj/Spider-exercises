def getSalt():
    '''
    salt公式是：  "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
    把他翻译成python代码
    :return:
    '''
    import time, random

    salt = int(time.time()*1000) + random.randint(0,10)

    return salt

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()

    # update需要一共bytes格式的参数
    md5.update(v.encode("utf-8"))

    sign = md5.hexdigest()

    return sign


def getSign(key, salt):

    sign = 'fanyideskweb'+ key + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = getMD5(sign)

    return sign

from urllib import request, parse


def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    ##这个地方，注意需要重新实例化一个salt，因为，salt的值和时间有关系，所以下方的"salt"和"sign"调用的salt的值需要是一样的
    salt = getSalt()

    data = {
        "i": key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt) ,
        "sign": getSign(key, salt),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult": "false"
    }

    print(data)

    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        #"Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1548144101@10.168.8.76;JSESSIONID=aaaTLWzfvp5Hfg9mAhFkw;OUTFOX_SEARCH_USER_ID_NCOO=1999296830.4784973;___rl__test__cookies=1523100789517",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0( X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36 X-Requested-With: XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("henry")


