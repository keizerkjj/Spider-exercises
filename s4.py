# 利用parse 模拟urlopen里的 post

from urllib import request,parse
import json
#json的作用是，使能够打开json的格式

# 通过用f12观察，百度翻译的"网络"，可以可以找到baseurl是一个以sug结尾的url

baseurl = 'https://fanyi.baidu.com/sug'

# 和get一样，需要有一个data库，其实就是一个字典
data = {
    'kw' : '女孩'
}

data = parse.urlencode(data).encode("utf-8")

rsp = request.urlopen(baseurl,data=data)

json_data = rsp.read().decode("utf-8")

print(type(json_data))


print(json_data)
#到这一步，我们得到了json返回数据，但是在显示器，依然看不到我们要的显示效果

#所以，接下来我们要把json_data转化成dict,我们能看得懂的形式

json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'],'---',item['v'])