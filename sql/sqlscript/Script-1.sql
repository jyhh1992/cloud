CREATE TABLE post(id INTEGER NOT NULL PRIMARY KEY,
title TEXT NOT NULL, content TEXT NOT NULL);

CREATE TABLE usersd(id INTEGER NOT NULL PRIMARY KEY,
name TEXT NOT NULL, phone TEXT NOT NULL, address text);

INSERT into post (id,title,content) values(1,'코딩','재미있어요!');
INSERT into post (id,title,content) values(2,'java','객체지향언어');
INSERT into post (id,title,content) values(3,'html','웹 표준 언어');
INSERT into post (id,title,content) values(4,'javascript','잘하면좋겠네');
INSERT into post (id,title,content) values(5,'django','풀 스택 개발 프레임워크');

INSERT  into usersd  (id,name,phone, address) values (1,'kim','010-1111-1111','seoul');
INSERT  into usersd  (id,name,phone, address) values (2,'song','010-2222-2222','seoul');
INSERT  into usersd  (id,name,phone, address) values (3,'lee','010-3333-3333','daegu');
INSERT  into usersd  (id,name,phone, address) values (4,'park','010-4444-4444','pusan');
INSERT  into usersd  (id,name,phone, address) values (5,'lee','010-5555-5555','daegu');

SELECT title, content FROM post;
SELECT * FROM  post p ;

SELECT * FROM post WHERE id=2;

SELECT * FROM post WHERE title like 'java%';

SELECT * FROM post WHERE title like '코딩';

SELECT title, content FROM post WHERE id BETWEEN  1 and 3;

SELECT * FROM usersd WHERE address IN  ('seoul','daegu');

SELECT * FROM post ORDER BY title ASC;

UPDATE post SET title ='제목수정중', content ='본문 수정중'  WHERE  id = 3;

SELECT * FROM post p ;

DELETE  FROM  post WHERE  id=3;

SELECT * FROM post p ;





