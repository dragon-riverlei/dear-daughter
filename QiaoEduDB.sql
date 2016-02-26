create database if not exists `qiao_edu` character set utf8;

use qiao_edu;

create table if not exists `junior_high_school` (
       `code` varchar(6) primary key,
       `area` varchar(10) not null,
       `name` varchar(40) not null
);
create table if not exists `senior_high_school` (
       `name` varchar(40) not null
);
create table if not exists `university` (
       `code` varchar(6) primary key,
       `name` varchar(40) not null
);
create table if not exists `senior_high_school_pre_admission` (
       `stu_no` bigint primary key,
       `from_code` varchar(6) not null,
       `to_name` varchar(40) not null,
       `year` smallint not null
);
