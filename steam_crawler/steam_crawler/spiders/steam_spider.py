
import json
import scrapy

from pprint import pprint

class SteamSpider(scrapy.Spider):
  name = 'steam'
  start_urls = ['http://store.steampowered.com/search?category1=998']
  each_title = []

  def parse(self, response):
    for title in response.css('.search_result_row'):

      yield {
        'title': title.css('.search_name .title::text').extract_first(),
        'link': title.css('a ::attr(href)').extract_first()
      }

    maximum_page = response.css('.search_pagination_right > a ::text')[::-1][1].extract()
    for i in range(1, int(maximum_page)):
      yield scrapy.Request('http://store.steampowered.com/search?category1=998&page=%d' % i, callback=self.parse)