import re
s = r'\d+'
p = re.compile(s)

m = p.search("one12two123three2344",10,50)

print(m.group())


m1 = p.findall("one12two123three2344")
print(m1)

s1 = r'[\u4e00-\u9fa5]+'
p1 = re.compile(s1)
m2 = p1.search('hello,你好啊，世界！')
print(m2.group())
