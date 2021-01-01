# @author like
# @since 2020-11-28 14:48
# @email 980650920@qq.com

# 测试请求头和响应头
import urllib.request as req


def loadBaidu():
    url = "https://www.baidu.com"
    # 自定义请求头
    header = {
        # 浏览器的版本
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.66 Safari/537.36 ",
        "name": "like"
    }

    # 创建请求对象
    request = req.Request(url, headers=header)
    # 请求网络数据
    response = req.urlopen(request)

    # 输出请求头和响应头
    request_headers = request.headers  # 对应我们传入的请求头信息
    response_headers = response.headers
    print("请求头：", request_headers)
    print("响应头:", response_headers)
    # 获取指定的请求头的信息
    name = request.get_header("Name")
    print(name)

    # 网页数据
    data = response.read().decode('utf-8')
    # 写入文件
    with open("baidu.html", "w")as f:
        f.write(data)

    full_url = request.get_full_url()
    print("完成的url", full_url)


if __name__ == '__main__':
    loadBaidu()
