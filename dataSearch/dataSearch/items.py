# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DatasearchItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    autor = scrapy.Field()
    #genre =  scrapy.Field()
    price = scrapy.Field()