# -*- coding: utf-8 -*-
# 上海初中代码
# 根据2015上海市中招政策性照顾名单公示整理

import scrapy

class ShanghaiSeniorHighPreAdmission2015 (scrapy.Spider):
    name = "ShanghaiSeniorHighPreAdmission2015"
    allowed_domains = ["www.shmeea.edu.cn"]
    start_urls = ["http://www.shmeea.edu.cn/20150712.htm"]

    def parse(self, response):
        links = response.xpath('/html/body/table[1]/tr/td/table/tr/td/p/strong/span/a/@href').extract()
        for link in links:
            yield scrapy.Request(link, self.extractSchoolCode)

    def extractSchoolCode(self, response):
        titles = response.xpath('/html/body/div/table[1]/tr/td/table/tr[1]/td[1]/text()').extract()
        print ",".join(titles).encode("UTF-8")
