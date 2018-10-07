from urllib import request,error
if __name__ == '__main__':
    url = 'http://www.baidu.com'
# 1.设置代理IP
    proxy = {'http':'101.110.119.60:80'}
# 2.构建proxy_handler
    proxy_handler = request.ProxyHandler(proxy)
#3. 设置opener
    opener = request.build_opener(proxy_handler)
#4. 下载opener
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)

    except error.URLError as e:
        print(e)