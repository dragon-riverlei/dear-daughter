# -*- coding: utf-8 -*-
#
# 2015年上海市高中学校代码
#
# Input:
# 2015年复旦大学、上海交通大学综合评价录取考生名单公示
# http://www.shmeea.edu.cn/node2/node118/node119/node175/node679/userobject1ai18445.html

# 
# Output: 初中代码(后6位),区,初中校名

import scrapy

class ShanghaiSeniorHighSchoolCode2015 (scrapy.Spider):
    name = "ShanghaiSeniorHighSchoolCode2015"
    allowed_domains = ["www.shmeea.edu.cn"]
    start_urls = ["http://www.shmeea.edu.cn/node2/node118/node119/node175/node679/userobject1ai18445.html"]
    code_map = {}

    def parse(self, response):
        trs = response.xpath("/html/body/table[4]/tr[1]/td[1]/div[1]/table[1]/tr[2]/td[2]/table[1]/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr")
        for i in range(1, len(trs)):
            values = trs[i].xpath("td/text()").extract()
            print ",".join((values[1].encode("UTF-8"), values[3].encode("UTF-8"), values[4].encode("UTF-8")))
    
