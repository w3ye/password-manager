create table acc(
account_id int primary key,
username varchar(255) not null,
psword varchar(255) not null,
app_name varchar(255) not null,
note varchar(255) default null
);