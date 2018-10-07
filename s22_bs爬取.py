from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

# 此处，content不需要进行decode解码，因为bs自动会进行解码
content = rsp.read()

soup = BeautifulSoup(content,'lxml')

content = soup.prettify()

print(content)
