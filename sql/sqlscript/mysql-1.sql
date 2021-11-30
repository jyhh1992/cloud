-- 데이터 베이스 생성
CREATE DATABASE mydb2;
CREATE DATABASE okdb;

-- DB선택하기
USE okdb;

CREATE TABLE mytable2(
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
modelnumber VARCHAR(15) NOT NULL,
series VARCHAR(30) NOT NULL,
PRIMARY KEY(id)
);

CREATE TABLE mytable3 (
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
name CHAR(20) NOT NULL,
age TINYINT,
phone VARCHAR(20),
email VARCHAR(30) NOT NULL,
address VARCHAR(50),
PRIMARY KEY(id)
);

-- 데이터 입력
USE mydb2;

-- 필드명을 지정하지않으면 모든 필드명을 작성해야한다
INSERT INTO mytable2 VALUES(1,'i7','7700','Kaby Lake');

-- 필드명을 지정하면 해당하는 부분만 작성가능
INSERT INTO mytable2 (name,modelnumber,series)
VALUES('i8','3080','Multi');
INSERT INTO mytable2 (name,modelnumber,series)
VALUES('i7','8700k','Core');
INSERT INTO mytable2 (name,modelnumber,series)
VALUES('i7','8565u','low');
INSERT INTO mytable2 (name,modelnumber,series)
VALUES('i5','8279u','coffee');

-- 데이터 읽기
SELECT * FROM mytable2;
SELECT name FROM mytable2;
SELECT name AS cpu_name FROM mytable2;
SELECT * FROM mytable2 ORDER BY id DESC;
SELECT * FROM mytable2 WHERE id <3;

DROP TABLE mytable ;

SELECT * FROM mytable2 WHERE name LIKE '%5';

SELECT * FROM mytable2 LIMIT 3;

SELECT * FROM mytable2;

UPDATE mytable2 SET name = 'i5', modelnumber = '5500' WHERE id = 3;

DELETE FROM mytable2 WHERE id = 3;

CREATE DATABASE rec;

CREATE DATABASE okdb;

CREATE DATABASE csm_db;












