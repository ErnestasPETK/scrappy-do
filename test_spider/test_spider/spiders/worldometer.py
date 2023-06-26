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
            yield response.follow(url=link, callback=self.parse_country, meta={"country": country_name})
# (//div[@class="table-responsive"]/table)[1]/tbody/tr
            # yield{
            #     "country_name": country_name,
            #     "link":absolute_url,
            # }
            

    def parse_country(self, response):
        year_rows = response.xpath('(//div[@class="table-responsive"]/table)[1]/tbody/tr')
        country = response.request.meta.get("country")
        for row in year_rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                "country" : country,
                "year" : year,
                "population" : population,
            }
            