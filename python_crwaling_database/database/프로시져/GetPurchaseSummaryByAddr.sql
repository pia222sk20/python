CREATE DEFINER=`root`@`localhost` PROCEDURE `GetPurchaseSummaryByAddr`(IN p_addr char(2))
BEGIN
	declare v_total_count int default 0;
    -- 구매건수 확인
    select
		count(*) into v_total_count
	from usertbl u
    join buytbl b
		on u.userid = b.userid
	where u.addr = p_addr or p_addr is Null;
    
    if v_total_count =0 then
		select 'No purchase data' as message;
	else
		select
			u.userid,
            u.name,
            c.code_value as addr_name,
            count(b.num) as purchase_count,
            sum(b.price * b.amount) as total_price
        from usertbl u
        join buytbl b
			on u.userid=b.userid
		left join code_master c
			on c.code_type='ADDR' and c.code_value = u.addr
		where u.addr = p_addr or p_addr is Null
        group by u.userid, u.name, c.code_name
        order by total_price desc;
	end if;
END