# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    Title 	       = scrapy.Field()
    Price 	       = scrapy.Field()
    E_comerce      = scrapy.Field()
    Rating   	   = scrapy.Field()
    Num_Validation = scrapy.Field()
    Link_Web 	   = scrapy.Field()
    
    
