import scrapy
import pandas as pd
from ssg.items import SsgItem

class SsgSpider(scrapy.Spider):
    handle_httpstatus_list = [401]
    name = 'ssg'
    user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    allowed_domains = ['ssg.com']
    #start_urls = []
    
    def start_requests(self):
        for page in range(1, 6):
            yield scrapy.Request(f'http://www.ssg.com/service/bestCtgItemList.ssg?zoneId=5000016005&ctgId=&page={page}', self.parse)
        #print(url)

    def parse(self, response):
        #print(response.text)
        for i in response.xpath('//*[@id="bestCategoryItem"]/li'):
            item = SsgItem()
            item['rank'] = i.xpath('div[1]/div[1]/span[1]/text()').extract()
            item['title'] = i.xpath('div[2]/div[2]/div/a/em[1]/text()').extract()
            item['price'] = i.xpath('div[2]/div[3]/div[1]/em/text()').extract()
            if not (stars := i.xpath('div[2]/div[5]/div/div/span/span/text()').extract()):
                stars = i.xpath('div[2]/div[4]/div/div/span/span/text()').extract()
            item['stars'] = stars
            if not (count := i.xpath('div[2]/div[5]/div/span/em/text()').extract()):
                if not (count := i.xpath('div[2]/div[4]/div/div/span/em/text()').extract()):
                    count = i.xpath('div[2]/div[4]/div/span/em/text()').extract()
            item['review_count'] = count
            item['img_url'] = 'https:' + i.xpath('div[1]/div[2]/a/img[1]/@src').extract()[0]
            item['link_url'] = 'https://www.ssg.com' + i.xpath('div[1]/div[2]/a/@href').extract()[0]
            #print(rank, title, price, stars, review_count, img_url, link_url)
            yield item
