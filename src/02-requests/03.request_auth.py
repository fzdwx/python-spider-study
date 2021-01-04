"""
@author like
@since 2021-01-04 20:15
@email 980650920@qq.com
"""
import requests

# 发送post请求 需要的參數的json格式
url = "http://47.112.150.204:8888/blog/user/login"
data = {"uid": "like",
        "password": "1"}
postReq = requests.post(url, json=data)
res = postReq.json()
token = res.token("data").token("token")
print(token)



# 发送post请求 auth 内网需要认证
auth = (user, pwd)
requests.post(url, auth=auth);
