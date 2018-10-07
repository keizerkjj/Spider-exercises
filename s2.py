import urllib
from urllib import request
import chardet


if __name__ == '__main__':
    url = 'http://stock.eastmoney.com/news/1407,20170807763593890.html'
    #接下来，第一步是要打开这个url网址
    rsp = urllib.request.urlopen(url)
    #第二步是，将这个网站读下来，以html的方式呈现
    html = rsp.read()

    #利用chardet插件，可以检测编码
    cc = chardet.detect(html)
    print(cc)
    # 第三步是，要decode，转码，因为上面的形式是binary二进制
    #括号中的encoding和utf-8是为了避免chardet检测不到值，如果监测不到，则默认utf-8

    html = html.decode(cc.get('encoding','utf-8'))

    print(html)

