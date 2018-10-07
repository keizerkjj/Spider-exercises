from selenium import webdriver
from lxml import etree


def get_web(url):
    driver = webdriver.Chrome()
    driver.get(url)

    print('waitting for .......')
    #time.sleep(10)
    print('waitting done .......')
    driver.set_page_load_timeout(10)

    driver.save_screenshot('douban_reader.png')


    fn = 'douban_reader.html'
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    content_parse(fn)
    driver.quit()

def content_parse(fn):
    html = ''

    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()


    # 生成xml树
    tree = etree.HTML(html)

    #查找book
    books = tree.xpath('//div[@class="item-root"]')

    for book in books:
        book_name = book.xpath(".//div[@class='title']/a")
        book_hrefs = book.xpath(".//div[@class='title']/a/@href")


        print(book_name[0].text)
        print(book_hrefs[0])


        for book_href in book_hrefs:
            driver = webdriver.Chrome()
            driver.get(book_href)
            print('2nd web waitting for .......')
            driver.set_page_load_timeout(10)
            #time.sleep(10)
            print('2nd web waitting done .......')
            driver.save_screenshot('book_href.png')

            book = 'books.html'
            with open(book, 'w', encoding='utf-8') as b:
                b.write(driver.page_source)

            parse_detail(book)
            driver.quit()



def parse_detail(book):
    bookhtml = ''
    with open(book, 'r', encoding='utf-8') as b:
        bookhtml = b.read()
    tree = etree.HTML(bookhtml)

    rating = tree.xpath('//div[@class="rating_wrap clearbox"]/div[@class="rating_self clearfix"]/strong')

    if (len(rating)):
            print(rating[0].text)




if __name__ == '__main__':
    urls = ['https://book.douban.com/subject_search?search_text=python&cat=1001&start={}'.format(str(i)) for i in range(0, 1710, 15)]
    for url in urls:
        print(url)
        get_web(url)
