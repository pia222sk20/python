CREATE DEFINER=`root`@`localhost` PROCEDURE `ManageCode`(
	IN p_code_type char(4),
    IN p_code_value char(10),
    IN p_code_name varchar(50),
    IN p_display_order int,
    IN p_use_yn char(1),
	IN p_action varchar(10) -- insert, update   
)
BEGIN
	IF p_action = 'insert' THEN
		-- 데이터 추가
        insert into code_master 
        values(p_code_type,p_code_value,p_code_name,p_display_order,p_use_yn);
    ELSEIF p_action = 'update' THEN
		-- 데이터 수정
        update code_master
        set code_name = p_code_name,
			display_order = p_display_order,
            use_yn = p_use_yn
        where code_type = p_code_type and code_value = p_code_value;
    ELSE
		-- 에러발생
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'invalide action! update or insert';
    END IF;
END