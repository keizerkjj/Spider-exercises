from urllib import request
from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content,'lxml')

#标签查找
rst = soup.select("title")
print(rst[0])

#属性查找
metas = soup.select("meta[content='always']")
print(metas)

