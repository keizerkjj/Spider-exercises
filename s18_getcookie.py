import requests


rsp = requests.get("http://fanyi.youdao.com/")
# 如果对方服务器给传送过来cookie信息，则可以通过反馈的cookie属性得到
# 返回一个cookiejar实例
cookiejar = rsp.cookies

# 可以讲cookiejar转换成字典
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print(cookiedict)