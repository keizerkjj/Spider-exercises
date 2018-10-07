import requests
from urllib import parse

#相比之前的urllib，requests的用法相似，但仍然存在不同
## 最主要的区别是，data和headers里面要求dict格式，而不需要非常麻烦地将其转码


baseurl = 'https://fanyi.baidu.com/sug'

data = {
    'kw' : '女孩'
}


#data = parse.urlencode(data).encode("utf-8") 不需要将data编码成bytes


# headers 的dict里面，不能是数字，而应该是字符
headers = {
    'Content_Length': str(len(data))
}
#构造request实例
# 将所有的请求，全部封装在request里面

#req = request.Request(url=baseurl,data=data,headers=headers)

#rsp = request.urlopen(req)

rsp = requests.post(baseurl,data=data,headers=headers)

#json_data = rsp.read().decode("utf-8")

print(rsp.text)
print(rsp.json())
