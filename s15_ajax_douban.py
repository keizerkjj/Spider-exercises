
from urllib import request, parse
import json
#对于ajax，通常得到的数据是json格式


url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20'

rsp = request.urlopen(url)
data = rsp.read().decode()
data = json.loads(data)

print(data)



