#15:32,18:00

from sqlalchemy.orm import sessionmaker
from web_scrapy.models import  db_connect,QuoteDB
import pymysql

class Search_data (object):
	def __init__(self):
		"""
		Initializes database connection and sessionmaker.
		Creates deals table.
		"""
		engine = db_connect()
		self.Session = sessionmaker(bind=engine)
		self.get_table()


	def get_table(self):

		session.query(User).all()
		quotedb = QuoteDB()
		datas = session.query(quotedb).all()
		for d in datas[0]:
			print (d)
        
   	