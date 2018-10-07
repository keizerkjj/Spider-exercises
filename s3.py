from urllib import request,parse


if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'

# 这里的重点是利用parse将文字参数进行编码，使能够拼接成被电脑识别的url

    wd = input("请输入关键字：")
    dic = {"wd":wd}
    dic = parse.urlencode(dic)

    fullurl = url + dic


    rsp = request.urlopen(fullurl)

    html = rsp.read()


    html = html.decode()

    print(type(dic))

    print(html)