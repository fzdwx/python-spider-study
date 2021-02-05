# - - - - - - - - - - - 
# @author like
# @since 2021-02-03 11:38
# @email 980650920@qq.com
#
from urllib import request, parse
import time
import random
import re
import csv

"""
      <div class="board-item-content">
              <div class="movie-item-info">
              <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a></p>
              <p class="star">
                主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
              </p>
              <p class="releasetime">上映时间：1994-09-10(加拿大)</p>    </div>
             <div class="movie-item-number score-num">
             <p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>
"""
fileName = "猫眼-Top100数据.csv"  # 保存文件的名字

url = "https://maoyan.com/board/4?offset={}"  # 请求的url

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

# 正则表达式
p = re.compile(
    '.*?title="(.*?)".*?</a></p>\D*<p class="star">(.*?\D*?)</p>\D*?<p class="releasetime">(.*?)</p>'
)
# p = re.compile('<div class="movie-item-info">.*?title=" (.*?)"*?class="star">(.*?)</p>*?releasetime">(.*?)</p>')
filmList = []
with open(fileName, 'a', encoding="utf-8") as  f:
    w = csv.writer(f)
    for no in range(1, 11):
        offset = (no - 1) * 10
        finUrl = url.format(offset)
        print(finUrl)

        req = request.Request(finUrl, headers=header)
        res = request.urlopen(req)

        html = res.read().decode('utf-8')

        movieList = p.findall(html)
        for info in movieList:
            data = (info[0].strip(), info[1].strip(), info[2].strip())
            filmList.append(data)
    # w.writerows(filmList)
print(filmList)
    # time.sleep(random.randint(0, 2))  # 随机休眠
