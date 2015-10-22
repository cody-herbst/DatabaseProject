CREATE DATABASE ClassSchedule;

Use ClassSchedule;

Create Table Courses (
	course_id Varchar(10),
	course_name Varchar(100),
    registration_level Varchar(50),
    Primary Key (course_id)
);

Create Table Sections (
    id int NOT NULL AUTO_INCREMENT,
	course_id Varchar(10),
    section_name Varchar(10),
    associate_term Varchar(25),
    credit_hours Varchar(1),
    seats_available Varchar(3),
    campus Varchar (30),
    Foreign Key (course_id) references Courses(course_id),
    Primary Key (id)
);

CREATE TABLE MeetTimes (
	id INT NOT NULL AUTO_INCREMENT,
    section_id INT NOT NULL,
    meet_type VARCHAR(25),
    time_val VARCHAR(30),
    days VARCHAR(10),
    location VARCHAR(50),
    schedule_type VARCHAR(50),
    instructor VARCHAR(74),
    Primary Key (id),
    Foreign Key (section_id) references Sections(id) 
);