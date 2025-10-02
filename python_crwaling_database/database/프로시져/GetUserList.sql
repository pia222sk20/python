CREATE DEFINER=`root`@`localhost` PROCEDURE `GetUserList`()
BEGIN
	select
		userid,
        name,
        birthyear,
        addr
    from usertbl
    order by name
    ;
END