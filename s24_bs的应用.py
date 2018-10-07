from urllib import request
from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content,'lxml')
# 上述，将内容放入soup汤里面，以lxml的方式驱动

# 接下来可以通过，索引，来调取soup里面的东西

print(soup. name)
'''
这种方法是，遍历提取数据
for node in soup.head.contents:
    if node.name == 'meta':
        print(node)
    if node.name == 'title':
        print(node.string)
'''
#第二种方法是，搜索数据，先是构建所有目标tag的实例
'''
tags = soup.find_all(name='meta')
for tag in tags:
    print(tag)
'''

#还可以搜索正则
tags_ = soup.find_all(re.compile('^me'),content='always')
for tag in tags_:
    print(tag)





