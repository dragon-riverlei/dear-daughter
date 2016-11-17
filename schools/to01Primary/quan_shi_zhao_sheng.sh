#!/usr/bin/bash

./quan_shi_zhao_sheng.py | paste - - - - - - - | awk '$4!="0.0"{print}' | sed 's/\t/,/g' | iconv -f UTF-8 -t GBK > quan_shi_zhao_sheng.csv
./quan_shi_zhao_sheng.py | paste - - - - - - - | awk '$4=="0.0"{print}' | sed 's/\t/,/g' | iconv -f UTF-8 -t GBK > qu_nei_zhao_sheng.csv
