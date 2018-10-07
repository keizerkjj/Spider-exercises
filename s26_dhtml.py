from selenium import webdriver
import time
# 以上是相当于模拟鼠标，进行网页的选取
from selenium.webdriver.common.keys import Keys
#这个是模拟键盘

# 建对应浏览器的实例
driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com')
print("Title:{0}".format(driver.title))
