# - - - - - - - - - - - 
# @author like
# @since 2021-02-11 9:09
# @email 980650920@qq.com
#
# 抓取需要登录的页面： http://www.renren.com/352146986/profile
#
import requests

headers = {
    "GET": "/home HTTP/1.1",
    "Host": "www.renren.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "http//www.renren.com/SysHome.do",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "anonymid=kl065w61tdo2gd; depovince=GW; _r01_=1; JSESSIONID=abcINJaZNwBz5h6A0PoEx; taihe_bi_sdk_uid=23b15e9687588b9b278a96820c028853; taihe_bi_sdk_session=a333868201e51afdf90779839cdcd948; ick_login=27405548-1247-48d3-9d4c-f4ad417da8d2; first_login_flag=1; ln_uact=980650920@qq.com; ln_hurl=http//head.xiaonei.com/photos/0/0/men_main.gif; wp_fold=0; jebecookies=e2f6b05f-f3f1-48f1-8416-99107631f41b|||||; _de=241729EC86E98BF0530F97F46C27D779696BF75400CE19CC; p=ec3a656ed3072c501860e4994fcde6d56; t=8c0df9b85a798da1ae862323862ff1e96; societyguester=8c0df9b85a798da1ae862323862ff1e96; id=352146986; xnsid=714cd7e9; loginfrom=syshome",
}
url = "http://www.renren.com/352146986/profile"
print(requests.get(url=url, headers=headers).text)
