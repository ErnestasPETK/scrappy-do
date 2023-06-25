import scrapy


class WorldometerSpider(scrapy.Spider):
    name = "worldometer"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        countries = response.xpath("//td/a")

        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            # absolute url
            absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url)

            # relative url
            yield response.follow(url=link)
            # yield{
            #     "country_name": country_name,
            #     "link":absolute_url,
            # }
    
