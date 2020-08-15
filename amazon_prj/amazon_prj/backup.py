import scrapy
from ..items import AmazonPrjItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1597485534&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        items = AmazonPrjItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()

        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_Price=["$"+x for x in product_price if x!="."]
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name']=product_name
        items['product_Price'] = product_Price
        items['product_imagelink'] = product_imagelink

        yield items
