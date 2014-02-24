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

LOG_LEVEL = 'DEBUG'

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',	
            'username': '',
            'password': '',
            'database': 'cryptocurrencynews'}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
