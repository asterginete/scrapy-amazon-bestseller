# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AmazonBestSellerItem(scrapy.Item):
    category = scrapy.Field()
    rank = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()

class EtsyCategoryItem(scrapy.Item):
    title = scrapy.Field()
    shop_name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()
