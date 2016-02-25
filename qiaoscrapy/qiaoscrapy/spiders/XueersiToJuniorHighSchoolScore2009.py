# -*- coding: utf-8 -*-
# 学而思2009小升初录取情况

import scrapy

class XueersiToJuniorHighSchoolScore2009 (scrapy.Spider):
    name = "XueersiToJuniorHighSchoolScore2009"
    allowed_domains = ["jzb.com"]
    start_urls = ["http://jzb.com/bbs/thread-216777-1-1.html"]
    nextLink = ""
    
    def parse(self, response):
        self.extractScores(response)
        while(self.nextLink!=""):
            yield scrapy.Request(self.nextLink, self.extractScores)

    def extractScores(self, response):
        print self.nextLink
        nextPage = response.css('span.pgt span.eduu_pg a.nxt')
        if(len(nextPage)>0):
            self.nextLink = nextPage.xpath('@href').extract()[0]
        else:
            self.nextLink = ""
        
        threadBoxs = response.css('.eduu_brg.eduu_thread_Box')
        for tbi in range(len(threadBoxs)):
            trs = threadBoxs[tbi].xpath('table/tr[2]/td[1]/div[1]/div/div[1]/table/tr[1]/td[1]/table/tr')
            if(len(trs)>0):
                print len(trs)
                for tri in range(1, len(trs)):
                    value1 = trs[tri].xpath('td/div/font/font/text()').extract()
                    value2 = trs[tri].xpath('td/div/font/font/font/text()').extract()
                    value3 = trs[tri].xpath('td/font/font/text()').extract()
                    if(len(value1)==5):
                        value = value1
                    if(len(value2)==5):
                        value = value2
                    if(len(value3)==5):
                        value = value3
                    print value[0].encode("UTF-8") + "," + value[1].encode("UTF-8") + "," + value[2].encode("UTF-8") + "," + value[3].encode("UTF-8") + "," + value[4].encode("UTF-8")
