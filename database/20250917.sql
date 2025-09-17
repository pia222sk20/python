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
-- 2. 성이 김씨성을 가지는 사람을 모두 출력
-- 3. 박씨성을 가진 사람중에서 서울에 사는 사람
-- 4. 이씨성을 가진 사람들중에서 지역이 서울이 아닌 사람들
-- 5. 1980년 이후 출생자이면서 키가 170이상이고 성씨가 박씨인 사람들
