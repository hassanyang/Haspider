import scrapy


class ApkmonkSpider(scrapy.Spider):
    name = 'apkmonk'
    allowed_domains = ['https://www.apkmonk.com/']
    start_urls = ['http://https://www.apkmonk.com//']

    def parse(self, response):
        pass
