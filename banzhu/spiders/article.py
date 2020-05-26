# -*- coding: utf-8 -*-
import scrapy
from banzhu.items import ArticleCatalogItem
import chardet
  

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['diyibanzhu7.xyz']
    start_urls = ['http://diyibanzhu7.xyz/shuku/']

    def parse(self, response):
        for line in response.xpath('//li[@class="column-2 "]'):
            # 初始化item对象保存爬取的信息
            item = ArticleCatalogItem()
            # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
            item['articleName'] = line.xpath('./div/a[@class="name"]/text()').get()
            item['link'] = line.xpath('./div/a[@class="name"]/@href').extract()
            yield item

        new_links = response.xpath('//a[@class="nextPage"]/@href').extract()
        if new_links:
            new_link = new_links[0]
            next_page_url = response.urljoin(new_link)
            yield scrapy.Request(next_page_url, callback=self.parse)
            print '----------->'
            print next_page_url
            # yield scrapy.Request("http://diyibanzhu7.xyz" + new_link, callback=self.parse)
        
        pass

"""

<div class="mod page">
<div class="pagelistbox">
<div><script type="text/javascript">fanyeshang()</script></div>
<a class="nextPage" href="/shuku/0-lastupdate-0-2.html">下页</a><a class="endPage" href="/shuku/0-lastupdate-0-797.html">尾页</a><a href="#" style="width:200px;">(第1/797页)当前20条/页</a><a style="width:150px;">输入页数<input id="pageinput" size="4"><input type="button" value="跳转" onclick="if (!window.__cfRLUnblockHandlers) return false; page()"> </a>
</div>
<div class="slide-baidu"><script src="/js/htmlk.js" type="text/javascript"></script></div>
</div>"""