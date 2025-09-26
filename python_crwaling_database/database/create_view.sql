CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `sqldb`.`user_buy_code_tbl` AS
    SELECT 
        `u`.`userID` AS `userID`,
        `u`.`name` AS `name`,
        `c`.`code_name` AS `addr_name`,
        `b`.`prodName` AS `prodName`,
        `b`.`price` AS `price`,
        `b`.`amount` AS `amount`,
        (`b`.`price` * `b`.`amount`) AS `total_price`,
        `cm`.`code_name` AS `code_name_mob1`,
        `cmt`.`code_name` AS `code_name_grpn`
    FROM
        ((((`sqldb`.`usertbl` `u`
        LEFT JOIN `sqldb`.`buytbl` `b` ON ((`u`.`userID` = `b`.`userID`)))
        LEFT JOIN `sqldb`.`code_master` `c` ON (((`c`.`code_type` = 'ADDR')
            AND (`c`.`code_value` = `u`.`addr`))))
        LEFT JOIN `sqldb`.`code_master` `cm` ON (((`cm`.`code_type` = 'MOB1')
            AND (`cm`.`code_value` = `u`.`mobile1`))))
        LEFT JOIN `sqldb`.`code_master` `cmt` ON (((`cmt`.`code_type` = 'GRPN')
            AND (`cmt`.`code_value` = `b`.`groupName`))))
    WHERE
        ((`c`.`use_yn` = 'Y')
            OR (`cm`.`use_yn` = 'Y')
            OR (`cmt`.`use_yn` = 'Y'))
    ORDER BY `u`.`name`
    ;