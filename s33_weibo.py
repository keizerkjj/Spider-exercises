
from selenium import webdriver
import time
#import re


url = 'https://s.weibo.com/weibo/%2523%25E5%25A5%25A5%25E6%2596%25AF%25E5%258D%25A1%2523&Refer=STopic_b'

def start_Chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def find_info():
    path    = 'div > div.total > span:nth-child(2)'
    element = driver.find_elements_by_css_selector(path)
    result = element[0].text.replace("讨论","")
    #element = driver.find_element_by_css_selector(path).text
    #pattern = re.compile(r'\d+.\d+')
    #info    = pattern.findall(element)
    #infor   = info[0]
    return result

while True:
    driver = start_Chrome()
    driver.get(url)
    time.sleep(5)
    info = find_info()

    #if int(float(num)) > 370:
    if info >= "370万":

        print(f'讨论量已经超过370万,并达到：{info}')
        break
    else:
        print('Not happening')

    time.sleep(2000)









