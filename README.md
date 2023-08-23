# Scrapy Web Scrapers for Amazon and Etsy

This project contains Scrapy spiders designed to extract data from Amazon's Best Sellers and Etsy's category pages.

## Features

- **Amazon Best Sellers Spider**: Extracts the top 10 items from various best seller categories on Amazon.
- **Etsy Category Spider**: Scrapes all visible attributes of items from provided Etsy category pages.
- **User Agent Rotation**: Uses a rotation of user agents to reduce the risk of being blocked.
- **Logging Pipeline**: Logs the scraped items for debugging purposes.
- **Database Storage Pipeline (Placeholder)**: A skeleton pipeline for storing scraped items in a database.

## Prerequisites

- Python 3.x
- Scrapy

## Setup

1. **Install Scrapy**:
   ```bash
   pip install scrapy
   ```

2. **Provide the URLs**:
   - For Amazon: Add the desired Amazon best seller URLs to the `amazon_links.txt` file, one URL per line.
   - For Etsy: Add the desired Etsy category URLs to the `etsy_links.txt` file, one URL per line.

## Usage

1. **Run the Amazon Spider**:
   ```bash
   scrapy crawl amazon_bestsellers
   ```

2. **Run the Etsy Spider**:
   ```bash
   scrapy crawl etsy_scraper
   ```

3. **Output**: Once the spiders complete their runs, you'll find the scraped data in CSV files (`amazon_bestsellers.csv` and `etsy_items.csv`).

## Notes

- Web structures can change over time. The spiders might require adjustments based on any changes made to the Amazon or Etsy pages.
- Web scraping might be against the terms of service of some websites. Always ensure you have the right to scrape a website and respect `robots.txt`.
- Consider using additional middlewares to handle CAPTCHAs, use proxies, or implement other anti-blocking strategies for a more robust solution.

## License

This project is open-source and available under the [MIT License](LICENSE).
