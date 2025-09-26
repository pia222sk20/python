select height from usertbl where name = '박보검';

-- 서브쿼리
-- 박보검보다 키가 큰 사람
select * 
from usertbl 
where 
	height > (select height     -- 박보검의 키를 출력
		from usertbl 
        where name = '박보검');

-- 박보검보다 나이가 많은사람        
select * 
from usertbl 
where 
	birthyear < (select birthyear 
		from usertbl 
        where name = '박보검');    
        
-- 박보검 보다 나이가 많으면서 키가 170이상인 사람

select * 
from usertbl 
where 
	birthyear < (select birthyear 
		from usertbl 
        where name = '박보검')
	and height >= 170
        ;           

-- 1. usertbl의 모든 데이터를 조회
select * from usertbl;
-- 2. 성이 김씨성을 가지는 사람을 모두 출력
select * from usertbl where name like '김%';
-- 3. 박씨성을 가진 사람중에서 서울에 사는 사람
select * from usertbl where name like '박%' and addr = '서울';
-- 4. 이씨성을 가진 사람들중에서 지역이 서울이 아닌 사람들
select * from usertbl where name like '이%' and addr not in ('서울');
-- 5. 1980년 이후 출생자이면서 키가 170이상이고 성씨가 박씨인 사람들
select * from usertbl where birthyear > 1980 and height >= 170;


-- any : 서브쿼리의 결과중에 하나라도 만족
-- all : 서브쿼리의 결과중에 모두만족

-- 서울에 사는 사람들의 키보다 큰 사람들
-- 서울에사는 사람들의 키중에 가장 작은 키보다 큰 사람들만 추출
select count(*)
from usertbl
where height > 
any(select min(height) from usertbl where addr = '서울');

-- 사람들의 키의 값들을 모두 만족하는 
-- 경남에서 가장 큰 키보다 큰 사람들
select *
from usertbl
where height > 
all(select height from usertbl where addr = '경남');

-- 경남지역의 사람들의 키와 같은 값을 가지는 모든지역의 사람들
select *
from usertbl
where height = 
any(select height from usertbl where addr = '경남');

select height from usertbl where addr = '경남' order by height desc;