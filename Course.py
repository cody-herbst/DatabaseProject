#includes all relevant info of course including section
from Section import Section
class Course:

  def  __init__(self, course_id, course_name, registration_level):
    self.CourseInfo = {}
    self.Sections = []
    self.CourseInfo['course_name'] = course_name
    self.CourseInfo['course_id'] = course_id
    self.CourseInfo['registration_level'] = registration_level

  def Store(self, cursor):
    # store Course info
    placeholders = ', '.join(['%s'] * len(self.CourseInfo))
    columns = ', '.join(self.CourseInfo.keys())
    qry = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('Courses', columns, placeholders)
    cursor.execute(qry, self.CourseInfo.values())

    for Section in self.Sections:
      Section.Store(cursor)

  def AddSection(self, section):
    self.Sections.append(section)

  def AddSections(self, sections):
    self.Sections.extend(sections)
