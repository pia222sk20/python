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


select * from customer;


-- customer_backup 테이블 생성 및 데이터 추가
create table customer_backup
select * from customer where customer_id <= 10;

select * from customer_backup;
-- customer_backup 테이블에 데이터를 추가
insert into customer_backup 
select * from customer where customer_id > 10;


-- update customer_id가 1인 고객의 activer 0으로 수정
select * from customer_backup where customer_id = 1; 

update customer_backup 
set active = 0, address_id=4
where customer_id = 1;


select * from customer_backup where customer_id = 1; 
delete from customer_backup
where customer_id = 1;

-- shopdb 삭제
drop database if exists shopdb;

/*
요구사항 분석
쇼핑몰 database shopdb
고객정보(고객id,이름)
상품정보(상품id,이름,단가,수량)
주문정보(고객id,상품id,구매가격)

액션: 회원가입
상품정보 출력
상품구입
상품정보 입력
대쉬보드 : 고객별 상품별 구매회수, 평균구매액
*/

select * from customer;
insert into customer values(null,'홍길동');

update customer 
set name = '강감찬'
where customer_id = 1;

delete from customer;