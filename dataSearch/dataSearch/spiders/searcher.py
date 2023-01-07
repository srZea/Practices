import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

class searcher (CrawlSpider):
    name = 'book searcher'
    urls = ['https://books.toscrape.com/index.html']

    rules = [ 
        Rule(LinkExtractor(restrict_css = '.nav-list > li > ul > li > a'), follow = True),
        Rule(LinkExtractor(restrict_css = '.table-striped > body > td'), callback = 'parser_book' )
        
        ]

    def parser_book (self, response): 



       