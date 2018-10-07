from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


def get_total(url):



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








