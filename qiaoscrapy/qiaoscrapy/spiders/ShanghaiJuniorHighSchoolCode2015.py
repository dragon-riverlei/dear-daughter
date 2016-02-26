# -*- coding: utf-8 -*-
#
# 2015年上海市初中学校代码
#
# Input: http://sh.zhongkao.com/e/20150527/556564db491e1.shtml
# Output: 初中代码(后6位),区,初中校名

import scrapy

class ShanghaiJuniorHighSchoolCode2015 (scrapy.Spider):
    name = "ShanghaiJuniorHighSchoolCode2015"
    allowed_domains = ["www.zhongkao.com"]
    start_urls = ["http://sh.zhongkao.com/e/20150527/556564db491e1.shtml"]
    code_map = {}
    
    def parse(self, response):
        trs =  response.xpath('/html/body/div[4]/div[3]/div[1]/table/tbody/tr')
        for i in range(1, len(trs)):
            values =  trs[i].xpath('td/text()').extract()
            self.code_map[values[2].strip()] = (values[1].strip(), values[3].strip())

        for key in self.code_map.keys():
            (area, name) =self.code_map[key]
            print key[3:].encode("UTF-8") + "," + area.encode("UTF-8") + "," + name.encode("UTF-8")
