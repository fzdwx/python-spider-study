"""
@author like
@since 2021-01-01 20:59
@email 980650920@qq.com
"""
import requests


class RequestSpider(object):
    def __init__(self, url):
        self.url = url
        headers = {
            # 浏览器的版本
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            # "uid": "like",
            # "password": "1"
        }
        self.resp = requests.post(url, headers=headers, data={"uid": "like",
                                                              "password": "1"})

    def run(self):
        data = self.resp.content.decode("utf-8")
        with open("1.html", "w", encoding='utf-8') as f:
            f.write(data)
        # 1.请求头
        requestHeader = self.resp.request.headers
        print("请求头：", requestHeader)
        # 2.响应头
        respHeaders = self.resp.headers
        print("响应头：", respHeaders)
        # 3.响应状态码
        statusCode = self.resp.status_code
        print(statusCode)
        # 4.响应的cookie
        print(self.resp.cookies)


# url = "https://www.baidu.com/s?wd=" + "你好"
url = "http://47.112.150.204:8888/blog/user/login"
RequestSpider(url).run()
