use ClassSchedule;

select associate_term, course_name, credit_hours, instructor, course_id, days
from (Courses Natural Join Sections) Natural Join MeetTimes
where course_name = 'Cyberspace & Society';