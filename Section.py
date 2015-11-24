#includes all relevant info for section

class Section:

  def __init__(self, course_id, section_name, semester, year, credit_hours, seats_available, campus):
      self.SectionInfo = {}
      self.MeetTimes = []
      self.SectionInfo['course_id'] = course_id
      self.SectionInfo['section_name'] = section_name
      self.SectionInfo['semester'] = semester
      self.SectionInfo['year'] = year
      self.SectionInfo['credit_hours'] = credit_hours
      self.SectionInfo['seats_available'] = seats_available
      self.SectionInfo['campus'] = campus

  def Store(self, cursor):
      #store section info
      placeholders = ', '.join(['%s'] * len(self.SectionInfo))
      columns = ', '.join(self.SectionInfo.keys())
      qry = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('Sections', columns, placeholders)
      cursor.execute(qry, self.SectionInfo.values())
      this_section_id = cursor.lastrowid
      for MeetTime in self.MeetTimes:
          MeetTime.Store(cursor, this_section_id)


  def AddMeetTimes(self, MeetTime):
      self.MeetTimes.append(MeetTime)
