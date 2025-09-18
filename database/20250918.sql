use newuserdb;
select distinct birthyear from usertbl where birthyear = 1972;

-- 테이블 복사(구조 + 데이터)
create table copy_usertbl (select name from usertbl);

-- 구조만 복사
create table copy2_usertbl like usertbl;
-- 기존 테이블에 다른 테이블의 데이터를 가져와서 추가
insert into copy2_usertbl(name,birthyear) select name, birthyear from usertbl;

select * from copy2_usertbl;