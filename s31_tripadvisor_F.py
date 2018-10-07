from bs4 import BeautifulSoup
import requests
import time
url = 'https://cn.tripadvisor.com/Restaurants-g186411-Leeds_West_Yorkshire_England.html'
urls = ''

def get_page(url,page_num):
    pageList = []
    for i in range(1,59):
        formdata = {
            'data[0][gaa]': 'page',
            'data[0][gal]' : i
        }
    try:
        r = requests.post(url, data =formdata)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('链接成功')
        p = re.compile(r'href="()"')
        tempList = re.findall(p, r.text)
        for each in tempList:
            pageList.append(each)
        print('保存页面成功')
        tempList = []
    except:
        print('链接失败')
    print(pageList)
    return pageList


def get_restaurant(url):
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')

    names    = soup.select('div.title > a[class="property_title"]')

    # hrefs    = soup.select('div.title > a[class="property_title"]')
    ratings  = soup.select('div.popIndexBlock > div')

    for name,rating in zip(names,ratings):

        data = {
            'name': list(name.stripped_strings),
            'rating':list(rating.stripped_strings),
        }
        print(data)


if __name__ == '__main__':
    get_restaurant(url)