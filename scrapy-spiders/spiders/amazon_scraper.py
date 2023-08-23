import scrapy

class AmazonBestSellersSpider(scrapy.Spider):
    name = 'amazon_bestsellers'
    
    # Read the links from a text file
    with open('../amazon_links.txt', 'r') as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        # Extract the top 10 items from the category
        for item in response.css('div.zg_itemImmersion')[:10]:
            yield {
                'category': response.css('span.zg_selected::text').get(),
                'rank': item.css('span.zg_rankNumber::text').get(),
                'name': item.css('div.p13n-sc-truncated::text').get().strip(),
                'url': item.css('a.a-link-normal::attr(href)').get()
            }

# Settings for the spider
BOT_NAME = 'amazon_scraper'
SPIDER_MODULES = ['amazon_scraper.spiders']
NEWSPIDER_MODULE = 'amazon_scraper.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
ROBOTSTXT_OBEY = True
FEED_FORMAT = 'csv'
FEED_URI = 'amazon_bestsellers.csv'

# Adjust the concurrency settings
CONCURRENT_REQUESTS = 10
DOWNLOAD_DELAY = 1  # Adjust this based on how aggressive you want the spider to be
