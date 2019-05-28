# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import codecs
import house.settings
import house.house_model

class HousePipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingHouseapeline(object):
    def __init__(self):
        self.insert_house_data = []
        time_string = house.settings.DATA_NAME
        file_name = time_string + "_hours.txt"
        self.file = codecs.open(file_name, 'wb', 'utf-8')
        house.house_model.init_db()
    
    def process_item(self, item, spider):
        self.insert_house_data.clear()
        for i in range(1, len(item['title'])):
            insert_h = house.house_model.House()
            insert_h.title = str(item['title'][i])
            insert_h.area = str(item['area'][i])
            insert_h.link = str(item['link'][i])
            insert_h.location = str(item['location'][i])
            insert_h.follow = str(item['follow'][i])
            insert_h.totalPrice = str(item['totalPrice'][i])
            insert_h.unitPrice = str(item['unitPrice'][i])
            self.insert_house_data.append(insert_h)
            
        house.house_model.insert_data_many(self.insert_house_data)
        return item
    
    def spider_closed(self, spider):
        self.file.close()
