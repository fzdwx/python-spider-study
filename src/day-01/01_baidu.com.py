# - - - - - - - - - - - 
# @author like
# @since 2021-02-03 8:47
# @email 980650920@qq.com
#
from urllib import request
from urllib import parse

word = input("请输入你要搜索的内容：")

url = "http://www.baidu.com/s?"
headers = {'user-agent': 'mozilla/5.0'}
queryStr = parse.urlencode({'wd': word})
url = url + queryStr

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

fileName = "{}.html".format(word)
with open(fileName, 'w', encoding='utf-8') as f:
    f.write(html)
print('保存成功:{}'.format(fileName))

"""
url 拼接
1.字符串相加
url = "http://www.baidu.com/s?" +urlencode({'wd': '北京时间'})
2.字符串格式化
url = "http://www.baidu.com/s?%s"%urlencode({'wd': '北京时间'})
3.format()
url = "http://www.baidu.com/s?{}".format(urlencode({'wd': '北京时间'}))
"""
