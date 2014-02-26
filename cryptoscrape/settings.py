# -*- coding: UTF-8 -*-
# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cryptoscrape'

SPIDER_MODULES = ['cryptoscrape.spiders']
NEWSPIDER_MODULE = 'cryptoscrape.spiders'
ITEM_PIPELINES = {
	'cryptoscrape.pipelines.CryptoCurrencyPipeline':1
}

LOG_LEVEL = 'INFO'
#LOG_STDOUT = True

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',	
            'username': '',
            'password': '',
            'database': 'cryptocurrencynews'}


words_to_match = ['Bitcoin', u'ビットコイン', '']

### Select the xml fields in the news items which are used in the document ranking
primary_fields = ['title']
secondary_fields = ['description', 'summary']

feed_urls = [
			'http://feeds.gawker.com/gizmodo/full',
			'http://techcrunch.com/feed/',
			'http://rss.itmedia.co.jp/rss/1.0/topstory.xml'
			]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
