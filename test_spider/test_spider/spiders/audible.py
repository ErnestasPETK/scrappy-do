import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.audible.com/search",
            callback=self.parse,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            },
        )

    def parse(self, response):
        audiobooks = response.xpath(
            '//ul[contains(@class,"bc-list")]/*[contains(@class,"productListItem")]'
        )
        for audiobook in audiobooks:
            title = audiobook.xpath(".//h3/a/text()").get()
            author = audiobook.xpath(
                './/li[contains(@class,"authorLabel")]/span/a/text()'
            ).get()
            narrator = audiobook.xpath(
                './/li[contains(@class,"narrator")]/span/a/text()'
            ).get()
            runtime = audiobook.xpath(
                './/li[contains(@class,"runtimeLabel")]/span/text()'
            ).get()
            price = audiobook.xpath(".//p[contains(id,buybox)]/span[2]/text()").get()

            yield {
                "title": title,
                "author": author,
                "narrator": narrator,
                "runtime": runtime.split("Length: ")[1],
                "price": price.strip(),
            }

        pagination_container = response.xpath('//ul[contains(@class,"pagingElements")]')
        next_page = pagination_container.xpath(
            './/li[last()]/span[contains(@class,"nextButton")]/a'
        )
        next_page_link = next_page.xpath(".//@href").get()

        if next_page_link:
            yield response.follow(url=next_page_link, callback=self.parse, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
