CREATE DATABASE ClassSchedule;

Use ClassSchedule;

Create Table Courses (
	course_id VarChar(16),
	course_name Varchar(100),
    registration_level Varchar(50),
    Primary Key (course_id)
);

Create Table Sections (
    section_id INT NOT NULL AUTO_INCREMENT,
	course_id VarChar(16),
    section_name Varchar(10),
    year Varchar(4),
    semester Varchar (6),
    credit_hours Varchar(1),
    seats_available Varchar(3),
    campus Varchar (30),
    Foreign Key (course_id) references Courses(course_id),
    Primary Key (section_id)
);

CREATE TABLE MeetTimes (
	meet_times_id INT NOT NULL AUTO_INCREMENT,
    section_id INT NOT NULL,
    meet_type VARCHAR(25),
    time_val VARCHAR(30),
    days VarChar(7),
    location_id INT NOT NULL,
    schedule_type VARCHAR(50),
    instructor_id INT NOT NULL,
    Primary Key (meet_times_id),
    Foreign Key (section_id) references Sections(section_id)
    #Foreign Key (location_id) references Locations(location_id)
    #Foreign Key (instructor_id) references Instructors(instructor_id)
);

Create Table Instructors (
	instructor_id INT NOT NULL,
    instructor VARCHAR(50)
);

Create Table Locations (
	location_id INT NOT NULL,
    building VARCHAR(30),
    room_number VARCHAR(10)
);
