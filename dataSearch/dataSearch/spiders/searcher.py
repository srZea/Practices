from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
class searcher (CrawlSpider):
    name = 'bookSpider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/index.html']
    base_url = 'https://books.toscrape.com'

    rules = [ 
        Rule(LinkExtractor(restrict_css = 'div.side_categories .nav-list li ul li a'), follow = True, callback = 'parse'),
        ]

    def parse(self, response): 
       for i in response.css('div.col-sm-8.col-sm-9'): 
            yield [{'name':i.css('div.col-sm-6.product_main h1::text').get(),
                  'genre':i.css('div.page-header action h1::text').get(),
                  'price':i.css('div.product_price p.price_color::text').get()}]
       