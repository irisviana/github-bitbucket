# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import web_scrapy.items as items
import web_scrapy.validation as validation

class WsSpider(scrapy.Spider):
	name = 'ws'

	def start_requests(self):

		df_links = pd.read_excel('web_scrapy/offers.xlsx', sheet_name=None)
		df_links = df_links['offers.csv']
		missing_value = df_links.columns[0]
		df_links.columns = ['links']
		df_links = df_links.append({'links':missing_value},ignore_index=True)
		sites=[]
		dt_produto_mercado_livre = df_links[df_links['links'].str.startswith('https://produto.mercadolivre')]

		dt_mercado_livre = df_links[df_links['links'].str.startswith('https://www.mercadolivre')]
		

		dt_magazine_luiza = df_links[df_links['links'].str.startswith('https://www.magazineluiza')]
		#dt_casas_bahia = df_links[df_links['links'].str.startswith('https://www.casasbahia')]


		for url in dt_produto_mercado_livre['links'].values[:]:
			yield scrapy.Request(url=url, callback=self.parse_mercado_livre)

		for url in dt_mercado_livre['links'].values[:]:
			yield scrapy.Request(url=url, callback=self.parse_mercado_livre)

		for url in dt_magazine_luiza['links'].values[:]:
			yield scrapy.Request(url=url, callback=self.parse_magazine_luiza)

	
	"########### MAGAZINE LUIZA ###########"

	def parse_magazine_luiza(self, response):

		title_unavailable= response.xpath('.//h1[@class = "header-product__title--unavailable"]').get()

		if(title_unavailable is None):
			
			ul= response.xpath('//ul[@role = "main"]')

			if(ul is not None):

				for link in ul.xpath('.//a/@href').getall():
					yield scrapy.Request(url=link.encode('utf-8'), callback=self.get_magazine_content,dont_filter=True)

		else:
			
			yield self.get_magazine_html_inf(response)

	def get_magazine_html_inf(self,response):

		items_web = items.WebScrapyItem()
		title= response.xpath('.//h1[@class = "header-product__title"]//text()').getall()
		price= response.xpath('.//span[@class = "price-template__text"]//text()').getall()
		tables= response.xpath('.//table[@class = "description__box"]//text()').getall()
		rat= response.xpath('.//span[@class = "product-review__rating-average"]//text()').get()
		val= response.xpath('.//span[@class = "product-review__rating-total"]//text()').get()
		rating,num_val=validation.get_magazine_rating_and_numval(rat,val)
		titl,pric,rati=validation.verify_encode_magazine_luiza(title,price,rating)

		items_web['Title']= titl
		items_web['Price']= pric
		items_web['E_comerce']= 'Magazine Luiza'
		items_web['Rating']= rati
		items_web['Num_Validation']= num_val
		items_web['Link_Web']= response.url.encode('utf-8')

		return items_web

	def get_magazine_content(self,response):
		yield self.get_magazine_html_inf(response)

	"########### MERCADO LIVRE ###########"

	def parse_mercado_livre(self, response):
		
		ol=response.xpath('//ol[@class = "ui-search-layout ui-search-layout--stack"]')

		if(ol is not None):
			
			div=ol.xpath('//div[@class = "ui-search-item__group ui-search-item__group--title"]')
			
			if(div is not None):

				for link in div.xpath('.//a/@href').getall():

					yield scrapy.Request(url=link.encode('utf-8'), callback=self.get_mercado_livre_html_inf,dont_filter=True)
	
		else:
			
			yield self.get_mercado_livre_html_inf(response)

	def get_mercado_livre_content(self,response):

		yield self.get_mercado_livre_html_inf(response)

	def get_mercado_livre_html_inf(self,response):

		items_web = items.WebScrapyItem()
		title= response.xpath('.//h1[@class = "ui-pdp-title"]//text()').getall()
		price= response.xpath('.//span[@class = "price-tag ui-pdp-price__part"]//text()').getall()
		rating= response.xpath('.//h2[@class = "ui-pdp-reviews__rating__summary__average"]//text()').get()
		num_val= response.xpath('.//h4[@class = "ui-pdp-reviews__rating__summary__label"]//text()').get()
		enc_title,enc_price,enc_rat,enc_val=validation.verify_encode_mercado_livre(title,price,rating,num_val)

		items_web['Title']= enc_title
		items_web['Price']= enc_price
		items_web['E_comerce']= 'Mercado Livre'
		items_web['Rating']= enc_rat
		items_web['Num_Validation']= enc_val
		items_web['Link_Web']= response.url.encode('utf-8')

		return items_web

