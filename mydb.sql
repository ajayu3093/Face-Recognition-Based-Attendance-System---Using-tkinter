create database Attendance;
use Attendance;
CREATE TABLE Attendance (
    ID varchar(30),
    NAME VARCHAR(255) NOT NULL,
    DATE DATE NOT NULL,
    TIME TIME NOT NULL
);
select * from Attendance;
SELECT * FROM Attendance WHERE DATE = CURDATE();
SELECT * FROM Attendance WHERE DATE = '2024-05-16';

drop table Attendance;
