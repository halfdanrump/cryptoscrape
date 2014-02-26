from scrapy.contrib.spiders import XMLFeedSpider
from cryptoscrape.items import CryptoNewsItem

#from myproject.items import TestItem

class XMLSpider(XMLFeedSpider):
    name = 'xmlfeedparser'
    #allowed_domains = ['http://techcrunch.com/']
    #start_urls = ['http://techcrunch.com/feed/', 'feeds.gawker.com/gizmodo/full']
    start_urls = ['http://feeds.gawker.com/gizmodo/full']
    # allowed_domains = ['rss.rssad.jp']
    # start_urls = ['rss.rssad.jp/rss/itmtop/1.0/topstory.xml']
    iterator = 'iternodes' # This is actually unnecessary, since it's the default value
    itertag = 'item' # Iterrate over all item tags

    def parse_node(self, response, node):
        item = CryptoNewsItem()
        item['title'] = node.xpath('title/text()').extract()
        item['link'] = node.xpath('link/text()').extract()
        item['description'] = node.xpath('description/text()').extract()
        return item