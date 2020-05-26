# -*- coding: utf-8 -*-
import scrapy
from banzhu.json.jsonload import jsonLoad
from banzhu.items import TitleItem

class TitleSpider(scrapy.Spider):
    name = 'title'
    allowed_domains = ['diyibanzhu7.xyz']
    start_urls = ['http://diyibanzhu7.xyz/shuku/']
    articleName = ""

    def __init__(self):
        load = jsonLoad()
        self.q = load.load("/Users/yisquare-cs/python3/banzhu/f.json")
        data = self.q.get()
        self.articleName =  data['articleName']
        self.start_urls[0] = 'http://diyibanzhu7.xyz' + data['link'][0]
        pass

    def parse(self, response):
        data = response.xpath('//div[@class="mod block update chapter-list"]/div[@class="bd"]')
        for line in data[1].xpath('./ul[@class="list"]/li'):
            # 初始化item对象保存爬取的信息
            item = TitleItem()
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['title'] = line.xpath('./a/text()').get()
            item['articleName'] = self.articleName
            item['link'] = line.xpath('./a/@href').extract()
            yield item

        new_links = response.xpath('//a[@class="nextPage"]/@href').extract()
        end_page_links = response.xpath('//a[@class="endPage"]/@href').extract()
        
        #http://diyibanzhu7.xyz/15/15216/
        if new_links:
            new_link = new_links[0]
            end_page = end_page_links[0]
            if new_link == end_page:
                data = self.q.get()
                self.articleName =  data['articleName']
                new_link = data['link'][0]
                next_page_url = response.urljoin(new_link)
                print next_page_url
                yield scrapy.Request(next_page_url, callback=self.parse)
            else:
                next_page_url = response.urljoin(new_link)
                yield scrapy.Request(next_page_url, callback=self.parse)
        pass

"""

<div class="container">
<div class="mod mod-back breadcrumb">
<div class="bd">
<a href="/" class="home"></a>
<span class="divide"></span>
<a href="/fenlei/7_1.html">其他类别小说</a>
<span class="divide"></span>
<a href="/15/15216/">偷吃老爸好几次章节目录</a>
</div>
</div>
<div class="mod detail">
<div class="bd column-2">
<div class="left">
</div>
<div class="right">
<h1>偷吃老爸好几次</h1>
<p class="info">
作者：lili525<br>
类型：其他类别<br>
字数：46854<br>
人气：5271 </p>
<span class="status is-serialize">连载中..</span>
</div>
</div>
<div class="ft">
<table>
<tbody><tr>
<td width="50%">
<a class="read start" href="323329.html">从头开始阅读</a>
</td>
<td width="5">&nbsp;</td>
<td width="50%">
<a class="collect" href="/">Prohibit downloads</a>
</td>
</tr>
</tbody></table>
</div>
</div>
<div class="mod book-intro">
<div class="bd"> 我的家在南方某市郊区的一个大工厂，据说这个工厂是在建国初期建成的。那时我们国家一穷二白，急需工厂生产物资，但是为了防止空袭只得把工厂建在了偏远不易被发现的山区。这是一个织布工厂，几千工人，有自己的生活区、生产区，有市场、电影院、学校、医院，每天晚上工厂还通过自己的闭路电视给大家放录像。从70年代到90年代，这个工厂有着自己强大的生命力。我后来回想起来，这就是一个巴伐利亚小镇一样的工厂，这里的男人女人基本上自给自足，包括恋爱、结婚、生子。想象一下，这里到处是妙龄的织布女工和健壮的机修工人，尽管市区到这里有公交车，但是绝大多数的人们下班后还是回到自己的小家，洗澡吃饭完毕后简单的娱乐一下，夜幕降临精彩的故事才刚刚开始。
</div>
</div>
<div class="slide-baidu"><script src="/js/htmlk.js" type="text/javascript"></script></div>
<div class="mod block update chapter-list">
<div class="hd">
<h4>偷吃老爸好几次最新章节</h4>
</div>
<div class="bd">
<ul class="list">
<li><a href="/15/15216/335670.html">偷吃老爸好几次（08-09）</a></li>
<li><a href="/15/15216/327282.html">偷吃老爸好几次（07）</a></li>
<li><a href="/15/15216/327281.html">偷吃老爸好几次（06）2u2u2u.C〇M</a></li>
</ul>
</div>
</div> <div class="slide-baidu"><script src="/js/htmlk.js" type="text/javascript"></script></div>
<div class="mod block update chapter-list">
<div class="hd">
<h4>偷吃老爸好几次章节列表</h4>
</div>
<div class="bd">
<ul class="list"><li><a href="/15/15216/323329.html">偷吃老爸好几次（01）</a></li>
<li><a href="/15/15216/323330.html">偷吃老爸好几次（02）</a></li>
<li><a href="/15/15216/323331.html">偷吃老爸好几次（03）</a></li>
<li><a href="/15/15216/325704.html">偷吃老爸好几次（04）</a></li>
<li><a href="/15/15216/325705.html">偷吃老爸好几次（05）</a></li>
<li><a href="/15/15216/327281.html">偷吃老爸好几次（06）2u2u2u.C〇M</a></li>
<li><a href="/15/15216/327282.html">偷吃老爸好几次（07）</a></li>
<li><a href="/15/15216/335670.html">偷吃老爸好几次（08-09）</a></li>
</ul>
</div>
</div>
<div class="slide-baidu"><script src="/js/htmlk.js" type="text/javascript"></script></div>
<div class="mod page">
<div class="pagelistbox">
<div class="page"><a class="indexPage" href="/15/15216_1/">首页</a><a class="prePage" href="/15/15216_1/">上页</a><a class="nextPage" href="/15/15216_1/">下页</a><a class="endPage" href="/15/15216_1/">尾页</a>(第1/1页)当前20条/页 输入<input id="pageinput" size="4"><input type="button" value="跳转" onclick="if (!window.__cfRLUnblockHandlers) return false; page()"></div></div>
</div>
<div class="slide-baidu"><script src="/js/htmlk.js" type="text/javascript"></script></div>
<div class="mod block column-list">
<div class="hd" boxid="heiyanMobileChapterJingpin">
<h4>类似偷吃老爸好几次的小说推荐</h4>
</div>
<div class="bd">
<ul class="list">
<li><a href="/0/3/"><img src="/images/jipin-default.jpg" alt="七彩玫瑰" onerror="this.src='/images/jipin-default.jpg'"></a><div class="name"><a href="/0/3/">七彩玫瑰</a></div></li><li><a href="/0/4/"><img src="/images/jipin-default.jpg" alt="人妻赵天云修车群辱记" onerror="this.src='/images/jipin-default.jpg'"></a><div class="name"><a href="/0/4/">人妻赵天云修车群辱记</a></div></li><li><a href="/0/5/"><img src="/images/jipin-default.jpg" alt="天鹅泪" onerror="this.src='/images/jipin-default.jpg'"></a><div class="name"><a href="/0/5/">天鹅泪</a></div></li><li><a href="/0/6/"><img src="/images/jipin-default.jpg" alt="我在AV的日子" onerror="this.src='/images/jipin-default.jpg'"></a><div class="name"><a href="/0/6/">我在AV的日子</a></div></li><li><a href="/0/8/"><img src="/images/jipin-default.jpg" alt="拉姆纪-第二卷" onerror="this.src='/images/jipin-default.jpg'"></a><div class="name"><a href="/0/8/">拉姆纪-第二卷</a></div></li><li><a href="/0/11/"><img src="/images/jipin-default.jpg" alt="程庄杂交实录" onerror="this.src='/images/jipin-default.jpg'"></a><div class="name"><a href="/0/11/">程庄杂交实录</a></div></li><li><a href="/0/13/"><img src="/images/jipin-default.jpg" alt="再见，金小姐(人生如梦)" onerror="this.src='/images/jipin-default.jpg'"></a><div class="name"><a href="/0/13/">再见，金小姐(人生如梦)</a></div></li><li><a href="/0/15/"><img src="/images/jipin-default.jpg" alt="性感的美腿女神(合集)" onerror="this.src='/images/jipin-default.jpg'"></a><div class="name"><a href="/0/15/">性感的美腿女神(合集)</a></div></li>
</ul>
</div>
</div>
<div class="mod mod-back">
<div class="bd">
<a href="/" class="home"></a>
<span class="divide"></span>
<a href="/fenlei/7_1.html">其他类别小说</a>
<span class="divide"></span>
<a href="/15/15216/">偷吃老爸好几次最新章节</a>
</div>
</div>
</div>

"""