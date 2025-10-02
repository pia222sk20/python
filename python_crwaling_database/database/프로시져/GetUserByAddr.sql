CREATE DEFINER=`root`@`localhost` PROCEDURE `GetUserByAddr`(IN p_addr char(2))
BEGIN
	IF p_addr IS NULL or p_addr = '' THEN
		-- 지역이 없거나 빈 문자열이면 전체 회원 조회
        select
			userid,
            name,
            addr,
            c.code_name as addr_name
        from usertbl u
        left join code_master c
			on c.code_type = 'ADDR' and c.code_value = u.addr
		order by name;
	ELSE
		-- 특정 지역의 회원만 조회
        select
			userid,
            name,
            addr,
            c.code_name as addr_name
        from usertbl u
        left join code_master c
			on c.code_type = 'ADDR' and c.code_value = u.addr
		where u.addr = p_addr
		order by name;
	END IF;
END