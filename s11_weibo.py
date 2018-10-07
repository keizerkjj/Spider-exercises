# 用cookiejar访问微博，通过自动使用cookie

from urllib import request, parse
from http import cookiejar

#  创建filecookiejar的实例
filename = "cookie02.txt"
cookie = cookiejar.MozillaCookieJar(filename)

# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''

    # 此url需要从登录form的action属性中提取
    url = "https://passport.weibo.cn/sso/login"

    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
    'username':'852489177@qq.com',
    'password':'stkjj2112',
    'savestate':'1',
    'r':'http://weibo.cn/',
    'ec':'0',
    'pagerefer':'',
    'entry':'mweibo',
    'wentry':'' ,
    'loginfrom':'',
    'client_id':'',
    'code':'',
    'qq':'',
    'mainpageflag':'1',
    'vid':'fef0ad08eb4bf0b3e04a026f8778705614f877870561',
    'hff':'',
    'hfp':'',
    }
    headers = {
        'Host': 'passport.weibo.cn',
        'Connection': 'keep-alive',
        'Content-Length': '219',
        'Origin': 'https://passport.weibo.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode(),headers=headers)

    # 使用opener发起请求
    rsp = opener.open(req)







    # 保存cookie到文件
    # ignor_discard表示及时cookie将要被丢弃也要保存下来
    # ignore_expire表示如果该文件中cookie即使已经过期，保存
    cookie.save(ignore_discard=True, ignore_expires=True)

if __name__ == '__main__':
    login()