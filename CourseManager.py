import MySQLdb

course_dict = {}

def StageCourse(course):
    if course.CourseInfo['course_id'] in course_dict:
      course_dict[course.CourseInfo['course_id']].AddSections(course.Sections)
    else:
      course_dict[course.CourseInfo['course_id']] = course

def StoreAllCourses():
  db = MySQLdb.connect(host="localhost", # your host, usually localhost
                       user="root", # your username
                       passwd="1234", # your password
                       db="ClassSchedule") # name of the data base

  # you must create a Cursor object. It will let
  #  you execute all the queries you need
  try:
    cursor = db.cursor()
    for course_key, course_val in course_dict.iteritems():
      course_val.Store(cursor)
    db.commit()
  except MySQLdb.Error as e:
    db.rollback()
    raise e

  finally:
    cursor.close()
    db.close()
