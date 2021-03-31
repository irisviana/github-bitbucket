# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
class MlSpider(scrapy.Spider):
	
    name = 'ml'
    
    #start_urls = [dt_mercado_livre['links'].values[4]]

    #def parse(self, response,**kwargs):
        #pass
'''
	def parse(self, response):

		items_web = items.WebScrapyItem()
		price= response.xpath('//span[@class = "price-tag ui-pdp-price__part"]//text()').getall()

		if(len(price)==0):

			div= response.xpath('//div[@class="ui-search-result__content-wrapper"]')

			for i in range(len(div)):

				title_mult = div[i].xpath('.//h2[@class = "ui-search-item__title"]//text()').getall()
				price_mult = div[i].xpath('//span[@class = "price-tag ui-search-price__part"]//text()').getall()

				items_web['Title']= self.verify_encode_title(title_mult)
				items_web['Price']= self.verify_encode_price(price_mult)

				yield items_web
		else:

			title= response.xpath('.//h1[@class = "ui-pdp-title"]//text()').getall()
			
			items_web['Title']= self.verify_encode_title(title)
			items_web['Price']=float(price[1].encode('utf-8'))
			
			yield items_web
'''

			
		
		
