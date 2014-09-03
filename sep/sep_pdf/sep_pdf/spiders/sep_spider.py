from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import Selector
from sep_pdf.items import SepPdfItem
from time import time
import csv
import re
import string
import sys

class SepSpider201301(CrawlSpider):
	name = 'sep_crawler_gral'
	allowed_domains = ["sep.gob.mx"]
	def start_requests(self):
		yield Request(self.mekler) 
	def parse(self, response):
		sel = Selector(response)
		items = []
		item = SepPdfItem()
		archivos = []
		sites = sel.xpath('//div[@id="content"]/p')
		if len(sites) <10:
			sites = sel.xpath('//div[@id="indiceTematico"]/div/h3')
		for site in sites:
			link = site.xpath('a/@href').extract()
			if len(link)>0:
				if link[0].find('http')>=0:
					request = Request(link[0], callback=self.parse_pdf)
				else:
					request = Request('http://www.sep.gob.mx'+link[0], callback=self.parse_pdf)
				yield request
		pass

	def parse_pdf(self, response):
		sel = Selector(response)
		items = []
		item = SepPdfItem()
		archivos = []
		sites = sel.xpath('//div[@id="content"]/p')
		if len(sites)==0:
			sites = sel.xpath('//div[@id="interna_colIzquierda"]/p')
		item['url'] = response.url
		for site in sites:
			title = site.xpath('a/text()').extract()
			link = site.xpath('a/@href').extract()
			if len(title) >0 and len(link)>0:
				archivos.append([title[0],link[0]])
		item['archivo'] = archivos
		return item