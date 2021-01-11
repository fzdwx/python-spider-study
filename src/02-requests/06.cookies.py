# - - - - - - - - - - - 
# @author like
# @since 2021-01-04 20:46
# @email 980650920@qq.com
#
import requests

# 发送post请求 需要的參數的json格式
header = {
    # 浏览器的版本
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.66 Safari/537.36 ",
}

url = "http://47.112.150.204:8888/blog/user/login"
data = {"uid": "like",
        "password": "1"}
postReq = requests.post(url, json=data)
res = postReq.json()
token = res.get("data").get("token")
print(token)
infoUrl = "http://47.112.150.204/user/info"
# 写法一
# sessions = requests.session()  # 制动保存session
# infoReq = sessions.get(infoUrl, headers=header)
# data = infoReq.content.decode()
# 写法二
cookie = {"blog-token": token}

infoReq = requests.get(infoUrl, cookies=cookie, headers=header)
data = infoReq.content.decode()

print(infoReq.cookies)

with open("info.html", "w", encoding="utf-8") as f:
    f.write(data)
