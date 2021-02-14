# - - - - - - - - - - - 
# @author like
# @since 2021-02-14 12:32
# @email 980650920@qq.com
#
from selenium import webdriver
from selenium import common
import time

# 打开浏览器
chrome = webdriver.Chrome()
# 输入百度url 跳转页面
chrome.get('http://www.baidu.com')
chrome.find_element_by_id('kw').send_keys('药水哥')
chrome.find_element_by_id('su').click()
print(chrome.page_source)
# 关闭
# chrome.quit()
