from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

def start_Chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def scroll_down():
    html_page = driver.find_element_by_tag_name('html')
    for i in range(8):
        print(i)
        html_page.send_keys(Keys.END)
        time.sleep(5)
def gap_fill(start_time,end_time):
    return f'is_ori=1&key_word=&start_time={start_time}&end_time={end_time}&gid=4295948747861010&is_search=1&is_searchadv=1#_0'

def find_infor():

    sel = 'div.WB_feed_detail.clearfix'
    cards = driver.find_elements_by_css_selector(sel)
    info_list = []

    for card in cards:
        wb_text_sel = 'div.WB_detail > div.WB_text.W_f14'
        wb_date_sel = 'div.WB_detail > div.WB_from.S_txt2 > a:nth-child(1)'
        wb_text = card.find_element_by_css_selector(wb_text_sel).text
        wb_date = card.find_element_by_css_selector(wb_date_sel).text

        info_list.append([wb_date,wb_text])
    return info_list


def find_next():
    next_sel = 'div > a[action-type=feed_list_page]'
    next_page = driver.find_elements_by_css_selector(next_sel)
    if next_page:
        return next_page[0].get_attribute('href')

def save(info):

    full_path = './' + 'Group_text' + '.csv'
    if os.path.exists(full_path):
        with open(full_path,'a') as f:
            writer = csv.writer(f)
            writer.writerows(info)
    else:
        with open(full_path,'w+') as f:
            writer = csv.writer(f)
            writer.writerows(info)

def find_next():
        next_sel = 'a.page.next'
        next_page = driver.find_elements_by_css_selector(next_sel)
        if next_page:
            return next_page[0].get_attribute('href')

def login(url):
        driver.get(url)
        time.sleep(40)

def run_crawl(full_url):

    driver.get(full_url)
    time.sleep(10)
    scroll_down()
    time.sleep(5)
    info = find_infor()
    save(info)
    next_page = find_next()
    if next_page:
        run_crawl(next_page)

start_time = input("请输入开始日期（yyyy-mm-dd）:")
end_time = input("请输入结束日期（yyyy-mm-dd）:")
base_url = 'https://www.weibo.com/mygroups?'
full_url = base_url + gap_fill(start_time,end_time)
URL = 'https://t.sina.com'
driver = start_Chrome()
login(URL)
run_crawl(full_url)