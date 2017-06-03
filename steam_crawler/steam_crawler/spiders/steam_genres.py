
import json
import scrapy

from pprint import pprint

class SteamSpider(scrapy.Spider):
  name = 'steamgenre'
  start_urls = ['http://store.steampowered.com/games']
  each_title = []

  def parse(self, response):
    for genre in response.css('.popup_menu_item'):
      yield {
        'genre': genre.css('::text').extract_first().strip()
      }