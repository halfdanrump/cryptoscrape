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
from settings import words_to_match, primary_fields, secondary_fields



class CryptoCurrencyPipeline(object):
    def __init__(self):
		engine = db.connect()
		engine.connect()
		db.create_tables(engine)
		self.SessionMaker = sessionmaker(bind = engine)
		#log.start(logfile = 'spiderlog')
		



    def get_item_rank(self, item):
    	"""
    	Each occurance of any of the match-words in the title will increase the rank of the item by 1, whereas 
    	words in the description will increase the rank with the log of number of matches

    	"""
    	pf_rank = 0
    	sf_rank = 0
    	for word in words_to_match:
			pf_rank += sum(map(lambda field: item.get(field, '').lower().split(' ').count(word.lower()), primary_fields))
			sf_rank += sum(map(lambda field: item.get(field, '').lower().split(' ').count(word.lower()), secondary_fields))
    	rank = pf_rank + np.log(sf_rank)
    	return rank


    def process_item(self, item, spider):
		rank = self.get_item_rank(item)
		if rank > 0:
			item['rank'] = rank
			session = self.SessionMaker()
			news_item = db.NewsItem(**item)
			log.msg(u"Inserted item with title '%s' into the database."%item['title'])
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
			log.msg("Dropping irrelevant item")
			#pass
			#raise DropItem('Dropping irrelevant article:')
