from sqlalchemy.orm import sessionmaker
from web_scrapy.models import QuoteDB, db_connect, create_table
import pymysql
pymysql.install_as_MySQLdb()
class ScrapySpiderPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def verify_title_is_null(self,title):

        is_null=False

        if(title is None):

            is_null=True

        return is_null

   
        
    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        if (self.verify_title_is_null(item["Title"]) == False):
            session = self.Session()
            quotedb = QuoteDB()
            quotedb.Title = item["Title"]
            quotedb.Price = item["Price"]
            quotedb.E_comerce      = item['E_comerce']
            quotedb.Rating         = item['Rating']
            quotedb.Num_Validation = item['Num_Validation']
            quotedb.Link_Web       = item['Link_Web']
            # check whether the product exists
            #exist_product = session.query(QuoteDB).filter_by(Title = quotedb.Title).first()
            

            try:
                session.add(quotedb)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

            return item