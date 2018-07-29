import scrapy
from faren.items import FarenItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = "autospd"
    allowed_domains = {"https://sh.tianyancha.com/search"}
    start_urls = {
        'https://sh.tianyancha.com/search'
    }

    def parse(self, response):
        item=AutopjtItem()
        # 通过各XPath表达式分别提取商品的名称、价格、链接、评论数等信息
        item["company"] = response.xpath("//a[@class='name']/@text()").extract()
        item["name"] = response.xpath("//a[@class='legalPersonName hover_underline']/@text()").extract()
        item["telephone"] = response.xpath("//span[@class='link-hover-click']/@text()").extract()
        # 提取完成后返回item
        yield item
        for i in range(1, 250):
            url = "https://sh.tianyancha.com/search/p"+str(i)
            # 通过yield返回Request,并指定要爬取的网址和回调函数
            # 实现自动爬取
            yield Request(url, callback=self.parse)
