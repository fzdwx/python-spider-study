# @author like
# @since 2020-11-30 10:30
# @email 980650920@qq.com

import urllib.request as req

"""
" 自定义添加代理ip功能
" 系统的urlopen并没有添加代理ip的功能所以我们需要自定义这个功能
" ssl 安全套接层  http:80-https:443
" urlopen 为什么可以请求数据 handler处理器
" 自己的opener请求数据
"""


def handlerOpener():
    url = "http://47.112.150.204/"

    # 创建自己的处理器
    handler = req.HTTPHandler
    # 创建自己的opener
    opener = req.build_opener(handler)
    # open
    response = opener.open(url)
    data = response.read().decode("utf8")

    print(response)
    print(data)


if __name__ == '__main__':
    handlerOpener()
