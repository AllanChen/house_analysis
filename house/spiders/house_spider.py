import scrapy
import json
from scrapy import log,signals
from house.items import HouseItem

class HouseSpider(scrapy.Spider):
    name = "house"
    allowed_domains = ["house.com"]
    start_urls = [
        "https://gz.lianjia.com/ershoufang/nansha/p1p2p3p4/",
        "https://gz.lianjia.com/ershoufang/nansha/pg2p1p2p3p4/",
        "https://gz.lianjia.com/ershoufang/nansha/pg3p1p2p3p4/",
        "https://gz.lianjia.com/ershoufang/nansha/pg4p1p2p3p4/",
        "https://gz.lianjia.com/ershoufang/nansha/pg5p1p2p3p4/",
        "https://gz.lianjia.com/ershoufang/nansha/pg6p1p2p3p4/",
        "https://gz.lianjia.com/ershoufang/nansha/pg7p1p2p3p4/",
        "https://gz.lianjia.com/ershoufang/nansha/pg8p1p2p3p4/",
        "https://gz.lianjia.com/ershoufang/nansha/pg9p1p2p3p4/",
        "https://gz.lianjia.com/ershoufang/nansha/pg10p1p2p3p4/"
    ]

    def parse(self, response):
        items = []
        response_data = response.xpath('//ul[@class="sellListContent"]')
        for data in response_data:
            title_data = data.xpath('//div[@class="title"]')
            address_data = data.xpath('//div[@class="houseInfo"]')
            flood_data = data.xpath('//div[@class="positionInfo"]')
            follow_info_data = data.xpath('//div[@class="followInfo"]')
            tag_data = data.xpath('//div[@class="tag"]')
            totalPrice_data = data.xpath('//div[@class="totalPrice"]')
            unitPrice_data = data.xpath('//div[@class="unitPrice"]')

            item = HouseItem()
            item['title'] = title_data.xpath('a/text()').extract()
            item['link'] = title_data.xpath('a/@href').extract()
            item['flood'] = flood_data.xpath('text()').extract()
            item['area'] = flood_data.xpath('a/text()').extract()
            item['follow'] = follow_info_data.xpath('text()').extract()
            item['location'] = address_data.xpath('text()').extract()
            item['totalPrice'] =totalPrice_data.xpath('span/text()').extract()
            item['unitPrice'] = unitPrice_data.xpath('span/text()').extract()
            items.append(item)
        return items


            

