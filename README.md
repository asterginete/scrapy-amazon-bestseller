# Amazon Best Sellers Scraper

This scraper is built using the Scrapy framework and is designed to extract the top 10 items from various best seller categories on Amazon.

## Features

- Reads a list of Amazon best seller URLs from a text file.
- Extracts the top 10 items from each provided category.
- Outputs the scraped data to a CSV file.

## Prerequisites

- Python 3.x
- Scrapy

## Setup

1. **Install Scrapy**:
   If you haven't installed Scrapy yet, you can do so using pip:
   ```bash
   pip install scrapy
   ```

2. **Provide the Amazon Best Seller URLs**:
   Add the desired Amazon best seller URLs to the `amazon_links.txt` file, one URL per line.

## Usage

1. Navigate to the root directory of the Scrapy project.
2. Run the spider using the following command:
   ```bash
   scrapy crawl amazon_bestsellers
   ```

3. Once the spider completes its run, you'll find the scraped data in `amazon_bestsellers.csv`.

## Notes

- Amazon frequently changes its website structure. The scraper might require adjustments based on any changes made to the Amazon page.
- Web scraping might be against Amazon's terms of service. Always ensure you have the right to scrape a website and respect `robots.txt`.
- Amazon might block or throttle requests from scrapers. Consider using middlewares to rotate user agents or proxies, and handle CAPTCHAs for a more robust solution.

## License

This project is open-source and available under the [MIT License](LICENSE).
