
import json
import scrapy

from pprint import pprint

class SteamSpider(scrapy.Spider):
  name = 'steamtags'
  start_urls = ['http://store.steampowered.com/tag/browse/']
  each_title = []

  def parse(self, response):
    for title in response.css('.tag_browse_tag'):
      yield {
        'tag': title.css('::text').extract_first()
      }