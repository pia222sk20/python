use newuserdb;
select distinct birthyear from usertbl where birthyear = 1972;

-- 테이블 복사(구조 + 데이터)
create table copy_usertbl (select name from usertbl);

-- 구조만 복사usertbl
create table copy2_usertbl like usertbl;
-- 기존 테이블에 다른 테이블의 데이터를 가져와서 추가
insert into copy2_usertbl(name,birthyear) select name, birthyear from usertbl;

select * from copy2_usertbl;

use employees;
select gender,min(birth_date) as birth_date from employees group by gender;

-- 회원별 구매 횟수가 3회 이상인 사람
-- select
-- usrid, count(*)
-- from order
-- group by userid
-- having count(*) <=3

use sakila;
select * from payment;

select customer_id, count(*)
from payment
group by customer_id
having count(*) >=30
;

-- payment테이블의 amount 금액
-- 각 고객별 총 결제 금액
select 
	customer_id, 
	max(amount) max,
    avg(amount) avg,
    sum(amount) sum
from payment
	group by customer_id
    order by max desc, avg desc
;

-- rollup  총합과 단위합  group by 절과 함께 사용
-- 고객별  총 결제금액 + 전체 합계
select 
customer_id,
staff_id,
sum(amount)
from payment
group by customer_id,staff_id with rollup
;

select 
year(payment_date), month(payment_date) ,
sum(amount)
from payment
group by year(payment_date), month(payment_date) with rollup 
;