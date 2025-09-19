CREATE DEFINER=`root`@`localhost` PROCEDURE `AddCodeWithTransaction`(
	IN p_code_type char(4),
    IN p_code_value char(10),
    IN p_code_name varchar(50),
    IN p_display_order int,
    IN p_use_yn char(1)
)
BEGIN
	-- 사용자가 발생시키는 에러 중복이면
    declare v_exists int default 0;
    -- 시스템 예외가 발생했을때 처리
    declare exit handler for sqlexception
    begin
		rollback;
        select 'error transaction rollback' as message;
    end;
    -- 중복코드 체크
    select count(*) into v_exists
    from code_master
    where code_type = p_code_type and code_value = p_code_value;
    
    if v_exists > 0 then
		signal sqlstate '45000'
        set message_text = 'code already existes';
	else
		start transaction;
        insert into code_master
        values(p_code_type,p_code_value,p_code_name,p_display_order,p_use_yn);
        commit;
        select 'code added success' as message;
    end if;
    
END