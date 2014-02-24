# -*- coding: UTF-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy import log
import numpy as np
import db
from sqlalchemy.orm import sessionmaker


words_to_match = ['Bitcoin', u'ビットコイン', u'買う機種']


class CryptoCurrencyPipeline(object):
    def __init__(self):
		engine = db.connect()
		engine.connect()
		db.create_tables(engine)
		self.SessionMaker = sessionmaker(bind = engine)
		

    def get_item_rank(self, item):
    	rank = 0
    	for word in words_to_match:
    		rank += item['title'][0].count(word) + np.log(item['description'][0].count(word) + 1)
    	return rank


    def process_item(self, item, spider):
		rank = self.get_item_rank(item)
		#print rank
		#if rank > 0:
		if rank > 0:
			item['rank'] = rank
			session = self.SessionMaker()
			news_item = db.NewsItem(**item)
			try:
				session.add(news_item)
				session.commit()
			except:
				session.rollback()
				raise
			finally:
				session.close()
			return item
		else:
			raise DropItem('Dropping irrelevant article:')
