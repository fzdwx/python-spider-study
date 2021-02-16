# - - - - - - - - - - - 
# @author like
# @since 2021-02-16 9:17
# @email 980650920@qq.com
#
from  selenium import webdriver

op = webdriver.ChromeOptions()
op.add_argument('--headless')

chrome = webdriver.Chrome(options=op)
chrome.get('http://www.baidu.com')
chrome.save_screenshot('baidu.png')