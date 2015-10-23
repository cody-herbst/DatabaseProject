# for every section there could be one or many meet times

#includes all relevant info for section

class MeetTime:

  def __init__(self,  meet_type, time, days, location, schedule_type, instructor ):
      self.MeetTimeInfo = {}
      self.MeetTimeInfo['meet_type'] = meet_type
      self.MeetTimeInfo['time_val'] = time
      self.MeetTimeInfo['days'] = days
      self.MeetTimeInfo['location'] = location
      self.MeetTimeInfo['schedule_type'] = schedule_type
      self.MeetTimeInfo['instructor'] = instructor

  def Store(self, cursor, section_id):
      #store section info
      self.MeetTimeInfo['section_id'] = section_id
      placeholders = ', '.join(['%s'] * len(self.MeetTimeInfo))
      columns = ', '.join(self.MeetTimeInfo.keys())
      qry = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('MeetTimes', columns, placeholders)
      cursor.execute(qry, self.MeetTimeInfo.values())
