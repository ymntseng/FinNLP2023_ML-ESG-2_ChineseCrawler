# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EsgCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # origin
    pk = scrapy.Field()
    URL = scrapy.Field()
    news_headline = scrapy.Field()
    impact_type = scrapy.Field()

    # new add by crawler
    news_content_html = scrapy.Field()
    news_content = scrapy.Field()