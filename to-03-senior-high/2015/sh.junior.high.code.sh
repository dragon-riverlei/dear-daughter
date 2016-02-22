cat priority.dueto.gov.01 priority.dueto.gov.03 priority.dueto.gov.04  | grep -v "考生报名号" | grep -v "大屯" | grep -v "张家洼" | grep -v "E+11" | grep -v "宝山" | grep -v "崇明" | grep -v "梅山" | grep -v "松江" | grep -v "金山" | grep -v "青浦" | grep -v "奉贤" | grep -v "往届生" | grep -v "个别报名" | awk '{print gensub(/[0-9]{2}([0-9]{6})[0-9]{4}/, "\\1", "g", $2),  $5, $6}' | sort | uniq | grep -v "^ "> sh.junior.high.code.tmp

cat priority.dueto.gov.02 | grep -v "宝山" | grep -v "崇明" |  grep -v "松江" | grep -v "金山" | grep -v "青浦" | grep -v "奉贤" | awk '{print gensub(/[0-9]{2}([0-9]{6})[0-9]{4}/, "\\1", "g", $2),  $3, $5}' | grep -v "中考报名号" | sort | uniq >> sh.junior.high.code.tmp

cat sh.junior.high.code.tmp | sort | uniq | awk '$2!="女"{print}' | sed 's/新区//g' | sed 's/区//g' | awk '{school[$1] = $2 "," $3}END{for(c in school){print c "," school[c]}}' | sort | uniq  > sh.junior.high.code
rm sh.junior.high.code.tmp

