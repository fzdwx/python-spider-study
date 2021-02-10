# - - - - - - - - - - - 
# @author like
# @since 2021-02-10 9:42
# @email 980650920@qq.com
#
"""
i: hello
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 16129207300886
sign: dea78aef134ec1e0216311a927a79eca
lts: 1612920730088
bv: 6a1ac4a5cc37a3de2c535a36eda9e149
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
"""
import time
import random
from hashlib import md5
import requests
from src.randomAgent import *


def getSaltAndSignAndTs(word):
    client = "fanyideskweb"

    ts = str(int(time.time() * 1000))

    salt = ts + str(random.randint(0, 9))

    s = md5()
    sign = client + word + salt + "n%A-rKafb[Gy?;N5@Tj"
    s.update(sign.encode())
    sign = s.hexdigest()

    return salt, ts, sign


def attack(word):
    salt, ts, sign = getSaltAndSignAndTs(word)
    # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "239",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-485193504@10.169.0.83; JSESSIONID=aaaNUy64FIp5FdN28JjEx; OUTFOX_SEARCH_USER_ID_NCOO=915595934.2597066; ___rl__test__cookies=1612940839212",
        "Host": "fanyi.youdao.com",
        "Origin": "http//fanyi.youdao.com",
        "Referer": "http//fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    fromData = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "lts": "1612920730088",
        "bv": "6a1ac4a5cc37a3de2c535a36eda9e149",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    return requests.post(url=url, data=fromData, headers=headers).json()


if __name__ == '__main__':
    word = input("要翻译的单词:")
    res = attack(word)
    print(res)
