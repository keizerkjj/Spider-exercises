# open Chrome with Selenium -> input -> go to target web -> scroll down -> find info -> save()
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
        time.sleep(2)

def find_infor():
    sel = 'div.WB_feed_detail'

    cards = driver.find_elements_by_css_selector(sel)
    info_list = []
    for card in cards:
        wb_text_sel = 'div.WB_text.W_f14'
        wb_date_sel = 'div.WB_from.S_txt2 > a.S_txt2:nth-child(1)'
        wb_text = card.find_element_by_css_selector(wb_text_sel).text
        wb_date = card.find_element_by_css_selector(wb_date_sel).text

        info_list.append([wb_date,wb_text])
    return info_list

def find_three():
    text_list_2 = []
    sel_2 = 'div.WB_feed_handle'
    three = driver.find_elements_by_css_selector(sel_2)
    for one in three:
        forward_sel = 'div.WB_feed_handle > div > ul > li:nth-child(2) > a > span > span > span > em:nth-child(2)'
        comment_sel = 'span[node-type=comment_btn_text]>span>em:last-child'
        like_sel = 'span[node-type=like_status]>em:last-child'
        forward = one.find_element_by_css_selector(forward_sel).text
        comment = one.find_element_by_css_selector(comment_sel).text
        like = one.find_element_by_css_selector(like_sel).text
        text_list_2.append([forward, comment, like])
    return text_list_2
def find_next():
    next_sel = 'a.page.next'
    next_page = driver.find_elements_by_css_selector(next_sel)
    if next_page:
        return next_page[0].get_attribute('href')

def save(info):

    full_path = './' + 'weibo_text' + '.csv'
    if os.path.exists(full_path):
        with open(full_path,'a') as f:
            writer = csv.writer(f)
            writer.writerows(info)
    else:
        with open(full_path,'w+') as f:
            writer = csv.writer(f)
            writer.writerows(info)
def save_2(three):
    full_path = './' + 'weibo_three' + '.csv'
    if os.path.exists(full_path):
        with open(full_path,'a') as f:
            writer = csv.writer(f)
            writer.writerows(three)
    else:
        with open(full_path,'w+') as f:
            writer = csv.writer(f)
            writer.writerows(three)

def run_crawl(base_url):

    driver.get(base_url)
    time.sleep(10)
    scroll_down()
    time.sleep(5)
    info = find_infor()
    three = find_three()
    save(info)
    save_2(three)
    driver.quit()

    #next_page = find_next()
    #if next_page:
        #run_crawl()

base_url = 'https://www.weibo.com/u/2075811071'
driver = start_Chrome()
input()
run_crawl(base_url)

