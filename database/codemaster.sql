use sqldb;
-- 공통코드 테이블 생성
drop table if exists code_master;
CREATE TABLE code_master (
    code_type CHAR(4) NOT NULL, -- 코드 분류 (예: ADDR, MOB1, GRPN)
    code_value CHAR(10) NOT NULL, -- 코드 값 (예: 서울, 011, 전자)
    code_name VARCHAR(50) NOT NULL, -- 코드 설명 (예: 서울특별시, SKT, 전자제품)
    display_order INT DEFAULT 0, -- 표시 순서
    use_yn CHAR(1) DEFAULT 'Y', -- 사용 여부 (Y/N)
    PRIMARY KEY (code_type, code_value)
);

-- 지역 코드 (ADDR)
INSERT INTO code_master (code_type, code_value, code_name, display_order) VALUES
('ADDR', '서울', '서울특별시', 1),
('ADDR', '경기', '경기도', 2),
('ADDR', '경남', '경상남도', 3),
('ADDR', '전남', '전라남도', 4),
('ADDR', '경북', '경상북도', 5);

-- 통신사 코드 (MOB1)
INSERT INTO code_master (code_type, code_value, code_name, display_order) VALUES
('MOB1', '011', 'SKT', 1),
('MOB1', '016', 'KT', 2),
('MOB1', '019', 'LGU+', 3),
('MOB1', '018', '알뜰폰', 4),
('MOB1', '010', '공통', 5);

-- 상품 분류 코드 (GRPN)
INSERT INTO code_master (code_type, code_value, code_name, display_order) VALUES
('GRPN', '전자', '전자제품', 1),
('GRPN', '의류', '의류', 2),
('GRPN', '서적', '도서', 3);