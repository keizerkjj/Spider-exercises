from urllib import request,error
if __name__ == '__main__':
    url= 'http://www.baidu.com'


    try:
        #第一种方法：模拟一个headers
        '''
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0'
        req = request.Request(url,headers=headers)
        '''
        # 第二种方法: 用req.add_header()的方法

        req = request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0')
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)

    except error.URLError as e:
        print(e)

    except Exception as e:
        print(e)
    print("Done!")