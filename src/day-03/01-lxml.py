# - - - - - - - - - - - 
# @author like
# @since 2021-02-06 9:25
# @email 980650920@qq.com

from lxml import etree

html = """
<div class="main-nav" data-sudaclick="blk_mainnav">
	<div class="nav-mod-1">
	<ul>
		<li><a href="http://news.sina.com.cn/" target="_blank"><b>新闻</b> </a></li>
		<li><a href="http://mil.news.sina.com.cn/" target="_blank">军事</a></li>
		<li><a href="https://news.sina.com.cn/china/" target="_blank">国内</a></li>
		<li><a href="http://news.sina.com.cn/world/" target="_blank">国际</a></li>
	</ul>
	<ul>
		<li><a href="http://finance.sina.com.cn/" target="_blank"><b>财经</b></a></li>
		<li><a href="http://finance.sina.com.cn/stock/" target="_blank">股票</a></li>
		<li><a href="http://finance.sina.com.cn/fund/" target="_blank">基金</a></li>
		<li><a href="http://finance.sina.com.cn/forex/" target="_blank">外汇</a></li>
	</ul>
	<ul>
		<li><a href="http://tech.sina.com.cn/" target="_blank"><b>科技</b></a></li>
		<li><a href="http://mobile.sina.com.cn/" target="_blank">手机</a></li>
		<li><a href="http://tech.sina.com.cn/discovery/" target="_blank">探索</a></li>
		<li><a href="http://zhongce.sina.com.cn/" target="_blank">众测</a></li>
	</ul>
</div>
"""
parseHtml = etree.HTML(html)
titleList = parseHtml.xpath('//a/text()')
urlList = parseHtml.xpath('//a/@href')
print(titleList)
print(urlList)
