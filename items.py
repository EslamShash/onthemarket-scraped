# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OnthemarketItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    store = scrapy.Field()
    phone = scrapy.Field()
    url = scrapy.Field()
    pass
