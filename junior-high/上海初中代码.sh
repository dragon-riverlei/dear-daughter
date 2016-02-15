cat 2015年上海市中招政策性照顾名单公示（第一批） 2015年上海市中招政策性照顾名单公示（第三批） 2015年上海市中招政策性照顾名单公示（第四批） | grep -v "考生报名号" | grep -v "大屯" | grep -v "张家洼" | grep -v "E+11" | grep -v "宝山" | grep -v "崇明" | grep -v "梅山" | grep -v "松江" | grep -v "金山" | grep -v "青浦" | grep -v "奉贤" | grep -v "往届生" | grep -v "个别报名" | awk '{print gensub(/[0-9]{2}([0-9]{6})[0-9]{4}/, "\\1", "g", $2),  $6}' | sort | uniq > 上海初中代码.tmp

cat 2015年上海市中招政策性照顾名单公示（第二批） | awk '{print gensub(/[0-9]{2}([0-9]{6})[0-9]{4}/, "\\1", "g", $2), $5}' | grep -v "中考报名号" | sort | uniq >> 上海初中代码.tmp

cat 上海初中代码.tmp | sort | uniq > 2015上海初中代码
rm 上海初中代码.tmp
