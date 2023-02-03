
# 创建数据库
drop database if exists at_sea_chat_db;
create database at_sea_chat_db;

use at_sea_chat_db;

create table user
(
    userid     int primary key not null auto_increment,
    username   varchar(255) unique default 'noname',
    `password` varchar(255)        default 'password',
    email      varchar(255) unique default 'example@example.com'
);
insert into user (userid, username, password, email)
values (1, 'testuser', 'testpassword', 'test@test.com'),
       (2, 'huber wang', 'kjhl', 'huberwang@163.com'),
       (3, 'google', 'googlepassword', 'google@gmail.com');


create table token
(
    create_date datetime default now(),
    token varchar(32),
    userid int not null ,
    foreign key (userid) references user(userid)
);
insert into token (token, userid)
values ('11111111111111111111111111111111', 1),
       ('22222222222222222222222222222222', 2),
       ('33333333333333333333333333333333', 3);
