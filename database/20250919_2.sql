select * from code_master where use_yn = 'Y';
select * from usertbl;

-- 서울 대신에 코드에있는 값을 불러와서 서울특별시 .. 이런형태로 고객정보 조회
-- join 해야하고... 매칭되는 기준 컬럼  code_value & addr
-- 테이블 명은 별칭

select 
u.userid,
u.name,
u.addr,
c.code_name
from usertbl u
left join code_master c
	on u.addr = c.code_value
    and c.code_type = 'ADDR'
where c.use_yn ='Y'    
;    

