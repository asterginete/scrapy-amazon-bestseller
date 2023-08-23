import scrapy

class EtsySpider(scrapy.Spider):
    name = 'etsy_scraper'
    
    # Read the links from a text file
    with open('etsy_links.txt', 'r') as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        # Extracting items from the category page
        for item in response.css('div.js-merch-stash-check-listing'):
            yield {
                'title': item.css('h3.text-gray.text-truncate.mb-xs-0.text-body::text').get(),
                'shop_name': item.css('p.text-gray-lighter.text-body-smaller.no-wrap.mb-xs-0::text').get(),
                'price': item.css('span.currency-value::text').get(),
                'url': item.css('a::attr(href)').get(),
                'image_url': item.css('img::attr(src)').get(),
                # Add more attributes as needed
            }

        # Pagination: Follow the next page link if it exists
        next_page = response.css('a.wt-action-group__item::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

# Settings for the spider
BOT_NAME = 'etsy_scraper'
SPIDER_MODULES = ['etsy_scraper.spiders']
NEWSPIDER_MODULE = 'etsy_scraper.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
ROBOTSTXT_OBEY = True
FEED_FORMAT = 'csv'
FEED_URI = 'etsy_items.csv'
