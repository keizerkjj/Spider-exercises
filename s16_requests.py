
import requests

url = 'https://www.baidu.com/s?'

kw = {
    "wd":"合肥天气"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

rsp = requests.get(url,params= kw,headers=headers)

print(rsp.status_code)