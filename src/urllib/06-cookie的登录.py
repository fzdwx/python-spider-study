"""
@author like
@since 2020-12-31 20:08
@email 980650920@qq.com
     获取个人中心
     1.代码登录，登录成功 cookie（有效）
     2.自动带着cookie，去请求个人中心

    cookiejar 自动保存这个cookie
"""

import urllib.request as request
import urllib.parse as p
from http import cookiejar


def cookieTest():
    # 1.代码登录
    # 1.1 登录的网站
    loginUrl = "https://mnote.tingkl.com/user/signIn"
    # 1.2登录的参数
    loginFormData = {
        "email": "980650920@qq.com",
        "password": "980650920"
    }
    header = {
        # 浏览器的版本
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    # 注意参数要解码
    logStr = p.urlencode(loginFormData).encode("utf-8")

    # 1.3发送登录请求
    cookieJar = cookiejar.CookieJar()
    # 定义有添加cookie功能的处理器
    cookieHandler = request.HTTPCookieProcessor(cookieJar)
    # 根据处理器生成opener
    opener = request.build_opener(cookieHandler)

    # 发送post请求
    login_request = request.Request(loginUrl, headers=header, data=logStr)
    # 如果登录成功，cookjar 自动保存cookie
    opener.open(login_request)

    # 2.访问个人中心
    centerUrl = "https://mnote.tingkl.com/main.html?_from=https%3A%2F%2Fmnote.tingkl.com%2Findex.html"
    centerRequest = request.Request(centerUrl, headers=header)
    resp = opener.open(centerRequest)
    data = resp.read().decode('utf-8')
    with open("test.html", "w") as f:
        f.write(data)
    resp.decode('utf-8')

cookieTest()
