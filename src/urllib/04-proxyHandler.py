"""
@author like
@since 2020-11-30 10:55
@email 980650920@qq.com
"""
import urllib.request as req

def createProxyHandler():
    url = "https://zhuanlan.zhihu.com/p/275976896"

    # 1.添加代理
    proxy = {
        # 免费的写法
        "http": "123.55.101.62:9999",

        # 付费代理
        # "http":"likelove":123@47.112.150.204
    }
    # 2.代理处理器
    proxyHandler = req.ProxyHandler(proxy)
    # 3.创建自己的opener
    proxyOpener = req.build_opener(proxyHandler)
    # 4.open
    resp = proxyOpener.open(url)
    data = resp.read().decode('utf-8')
    print(data)



"""
 随机选取代理ip
"""


def randomProxyHandler():
    url = "https://zhuanlan.zhihu.com/p/275976896"

    proxyList = [
        {"http": "123.55.101.62:9999"},
        {"http": "117.69.168.203:9999"},
        {"http": "60.169.133.186:9999"},
        {"http": "182.92.113.148:8118"},
        {"http": "123.123.123.123:8118"},
    ]
    for proxy in proxyList:
        # 2.代理处理器
        proxyHandler = req.ProxyHandler(proxy)
        # 3.创建自己的opener
        proxyOpener = req.build_opener(proxyHandler)
        # 4.open
        try:
            resp = proxyOpener.open(url)
            data = resp.read().decode('utf-8')
            print("success")
        except  Exception as e:
            print("失败:", proxy)


if __name__ == '__main__':
    randomProxyHandler()
