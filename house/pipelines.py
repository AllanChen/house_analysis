# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import time
import json,codecs,sys,csv
import house.settings
import house.test
class HousePipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingLianjiapeline(object):
    def __init__(self):
        time_string = house.settings.DATA_NAME
        file_name = time_string + "_hours.txt"
        self.file = codecs.open(file_name, 'wb', 'utf-8')
        house.test.init_db()
        
    def process_item(self, item, spider):
        title_list = item['title']
        for i in range(1, len(title_list)):
            line = json.dumps(
                    {
                        "title":str(item['title'][i]),
                        'area':str(item['area'][i]),
                        'link':str(item['link'][i]),
                        'location':str(item['location'][i]),
                        # 'tag1' : str(item['tag1'][i]) ,
                        # 'tag2': str(item['tag2'][i]),
                        'follow' : str(item['follow'][i]),
                        'totalPrice':str(item['totalPrice'][i]),
                        'unitPrice':str(item['unitPrice'][i]),
                    },ensure_ascii=False)
            line += ","
            self.file.write(line)

        time_string = house.settings.DATA_NAME
        file_name = time_string + "_hours.txt"
        self.txt_to_json(file_name)
        return item
    
    
    def txt_to_json(self,txt_name):
        data = ""
        time_string = house.settings.DATA_NAME
        with open(txt_name, 'r', encoding='utf-8') as file:
            data = file.read()
    
        data = "[" + data
        data = data + "]"
        data = data.replace(",]", "]")
        json_save_name = time_string + "_hours.json"
        file = codecs.open(json_save_name, 'wb', 'utf-8')
        file.write(data)
    
    
        with open(json_save_name, 'r', encoding='utf-8') as f:
            data_json = json.load(f)
            f.close()
    
        house.test.insert_data(data)
    
    def spider_closed(self, spider):
        self.file.close()
