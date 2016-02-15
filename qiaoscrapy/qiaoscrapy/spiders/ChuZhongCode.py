# -*- coding: utf-8 -*-
# 上海初中代码
# 根据2015上海市中招政策性照顾名单公示整理

import scrapy

class ShanghaiChuZhongCodeSpider2015(scrapy.Spider):
    name = "ShanghaiChuZhongCode2015"
    allowed_domains = ["www.shmeea.edu.cn"]
    start_urls = ["http://www.shmeea.edu.cn/node2/node118/node120/node209/node485/userobject1ai18315.html"
                  "http://www.shmeea.edu.cn/node2/node118/node120/node209/node485/userobject1ai18370.html",
                  "http://www.shmeea.edu.cn/node2/node118/node120/node209/node485/userobject1ai18383.html",
                  "http://www.shmeea.edu.cn/node2/node118/node120/node209/node485/userobject1ai18402.html"]
    
    def parse(self, response):
        trs = response.xpath('/html/body/table[4]/tr[1]/td/div/table/tr[2]/td[2]/table/tbody/tr')
        # if(response.url==self.start_urls[0] or response.url==self.start_urls[1]):
        if(response.url==self.start_urls[0]):
            tri = range(2, len(trs))
        else:
            tri = range(4, len(trs))
        for i in tri:
            self.extractTr(trs[i])

    def extractTr(self, tr):
        values =  tr.xpath('td/descendant::*/text()')
        print values[1].extract().encode("UTF-8") + "," + values[2].extract().encode("UTF-8") + "," +  values[3].extract().encode("UTF-8") + "," +  values[4].extract().encode("UTF-8") + "," +  values[5].extract().encode("UTF-8") + "," +  values[6].extract().encode("UTF-8") + "," +  values[7].extract().encode("UTF-8") + "," +  values[8].extract().encode("UTF-8")
            
    
    
