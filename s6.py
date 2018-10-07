# 构建一个urlerror

from urllib import request,error:
if __name__ == '__main__':
    url = 'http://www.baiiiiiiiiiidu.com'

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except e.URLError as e:
        print(e)



