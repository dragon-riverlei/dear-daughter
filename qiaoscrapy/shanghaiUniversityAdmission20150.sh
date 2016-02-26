#!/usr/bin/bash

scrapy crawl ShanghaiUniversityAdmission20150 |  sed 's/上海市//g' > ../to04University/2015/admission0
