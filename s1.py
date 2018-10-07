from urllib import request
if __name__ == '__main__':

    url = "https://jobs.zhaopin.com/244636025258676.htm"
    rsp =  request.urlopen(url)
    html = rsp.read()
    print(type(html))

    # 如果想把bytes转化成人能读得懂的字符，需要用decode解码

    html = html.decode()
    print(html)

# 出现一个问题，decode有时候没办法自动解析某些网页，需要在()内输入一些解码符
# 这个时候，需要用到chardet自动检测
