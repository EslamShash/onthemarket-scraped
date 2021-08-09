import scrapy
from scrapy_selenium import SeleniumRequest
from ..items import OnthemarketItem

class MarketSpider(scrapy.Spider):
    name = 'market'
    page_number = 2
    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.onthemarket.com/for-sale/property/london/?view=grid",
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        items = OnthemarketItem()
        homes = response.xpath("//ul[@id='properties']/child::li")
        for home in homes:
            items['title'] = home.xpath(".//span[@class='title']/a/text()").get()
            items['address'] = home.xpath(".//span[@class='address']/a/text()").get()
            items['price'] = home.xpath(".//a[@class='price']/text()").get()
            items['phone'] = home.xpath(".//div[@class='telephone']/a/text()").get()
            items['store'] = home.xpath(".//a[@class='marketed-by-link']/text()").get()
            items['url'] = response.urljoin(home.xpath(".//span[@class='title']/a/@href").get())
            if items['title'] is not None:
                yield items

        next_page = response.urljoin(response.xpath("//a[@title='Next page']/@href").get())
        if next_page:
            yield SeleniumRequest(
                url=next_page,
                wait_time=3,
                callback=self.parse
            )