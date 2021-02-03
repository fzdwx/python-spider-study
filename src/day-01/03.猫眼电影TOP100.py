# - - - - - - - - - - - 
# @author like
# @since 2021-02-03 11:38
# @email 980650920@qq.com
#
from urllib import request, parse
import time
import random
import re

"""
                    <dd>              
                        <i class="board-index board-index-1">1</i>
                        <a href="/films/1297" title="肖申克的救赎" class="image-link" data-act="boarditem-click"
                           data-val="{movieId:1297}">
                            <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"
                                 alt="" class="poster-default"/>
                            <img data-src="https://p0.meituan.net/movie/8112a8345d7f1d807d026282f2371008602126.jpg@160w_220h_1e_1c"
                                 alt="肖申克的救赎" class="board-img"/>
                        </a>
                        <div class="board-item-main">
                            <div class="board-item-content">
                                <div class="movie-item-info">
                                    <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click"
                                                       data-val="{movieId:1297}">肖申克的救赎</a></p>
                                    <p class="star">
                                        主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
                                    </p>
                                    <p class="releasetime">上映时间：1994-09-10(加拿大)</p></div>
                                <div class="movie-item-number score-num">
                                    <p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>
                                </div>

                            </div>
                        </div>
                    </dd>
"""
url = "https://maoyan.com/board/4?offset={}"
headers = {'user-agent': 'mozilla/5.0'}
p = re.compile(
    '<dd><i class="board-index board-index-1">(.*?)</i><a *? title="(.*?)"*?</a>*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p></div>*?</dd>')
for no in range(1, 11):
    offset = (no - 1) * 10
    finUrl = url.format(offset)

    req = request.Request(finUrl, headers=headers)
    res = request.urlopen(req)
    fileName = "猫眼-TOP100-{}.html".format(no)
    html = res.read().decode('utf-8')
    print(p.findall(html))
    time.sleep(random.randint(0, 3))  # 随机休眠
