# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TextPipeline(object):
    def __init__(self):
        self.fp = None

    def open_spider(self,spider):
        print("爬虫开始")
        self.fp = open('./data.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        line = item['title'] +"\n" + item['time'] +"\n" + item['subject'] +"\n" +item['content'] +"\n" +"\n"
        self.fp.write(line)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束")