from scrapy.spider import Spider
import feedparser

class RSSSpider(Spider):

	def parse(self):
		feed = 