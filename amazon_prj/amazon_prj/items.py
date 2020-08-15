# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonPrjItem(scrapy.Item):
    # define the fields for your item here like:
    product_Name = scrapy.Field()
    product_Price= scrapy.Field()
    product_imagelink= scrapy.Field()
    product_stars=scrapy.Field()



