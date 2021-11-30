BEGIN TRANSACTION;
CREATE TABLE usersdb(id integer primary key,             username text, email text, phone text, website text, regdate text);
INSERT INTO "usersdb" VALUES(1,'kim','kim@naver.com','010-3456-4567','kim.com','2021-10-25 14:48:32');
INSERT INTO "usersdb" VALUES(2,'Park','park@naver.com','010-3456-4567','park.com','2021-10-25 14:48:32');
INSERT INTO "usersdb" VALUES(3,'Lee','lee@naver.com','010-3333-3333','lee.com','2021-10-25 14:48:32');
INSERT INTO "usersdb" VALUES(4,'Cho','cho@naver.com','010-4444-4444','cho.com','2021-10-25 14:48:32');
INSERT INTO "usersdb" VALUES(5,'Yue','yue@naver.com','010-5555-5555','yue.com','2021-10-25 14:48:32');
INSERT INTO "usersdb" VALUES(6,'Sea','sea@naver.com','010-6666-6666','sea.com','2021-10-25 14:48:32');
COMMIT;
