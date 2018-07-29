# -*- coding: utf-8 -*-
import codecs
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FarenPipeline(object):
    def __init__(self):
        # 打开 mydata.json文件
        self.file = codecs.open("C:/Users/Administrator/AppData/Local/Programs/Python/Python36/Scripts/faren/far"
        "en/mydata.json","wb",encoding="utf-8")

    def process_item(self, item, spider):
        i = json.dumps(dict(item), ensure_ascii=False)
        # 每条数据后加上换行
        line = i + '\n'
        # 数据写入到mydata.json文件中
        self.file.write(line)
        return item

    def close_spider(self,spider):
        #关闭mydata.json文件
        self.file.close()