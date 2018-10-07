from urllib import request
import ssl
#利用ssl，用非认证上下文认证代替认证上下文认证，从而能进入没有安全证书的网站


ssl._create_default_https_context = ssl._create_unverified_context


url = "https://www.12306.cn/mormhweb/"
rsp = request.urlopen(url)
html = rsp.read().decode()
print(html)
