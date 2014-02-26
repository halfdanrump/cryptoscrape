from scrapy.spider import Spider
from scrapy import log
from cryptoscrape.items import CryptoNewsItem
import feedparser
from settings import feed_urls

class RSSSpider(Spider):

	name = 'rssfeedparser'
	#start_urls = ['http://rss.rssad.jp/rss/itmtop/1.0/topstory.xml']
	start_urls = feed_urls
	def parse(self, response):
		feed_items = list()
		log.msg('Scraping URL %s'%response.url)
		feed = feedparser.parse(response.url)
		
		try:
			for item in feed['entries']:
				news_item = CryptoNewsItem()
				news_item['title'] = item.get('title', None)
				news_item['link'] = item.get('link', None)
				news_item['description'] = item.get('description', None)
				news_item['summary'] = item.get('summary', None)
				feed_items.append(news_item)
		except KeyError:
			log.msg('Feed contained no items', level=log.WARNING)

		return feed_items