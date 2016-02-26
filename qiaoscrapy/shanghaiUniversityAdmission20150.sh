#!/usr/bin/bash

scrapy crawl ShanghaiJuniorHighSchoolCode2015 | sed 's/上海市//g' > ../to02JuniorHigh/2015/shanghaiJuniorHighSchoolCode2015

scrapy crawl ShanghaiUniversityAdmission20150 |  sed 's/上海市//g' > ../to04University/2015/admission0
