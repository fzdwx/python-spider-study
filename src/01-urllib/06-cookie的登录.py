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
    loginUrl = "https://clogin.lianjia.com/authentication/authenticate"
    # 1.2登录的参数
    loginFormData = {
        "credential": {
            "encodeVersion": "2",
            "username": "13789983260",
            "password": "Lk980650920"
        },
        "loginTicketId": "yclz6njR3xSNMvEHM1jNEWC6zcot3SKa",
        "mainAuthMethodName": "username-password",
        "service": "https://ajax.api.lianjia.com/login/login/getuserinfo",
        "srcId": "eyJ0Ijoie1wiZGF0YVwiOlwiNzQ2MTFmZmIyZWYzMTViOTBhYzkxZWUyMDc2NzA3ZDFkMGQ4NzE4YWM5M2VlNDJjOTA4YWVmOTk0YjJlYzdhYTQxNWEzYzViMmI1MTFhZDc1ZWViNGI5NTU5OThlYjcyMzExNzVjYTg4M2E2Y2YyY2YwYTFlMGJiNGQ2MDkwZjljZTFmYzg1ZDFlNGU4ZTE0NWVmNzgyYWE2ZTliYzk4OTZlM2U1NTQzNjJlYmY2ZmIxNGQxMTk0YTY3MTYxMTg2NjRjYjVjOWU4MGE5M2FmZjU5OWUxZjdlMTMyMzdkMjk1MDA0ZmE2YjRmNmRiNDhlMDQ4MjNhNDgzZmMxOGYyNmRlOGUyYjM5YWI4ZTUyNDc0ZWNlYzYxMzFiMGNlZjRmZDc3NzhhNDA4MTVjMzhmNGE2MjU1ODhjNGNkYzdkN2RmYzY1ZWM2NWYxNmQ0ZjM2NmQ1MTRjYmI3MjllYjI3NlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIxN2I5ZjBhN1wifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tLz91dG1fc291cmNlPWJhaWR1JnV0bV9tZWRpdW09cGluemh1YW4mdXRtX3Rlcm09Ymlhb3RpJnV0bV9jb250ZW50PWJpYW90aW1pYW9zaHUmdXRtX2NhbXBhaWduPXd5YmVpamluZyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9",
        "ticketMaxAge": "604800",
        "version": "2.0",
        "accountSystem": "customer",
        "context": "{}"
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
    login_request = request.Request(loginUrl, headers=header, data=logStr, method="post")
    # 如果登录成功，cookjar 自动保存cookie
    opener.open(login_request)

    # 2.访问个人中心
    centerUrl = "https://user.lianjia.com/"
    centerRequest = request.Request(centerUrl, headers=header)
    resp = opener.open(centerRequest)
    data = resp.read().decode('utf-8')
    with open("test.html", "w") as f:
        f.write(data)
    resp.decode('utf-8')


cookieTest()
