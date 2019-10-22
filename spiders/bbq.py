# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import re
from lxml import etree
from text.items import TextItem

class BbqSpider(scrapy.Spider):
    name = 'bbq'
    # allowed_domains = ['www.xxx.com']
    r_list = ['投资', '融资', '领投', '轮', '万元', '获得']
    path = r"/Users/kimmy/phantomjs-2.1.1-macosx/bin/phantomjs"
    # path = r"./text/phantomjs"
    bro = webdriver.PhantomJS(path)
    bro.get('https://www.pedaily.cn/first/')
    page_text = bro.page_source
    chocie_date = input(">>请输入要查询的年份:").strip()
    flag = re.findall(chocie_date, page_text)
    while not flag:
        bro.find_element_by_id("loadmore").click()
        page_text = bro.page_source
        flag = re.findall(chocie_date, page_text)
    tree = etree.HTML(page_text)
    start_urls = tree.xpath('//div[@id="firstnews-list"]/ul/li/div[@class="desc"]/a/@href')
    print("网页抓取结束")
    def parse(self, response):
        title = response.xpath('//h1[@id="newstitle"]/text()').extract_first()
        for i in self.r_list:
            if i in title:
                time = response.xpath('//div[@class ="info"]/div[1]/span[1]//text()')[0].extract()
                subject = response.xpath('//div[@class="subject"]/text()')[0].extract()
                content_list = response.xpath('//div[@id="news-content"]//text()').extract()
                content = "".join(content_list).strip().replace("\r\n", '')
                item = TextItem()
                item['title'] = title
                item['time'] = time
                item['subject'] = subject
                item['content'] = content
                yield item
                break





