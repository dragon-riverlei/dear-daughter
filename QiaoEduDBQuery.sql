-- 
select j.name, count(j.name) rank  from senior_high_school_pre_admission join junior_high_school j on j.code = from_code  where to_name like "上海中学" or to_name like "华师大二附中" oo to_name like "复旦附中" or to_name like "交大附中" or to_name like "七宝中学" group by j.name order by rank desc limit 20;


