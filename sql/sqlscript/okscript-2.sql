use okdb;

SELECT * from online_order oo ;
SELECT * FROM  category c ;
SELECT * FROM  user_info ui  ;

SELECT  * FROM item i ;

SELECT itemid, sum(gmv) as tot_gmv
from online_order 
group by 1
order by 2 desc;

##실습 2) 온라인 주문 데이터 분석
##2021년 6월 1일 하루동안의 주문 건

##1. 데이터 탐색 ##############################
## 비회원 주문 : userid null, 
SELECT  userid FROM user_info
group by 1
;

##a) 주문 테이블


##b) 상품 테이블


##c) 카테고리 테이블



##d) 유저 테이블



##2. TOP 상품의 매출 확인

##상품별 매출액 집계 후, 매출액 높은 순으로 정렬하기



##상품이름을 상품ID와 나란히 놓아서 한눈에 상품별 매출액을 확인할 수 있도록 하자.

select itemid, item_name, sum(gmv) as tot_gmv
from online_order as oo 
join item i on oo.itemid = i.id
GROUP by 1,2
ORDER by 3 desc;


##추가질문: 카테고리별 매출액은 어떻게 될까?
### 2중 join 하여 특정 컬럼만 보기
select oo.orderid, i.item_name, c.cate2
from online_order oo
join item i on oo.itemid = i.id 
join category c on i.category_id = c.id;


##Join 테이블에 Join을 한번 더
select i.item_name, c.cate1, sum(gmv) as tot_gmv
from online_order oo
join item i on oo.itemid = i.id 
join category c on i.category_id = c.id 
group by 1,2
order by 2 desc;

##추가질문: 성/연령별 매출액은 어떻게 될까?



##나이대별 출과 사용자수는 어떻게 될까?



##3. 카테고리별 주요 상품의 매출 확인



##추가질문: 남성이 구매하는 아이템은 어떤 것이 있을까?



##추가질문: 남성의 나이대별 구매하는 아이템은 어떤 것이 있을까?