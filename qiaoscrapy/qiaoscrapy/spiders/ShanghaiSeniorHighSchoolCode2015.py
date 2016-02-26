# -*- coding: utf-8 -*-
#
# 2015年上海市高中学校代码
#
# Input:
# 2015年复旦大学、上海交通大学综合评价录取考生名单公示
# http://www.shmeea.edu.cn/node2/node118/node119/node175/node679/userobject1ai18445.html
#
# 2015年上海市普通高校自主招生录取考生名单公示
# http://www.shmeea.edu.cn/node2/node118/node119/node175/node679/userobject1ai18504.html
# 
# Output: 考生编号,高中,大学

import scrapy

class ShanghaiUniversityAdmission20150 (scrapy.Spider):
    name = "ShanghaiUniversityAdmission20150"
    allowed_domains = ["www.shmeea.edu.cn"]
    start_urls = [
        "http://www.shmeea.edu.cn/node2/node118/node119/node175/node679/userobject1ai18445.html",
        "http://www.shmeea.edu.cn/node2/node118/node119/node175/node679/userobject1ai18504.html"
    ]
    code_map = {}

    def parse(self, response):
        if response.url == self.start_urls[0] :
            trs = response.xpath("/html/body/table[4]/tr[1]/td[1]/div[1]/table[1]/tr[2]/td[2]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr")
            for i in range(1, len(trs)):
                values = trs[i].xpath("td/text()").extract()
                print ",".join((values[1].encode("UTF-8"), values[3].encode("UTF-8"), values[4].encode("UTF-8")))
        else:
            trs = response.xpath("/html/body/table[4]/tr[1]/td[1]/div[1]/table[1]/tr[2]/td[2]/table[1]/tbody/tr")
            for i in range(1, len(trs)):
                values = trs[i].xpath("td/font/text()").extract()
                print ",".join((values[1].encode("UTF-8"), values[4].encode("UTF-8"), values[5].encode("UTF-8")))
                
