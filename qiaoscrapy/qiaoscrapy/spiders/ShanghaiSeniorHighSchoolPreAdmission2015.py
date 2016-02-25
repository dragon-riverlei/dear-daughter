# -*- coding: utf-8 -*-
# 
# 2015年上海市高中学校“提前招生录取”考生名单
#
# Input: http://www.shmeea.edu.cn/20150712.htm
# Output: 考生编号,录取高中
# 

import scrapy

class ShanghaiSeniorHighSchoolPreAdmission2015 (scrapy.Spider):
    name = "ShanghaiSeniorHighSchoolPreAdmission2015"
    allowed_domains = ["www.shmeea.edu.cn"]
    start_urls = ["http://www.shmeea.edu.cn/20150712.htm"]
    school_name_map = {}
    def parse(self, response):
        links = response.xpath('/html/body/table[1]/tr/td/table/tr/td/p/strong/span/a/@href').extract()
        for link in links:
            school_name = "".join(response.xpath('/html/body/table[1]/tr/td/table/tr/td//a[@href="' + link +'"]//text()').extract())
            self.school_name_map[link] = school_name
            yield scrapy.Request(link, self.extractStudent)

    def extractStudent(self, response):
        stu_no = response.xpath('/html/body/table[1]/tr/td/table/tr[3]/td[2]/text()').extract()
        if(len(stu_no)>0):
            self.extractJuniorHighSchoolCode(response, '/html/body/table[1]/tr/td/table/tr')
        else:
            stu_no = response.xpath('/html/body/div/table[1]/tr/td/table/tr[3]/td[2]/text()').extract()

        if(len(stu_no)>0):
            self.extractJuniorHighSchoolCode(response, '/html/body/div/table[1]/tr/td/table/tr')
        else:
            stu_no = response.xpath("/html/body/div/table/tr[3]/td[2]/text()").extract()

        if(len(stu_no)>0):
            self.extractJuniorHighSchoolCode(response, '/html/body/div/table/tr')
        else:
            stu_no = response.xpath('/html/body/table/tr/td/div/table/tr[3]/td[2]/text()').extract()

        if(len(stu_no)>0):
            self.extractJuniorHighSchoolCode(response, '/html/body/table/tr/td/div/table/tr')            
        else:
            print response.url

    def extractJuniorHighSchoolCode(self, response, selector):
        students = response.xpath(selector)
        idx = range(3, len(students))
        for i in idx:
            stu_no = students[i].xpath("td[2]/text()").extract()
            if(len(stu_no)==1 and stu_no[0].isdigit()):
                print stu_no[0].encode("UTF-8") + "," + self.school_name_map[response.url].encode("UTF-8")
