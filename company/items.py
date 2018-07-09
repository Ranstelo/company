# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    com_des = scrapy.Field()
    com_name = scrapy.Field()
    com_fund_needs_name = scrapy.Field()
    com_addr = scrapy.Field()
    com_born_date = scrapy.Field()
    com_cat_name = scrapy.Field()
    com_id = scrapy.Field()
    com_sub_cat_name = scrapy.Field()

