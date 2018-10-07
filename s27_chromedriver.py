from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = 'http://www.baidu.com'

driver.get(url)
# 访问用浏览器访问url

text = driver.find_element_by_id('wrapper').text
print(text)
print(driver.title)

# 让浏览器自动化的输入关键字并查询
# 因为事先知道了，kw是输入框的ui
driver.find_element_by_id('kw').send_keys(u'UIC')
# 查询的ui是su，找到后，click

driver.find_element_by_id('su').click()

time.sleep(5)
driver.save_screenshot('uic.png')

#下面要自动获取cookies
print(driver.get_cookies())

# 下面，要模拟键盘的操作
driver.find_element_by_id('kw').clear()

driver.find_element_by_id('kw').send_keys(u'MIT')
driver.save_screenshot('MIT.png')
driver.find_element_by_id('su').click()
time.sleep(5)

#最后要清空，输入框里面的字
driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

#最后，让driver 关闭
driver.quit()












