from Course import Course
from bs4 import BeautifulSoup
from Section import Section
from MeetTimes import MeetTime
from Locations import *
from Instructors import *
import CourseManager

def Parse(html):
  parsedHtml = BeautifulSoup(html, 'html5lib')
  allTableRows = parsedHtml.find('table', {'class':'datadisplaytable', 'summary':'This layout table is used to present the sections found'}).tbody.find_all('tr', recursive=False)
  while allTableRows:
    ParseTableRow(allTableRows)

def ParseTableRow(tableRows):
  dataRow = tableRows.pop()
  headerRow = tableRows.pop()
  course = CreateCourse(dataRow, headerRow)
  CourseManager.StageCourse(course)

def CreateCourse(dataRow, headerRow):
  # get id_val and name_val
  header_info = headerRow.find('a').text # one full string ex: Math for a Digital World - 21370 - CIS 0823 - 001
  split_value = header_info.split(' - ')
  id_val = str(split_value[2]) #position of course_id
  name_val = str(split_value[0]) #position of name_val

  # get reg_lev_val
  reg_lev_val = str(dataRow.td.find(text='Registration Levels: ').parent.next.next).rstrip('\n')

  # create and return course
  course = Course(id_val, name_val, reg_lev_val)
  section = CreateSection(id_val, dataRow, headerRow)
  course.AddSection(section)
  return course

def CreateSection(course_id, dataRow, headerRow):
  # get section id
  header_info = headerRow.find('a').text
  split_value = header_info.split(' - ')
  sec_name = str(split_value[3])

  # get associated term, credits, seats available and campus_val
  term_val = str(dataRow.td.find(text='Associated Term: ').parent.next.next).rstrip('\n')
  term_array = term_val.split()
  year_val = term_array[0]
  semester_val = term_array[1]

  credit_val = str(dataRow.td.find(text='Credit Hours: ').parent.next.next).rstrip('\n').lstrip()
  seats_ava_val = str(dataRow.td.find(text='Seats Available: ').parent.parent.next.next.next).rstrip('\n')
  campus_val = ""
  if 'Main Campus' in str(dataRow.td):
    campus_val = 'Main Campus'
  elif 'Ambler Campus' in str(dataRow.td):
    campus_val = 'Ambler Campus'
  elif 'Center City Campus' in str(dataRow.td):
    campus_val = 'Center City Campus'
  elif 'Japan Campus' in str(dataRow.td):
    campus_val = 'Japan Campus'

  # create section
  section = Section(course_id, sec_name, semester_val, year_val, credit_val, seats_ava_val, campus_val)


  for meetRow in dataRow.tbody.find_all('tr', recursive=False):
      if meetRow.find('td'):
        meetTime = CreateMeetTime(meetRow)
        section.AddMeetTimes(meetTime)
  return section

def CreateMeetTime(dataRows):
  alltabledata = dataRows.find_all('td')
  type_val = str(alltabledata[0].text)
  time_val = str(alltabledata[1].text)
  days_val = alltabledata[2].text
  location_id = AddLocation(str(alltabledata[3].text))
  schedule_type_val = str(alltabledata[6].text)

  instructor_name_list = str(alltabledata[7].text).split()
  instructor_name = ' '.join(instructor_name_list)

  instructor_id = AddInstructor(instructor_name)

  return MeetTime(type_val, time_val, days_val, location_id, schedule_type_val, instructor_id)



