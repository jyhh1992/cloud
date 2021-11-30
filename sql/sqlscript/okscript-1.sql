use okdb;
FROM gmv_trend;

SELECT category FROM gmv_trend gt ;
SELECT yyyy FROM gmv_trend gt ;
-- 중복제거
SELECT DISTINCT  yyyy, category from gmv_trend gt ;

-- != <> 제외
SELECT *
FROM  gmv_trend gt 
WHERE  yyyy != 2021;
SELECT *
FROM  gmv_trend gt 
WHERE  yyyy <> 2021;

SELECT *
FROM gmv_trend gt 
WHERE category  in('농축수산물');

SELECT *
FROM gmv_trend gt 
WHERE category  not in('농축수산물');

SELECT *
FROM gmv_trend gt 
WHERE category  like('농축수산물');

SELECT *
FROM gmv_trend gt 
WHERE category  not like('농축수산물');

-- csv 파일 로딩시 숫자는 숫자 데이터 속성으로 설정해서 로딩하기(sum과 같은 계산)
SELECT category cate, yyyy year_,
sum(gmv) total_gmv
FROM gmv_trend gt 
group by category , yyyy;

SELECT * FROM gmv_trend gt ;

SELECT category cate, yyyy year_,
sum(gmv) total_gmv
FROM gmv_trend gt 
group by 1,2;#select column 나열순서

SELECT category cate, yyyy year_,
min(gmv) total_gmv
FROM gmv_trend gt 
group by category , yyyy;

SELECT category cate, yyyy year_,
max(gmv) total_gmv
FROM gmv_trend gt 
group by category , yyyy;

SELECT category cate, yyyy year_,
avg(gmv) total_gmv
FROM gmv_trend gt 
group by category , yyyy;

SELECT yyyy,
sum(gmv) total_gmv, min(gmv) min_, max(gmv) max_, avg(gmv) avg_
FROM gmv_trend gt 
group by 1;

SELECT category, yyyy, sum(gmv) as total_gmv
from gmv_trend gt
WHERE gmv >= 1000
group by 1, 2;
-- 조건에 맞는 

SELECT category, yyyy , sum(gmv) as total_gmv
from gmv_trend gt
group by 1, 2
HAVING sum(gmv) >= 2000;

SELECT category, yyyy, sum(gmv) as tot_gmv 
from gmv_trend
group by 1, 2
order by 1, 3 DESC ;

SELECT * from online_order oo ;























