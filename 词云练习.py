from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import jieba
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud


def start_Chrome():
    driver = webdriver.Chrome()
    driver.start_client()
    return driver

def scroll_down():
    html_page = driver.find_element_by_tag_name('html')
    for i in range(8):
        print(i)
        html_page.send_keys(Keys.END)
        time.sleep(3)
def gap_fill(start_time,end_time):
    return f'is_ori=1&key_word=&start_time={start_time}&end_time={end_time}&gid=4295948747861010&is_search=1&is_searchadv=1#_0'

def find_infor():

    sel = 'div.WB_feed_detail.clearfix'
    cards = driver.find_elements_by_css_selector(sel)
    info_list = []

    for card in cards:
        wb_text_sel = 'div.WB_detail > div.WB_text.W_f14'
        wb_text = card.find_element_by_css_selector(wb_text_sel).text

        info_list.append(wb_text)
    return info_list

def find_next():
    next_sel = 'div > a[action-type=feed_list_page]'
    next_page = driver.find_elements_by_css_selector(next_sel)
    if next_page:
        return next_page[0].get_attribute('href')

def login(url):
        driver.get(url)
        time.sleep(40)

def main(full_url):

    driver.get(full_url)
    time.sleep(10)
    scroll_down()
    time.sleep(2)

    next_page = find_next()
    if next_page:
        main(next_page)
    info = find_infor()
    print(info)
    #print('----'*30)
    comments = ''
    for k in range(len(info)):
        comments = comments + (str(info[k])).strip()
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterdata)
    print(cleaned_comments)
    segment = jieba.lcut(cleaned_comments)
    words_df = pd.DataFrame({'segment': segment})
    print(words_df.head())
    # 问题出现在下面，对于stopwords的编码，默认的utf-8没办法进行编码
    stopwords = pd.read_csv("/Users/likaizhe/Desktop/stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],encoding='utf-8')
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    #print(words_df.head())

    # 用numpy进行关键词语统计
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": np.size})
    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
    #print(words_stat.head())

    wordcloud = WordCloud(font_path="simhei.ttf",background_color="white", max_font_size=80)  # 指定字体类型、字体大小和字体颜色
    '''
    for x in words_stat.head(3).values:
        print({x[0]:x[1]})
        print(type(x))
    '''
    # 生成字典形式的格式
    word_frequence = {x[0]: x[1] for x in words_stat.head(200).values}

    # wordcloud直接可以使用字典形式
    wordcloud = wordcloud.fit_words(word_frequence)
    plt.imshow(wordcloud)
    plt.savefig("词云.png",dpi=100)

if __name__ == '__main__':
    start_time = input("请输入开始日期（yyyy-mm-dd）:")
    end_time = input("请输入结束日期（yyyy-mm-dd）:")
    base_url = 'https://www.weibo.com/mygroups?'
    full_url = base_url + gap_fill(start_time,end_time)
    URL = 'https://t.sina.com'
    driver = start_Chrome()
    login(URL)
    main(full_url)