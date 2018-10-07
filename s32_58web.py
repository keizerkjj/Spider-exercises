from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


def get_total(url):
'''
    headers = {
        'authority': 'bj.58.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'referer': 'https://bj.58.com/pbdn/0/pn4/?PGTID=0d305a36-0000-15b3-00ea-4c41d523c76b&ClickID=1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'f=n; webps=A; myfeet_tooltip=end; userid360_xml=7B8156FAFFD27A5E9F70ADB16D6CA323; time_create=1540592647892; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; sessionid=72cec6a5-d053-4ca1-85d8-41af6defd0be; id58=c5/njVusBvmwSoeDBodiAg==; 58tj_uuid=aa4786fc-4c1e-4d75-9b8f-c9dbe71d075f; _ga=GA1.2.1386308993.1538000636; _gid=GA1.2.102104077.1538000636; gr_user_id=ef8a7ec1-2e0a-4c44-94d2-5d2502798e2a; Hm_lvt_3013163ef40dcfa5b06ea83e8a1a797f=1538000636; f=n; als=0; gr_session_id_98e5a48d736e5e14=e174bfa1-075a-427e-b23e-218a70f76de1; gr_session_id_98e5a48d736e5e14_e174bfa1-075a-427e-b23e-218a70f76de1=true; new_uv=2; utm_source=; spm=; init_refer=https%253A%252F%252Fbj.58.com%252Fpbdn%252F0%252F; new_session=0; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1538041182; Hm_lpvt_e2d6b2d0ec536275bb1e37b421085803=1538041182; wmda_uuid=1f5888e18e1324df66c4d683d8b790a5; wmda_new_uuid=1; wmda_session_id_1409632296065=1538041182717-4c3edefe-f943-0721; wmda_visited_projects=%3B1409632296065; final_history=35589040514488; ppStore_fingerprint=9E702A60FDBAAC2870C454541A9604A1BA3E1EABEFB6198D%EF%BC%BF1538041188358; xzfzqtoken=bP%2BLMsQ8ttt%2FbLiHneshVDCCSAuIFS744LHdN9dUccwcDwPWKyGixSio%2F8zLa1%2Ftin35brBb%2F%2FeSODvMgkQULA%3D%3D; xxzl_deviceid=gWi%2Btqsxp74laaVG2xezuh%2FH%2FO2wBrANC%2BROaBPb2o0zW10gy2UAqU6Wz%2Fku3hIc; Hm_lpvt_3013163ef40dcfa5b06ea83e8a1a797f=1538041342; GA_GTID=0d305a36-0000-1545-026f-87239bcd9195',
    }

    params = (
        ('PGTID', '0d305a36-0000-17bb-2da5-41a86419c258'),
        ('ClickID', '1'),
    )
'''
# 可以不需要伪装 headers 和 params，因为58的反爬虫是-相应时间，所以只需要sleep

    web_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text,'lxml')
    hrefs = soup.select('a.t')

    print(type(hrefs))
    href_list = []

    for href in hrefs:
        link = href.get('href')
        if 'pingbandiannao' in link:
            href_list.append(link)

    for href in href_list:
            spider(href)

def spider(href):
    driver = webdriver.Chrome()
    driver.get(href)
    driver.set_page_load_timeout(5)
'''
    这一步是将driver爬取的页面打印到文件中，查看文件中是否拥有我们要的ajax数据
    fn = 'product.html'
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'lxml')
'''
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    title_list = soup.select('h1.detail-title__name')
    title = title_list[0].text.strip()

    price_list = soup.select('span.infocard__container__item__main__text--price')
    price = price_list[0].text.strip()

    area_list = soup.select('div.infocard__container__item__main > a')
    area = area_list[0].text.strip()

    typename_list= soup.select('div.nav > a')
    typename= typename_list[-1].text

    view_list = soup.select('span.detail-title__info__totalcount')
    view = view_list[0].text.strip()
    data = {
        'title': title,
        'price': price,
        'area': area,
        'typename':typename,
        'view': view

    }
    print(data)


if __name__ == '__main__':
    urls = ['https://bj.58.com/pbdn/0/pn{}/'.format(str(i)) for i in range(1, 4, 1)]
    for url in urls:
        get_total(url)








