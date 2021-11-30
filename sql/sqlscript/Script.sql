-- table 만들기
CREATE TABLE user_t(id INTEGER PRIMARY KEY,
username TEXT, email TEXT, phone TEXT,
website TEXT, regdate TEXT);

-- table 만들기
CREATE TABLE user_t2(id INTEGER PRIMARY KEY,
username TEXT, email TEXT, phone TEXT,
website TEXT, regdate TEXT);

-- table 삭제
DROP TABLE user_t2 

-- table 입력
insert into user_t values(1, 'kim', 'kim@cozlab.com', '010-1234-5678','cozlab.com','20201024');
insert into user_t values(2, 'lee', 'lee@naver.com', '010-1234-5678','naver.com','20201024');
insert into user_t values(3, 'hwang', 'hwang@cozlab.com', '010-2356-0978','cozlab.com','20201024');
insert into user_t values(4, 'oh', 'oh@naver.com', '010-1234-5678','naver.com','20201024');
insert into user_t values(5, 'jeon','jeon@googl.com','010-9876-5432','googl.com','20211025');

-- Read(select)
SELECT 
FROM user_t ut ;
SELECT  username, phone
FROM user_t;

-- UPDATE 
update user_t set email ='kim@google.com', phone ='010-2356-3245'
WHERE id=1;

--DELETE 
DELETE FROM user_t 
WHERE id=3;

-- 테이블 완전삭제
DROP TABLE user_t ;

CREATE TABLE post(id INTEGER NOT NULL PRIMARY KEY,
title TEXT NOT NULL, content TEXT NOT NULL);

DROP  TABLE post;