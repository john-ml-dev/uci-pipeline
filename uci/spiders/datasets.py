import scrapy


class DatasetsSpider(scrapy.Spider):
    name = "datasets"
    allowed_domains = ["uci.com"]
    start_urls = ["https://uci.com"]

    def parse(self, response):
        pass
