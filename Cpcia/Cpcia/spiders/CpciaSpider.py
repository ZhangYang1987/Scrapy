import scrapy
import uuid
from Cpcia.items import CpciaItem
from scrapy.selector import Selector

class CpciaSpider(scrapy.Spider):
    name='cpcia'
    allowed_domains=['cpcia.org.cn']
    start_urls=[]
    for i in range(401,501):
        start_urls.append('http://www.cpcia.org.cn/html/19/news_page%d.html' %i)

    def parse(self, response):
        # item = CpciaItem()
        selector = Selector(response)
        # title = selector.xpath('//h1[@class="title"]/text()').extract()
        # time = selector.xpath('//div[@class="source"]/text()').extract()
        # # link=selector.xpath('//div[@class="page_list"]/ul/li/a/@href').extract()
        # content = selector.xpath('//div[@class="content"]/p/text()').extract()
        # # img_urls=selector.xpath('//p/img/@src').extract()
        #
        # # for img_url in img_urls:
        # #     b = 'http://www.miit.gov.cn'
        # #     for i in img_url.split('/')[4:]:
        # #         b+='/'+i
        # #     item['img_url'] = [b]
        # #     yield item
        #
        # item['title'] = str(title)
        # item['time'] = str(time)
        # item['content'] = str(content)
        # item['id'] = str(uuid.uuid1())
        # #
        # print(title, time, content)
        # # print(link)
        # yield item

        for link in selector.xpath('//div[@class="page_list"]/ul/li/a/@href').extract():
            b = 'http://www.cpcia.org.cn'+link
            # print(b)
            yield response.follow(b, callback=self.children_parse)

        # for link in selector.xpath('//a[@class="wh14"]/@href').extract():
        #     b = 'http://www.cpcia.org.cn'+link
        #     # print(b)
        #     yield response.follow(b, callback=self.children_parse)

    def children_parse(self,response):
        item = CpciaItem()
        selector = Selector(response)
        title = selector.xpath('//h1[@class="title"]/text()').extract()
        time = selector.xpath('//div[@class="source"]/text()').extract()
        # link=selector.xpath('//div[@class="page_list"]/ul/li/a/@href').extract()
        content = selector.xpath('//div[@class="content"]/p/text()').extract()
        item['title'] = str(title)
        item['time'] = str(time)
        item['content'] = str(content)
        item['id'] = str(uuid.uuid1())
        #
        # print(title, time, content)
        # print(link)
        yield item

        pass
