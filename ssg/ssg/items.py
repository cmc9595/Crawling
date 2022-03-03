# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class SsgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    stars = scrapy.Field()
    review_count = scrapy.Field()
    img_url = scrapy.Field()
    link_url = scrapy.Field()