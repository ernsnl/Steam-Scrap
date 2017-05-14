
import json
import scrapy

from pprint import pprint

class SteamGameInfoSpider(scrapy.Spider):
  name = 'steamgame'

  def start_requests(self):
    with open('steam_games.json') as data_file:    
        data = json.load(data_file)
        for game in data:
          yield scrapy.Request(game['link'], callback=self.parse, cookies={
            'birthtime': '28801',
            'lastagecheckage': '1-January-1923',
            'steamCountry': 'US',
            'timezoneOffset': '-28800',
            'mature_content': '1'
          })

  def parse(self, response):
    yield {
      'title': response.css('.apphub_AppName::text').extract_first(),
      'app_id': response.url,
      'description': response.css('.game_description_snippet::text').extract_first(),
      'review_data': {
        'total_review_count' : response.css('meta[itemprop*=reviewCount]::attr(content)').extract_first(),
        'rating': response.css('meta[itemprop*=ratingValue]::attr(content)').extract_first()
      },
      'tags': [tag.strip() for tag in response.css('.popular_tags a::text').extract()],
      'genres': [genre.strip() for genre in response.css('.details_block a[href*=genre]::text').extract()],
      'about': response.css('#game_area_description').extract_first()
    }