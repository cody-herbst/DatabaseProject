use ClassSchedule;

select *
from (Courses Natural Join Sections) Natural Join MeetTimes
where course_name = 'Cyberspace & Society';