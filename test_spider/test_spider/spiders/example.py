import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.meteo.lt"]
    start_urls = ["http://www.meteo.lt/en/"]

    def parse(self, response):
        pass
