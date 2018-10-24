from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time
import sys



class Spider:
    def __init__(self,index_url,target_url,page_range):
        self.index_url = index_url
        self.target_url = target_url
        self.page_range = page_range + 1
        self.raw_html = []
        self.boot()
    def boot(self):
        self.driver = Chrome()
        self.driver.start_client()
        self.check_cookie()
    def check_cookie(self):
        from xcookie import cookie_list
        if cookie_list:
            self.driver.get(self.index_url)
            time.sleep(8)
            self.driver.delete_all_cookies()
            print('clear')
            for c in cookie_list:
                self.driver.add_cookie(c)
            print('Done')
        else:
            print('please insert cookie!')
            sys.exit()

    def crawl(self):
        for p in range(1,self.page_range):
            full_url = f'{self.target_url}{p}'
            self.driver.get(full_url)
            print(full_url)
            time.sleep(5)
            self.raw_html.append(self.driver.page_source)


class Parser:
    def __init__(self,raw_html):
        self.raw_html = raw_html
        self.info = []
    def parse(self):
        for html in self.raw_html:
            soup = BeautifulSoup(html, 'html.parser')
            text_sel = 'div.WB_detail'
            text = soup.select(text_sel)
            for text_detail in text:
                content = text_detail.get_text()
                clean_text = content.replace(' ','').replace('\n','')
                self.info.append(clean_text)
        print(self.info)

    def save_to_csv(self):
        with open('collection.txt','a+') as f:
            for i in self.info:
                f.write(i)
                f.write('\n')
                f.write('-'*50)
                f.write('\n')

s = Spider(index_url='https://www.weibo.com/',target_url='https://www.weibo.com/fav?page=',page_range=2)
s.crawl()
p = Parser(s.raw_html)
p.parse()
p.save_to_csv()






















