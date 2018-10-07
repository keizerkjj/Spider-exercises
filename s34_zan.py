from selenium import webdriver
import time

def start_Chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def find_like():
    # 定位为点赞的button的位置
    sel = 'span.line.S_line1 > span >em.ficon_praised'

    # 关于sel路径的获取，建议用firefox打开审查，在元素界面，运用左上角的选择器定位目标按钮的路径。然后在html中输入路径以配对


    elements = driver.find_elements_by_css_selector(sel)
    return elements

def add_like():
    pass




url = 'https://t.sina.com'
fri_url = 'https://www.weibo.com/mygroups?gid=3579361053670736&wvr=6&leftnav=1&isspecialgroup=1'
while True:
    driver = start_Chrome()
    driver.get(url)
    time.sleep(40)
    driver.get(fri_url)
    time.sleep(6)
    likes = find_like()
    for like in likes:
        like.click()
        time.sleep(3)
        print("Done!")
    #c = driver.get_cookie()
    #driver.add_cookie()
    time.sleep(300)




