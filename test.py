from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
url = 'https://bj.58.com/pingbandiannao/35611156906824x.shtml?psid=191918625201616552436178152&entinfo=35611156906824_p&slot=-1&iuType=p_1&PGTID=0d305a36-0000-1b1a-7648-89c6596c0070&ClickID=1'
driver = webdriver.Chrome()
driver.get(url)
driver.set_page_load_timeout(5)
driver.save_screenshot('product.png')
fn = 'product.html'
with open(fn, 'w', encoding='utf-8') as f:
    f.write(driver.page_source)
with open(fn, 'r', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html,'lxml')


view_list = soup.select('span.detail-title__info__totalcount')
print(view_list)
