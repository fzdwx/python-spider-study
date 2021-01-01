# @author like
# @since 2020-11-28 16:00
# @email 980650920@qq.com

# 随机使用user agent
import urllib.request as req
import random


def load():
    # 请求的url地址
    url = "http://www.baidu.com"
    # userAgent的列表
    userAgentList = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET "
        "CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E) "
    ]

    # 随机选择一个
    randomUserAgent = random.choice(userAgentList)

    # 请求头
    header = {
        "user-agent": randomUserAgent
    }

    # 生成请求
    request = req.Request(url, headers=header)
    # 请求网络数据
    response = req.urlopen(request)
    print(request.get_header("User-agent"))


if __name__ == '__main__':
    load()
