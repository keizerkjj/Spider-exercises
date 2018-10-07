# 构建一个HTTPError,HTTPError是URLError的子集


from urllib import request,error
if __name__ == '__main__':
    url = 'http://www.sipo.gov.cn/wwwxiaomi'


    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)

    except error.URLError as e:
        print(e)