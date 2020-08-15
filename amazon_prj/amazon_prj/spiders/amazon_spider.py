import scrapy
from ..items import AmazonPrjItem
url_str=input("Enter the product category you want to search for : ")
words = url_str.split()
var = len(words)
if var == 1:
	url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=" + words[0]

if var == 2:
	url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=" + words[0] + "+" + words[1]

elif var == 3:
	url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=" + words[0] + "+" + words[1] + "+" + words[2]

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        url
    ]

    def parse(self, response):
        items = AmazonPrjItem()

        product_name = response.css('.a-size-base-plus.a-text-normal').css('::text').extract()
        product_Name = [x.strip() for x in product_name if x.strip()!=""]

        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_Price=["$"+x for x in product_price if x!="."]
        product_imagelink = response.css('.s-image::attr(src)').extract()
        product_stars =  response.css("span.a-icon-alt::text").extract()

        items['product_Name']=product_Name
        items['product_Price'] = product_Price
        items['product_imagelink'] = product_imagelink
        items['product_stars'] = product_stars

        yield items
