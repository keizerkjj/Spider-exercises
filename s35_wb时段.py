from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

def start_Chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def pin(st,et):
    return f'?is_ori=1&key_word=&start_time={st}&end_time={et}&is_search=1&is_searchadv=1#_0'

def scroll_down():
    html_page = driver.find_element_by_tag_name('html')
    for i in range(15):
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
        forward_sel = 'span[node-type=forward_btn_text]>span>em:last-child'
        comment_sel = 'span[node-type=comment_btn_text]>span>em:last-child'
        like_sel = 'span[node-type=like_status]>em:last-child'
        wb_text = card.find_element_by_css_selector(wb_text_sel).text
        wb_date = card.find_element_by_css_selector(wb_date_sel).text
        forward = card.find_element_by_css_selector(forward_sel).text
        comment = card.find_element_by_css_selector(comment_sel).text
        like = card.find_element_by_css_selector(like_sel).text
        info_list.append([wb_date,wb_text,forward,comment,like])
    return info_list

base_url = 'https://www.weibo.com/u/2075811071'
driver = start_Chrome()
input()
driver.get(base_url+pin('2018-08-01','2018-10-09'))
time.sleep(10)
scroll_down()
time.sleep(5)
info = find_infor()
print(info)


