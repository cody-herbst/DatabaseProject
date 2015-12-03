import MySQLdb
import json

criteria = {}

def buildWhereClause():
  conditionList = []
  for key, item in criteria.iteritems():
    if item != None and item != "":
        if key == 'instructor':
            conditionList.append('instructor Like \'%s\'' % ('%%'+ item + '%%'))
        elif key == 'from':
            conditionList.append('credit_hours >= %(from)s')
        elif key == 'course_id':
            conditionList.append('course_id Like \'%s\'' % ('%%' + item + '%%'))
        elif key == 'to':
            conditionList.append('credit_hours <= %(to)s')
        else:
            condition = key + ' = ' + '%(' + key + ')s'
            conditionList.append(condition)

  if not conditionList:
      return ""
  else:
    return ' Where ' +  ' and '.join(conditionList)

def executeQuery():
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="root", # your username
                         passwd="1234", # your password
                         db="ClassSchedule") # name of the data base
    try:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        #return "<tr><td>where clause {}</tr>".format(criteria)
        cursor.execute("SELECT year, semester, section_name, course_name, credit_hours, instructor, course_id, days " +
                        "FROM ((Courses Natural Join Sections) Natural Join MeetTimes ) Natural Join Instructors" +  buildWhereClause() + " Order By section_id;", criteria)
        rows = cursor.fetchall()
        retval = ''
        for row in rows:
           retval = retval + buildHtml(row)

        return retval
    except MySQLdb.Error as e:
        print buildWhereClause()
        cursor.close()
        db.close
        return "<tr><td>error {}</td><td>where clause {}</tr>".format(e.args[1], buildWhereClause())
    finally:
        cursor.close()
        db.close()

def buildHtml(row):
   return '<tr class="returnRow">' \
   '<td>' + row['year'] + " " + row['semester'] + '</td>' \
   '<td>' + row['course_name'] + '</td>' \
   '<td>' + row['credit_hours'] + '</td>' \
   '<td>' + row['instructor'] + '</td>' \
   '<td>' + row['course_id'] + '</td>' \
   '<td>' + row['section_name'] + '</td>' \
   '<td>' + row['days'] + '</td>' \
   '</tr>'


def executeAggregation():
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="root", # your username
                         passwd="1234", # your password
                         db="ClassSchedule") # name of the data base
    try:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select building, room_number, count(*) as count\
                from MeetTimes join Locations using(location_id)\
                where room_number != 'TBA'\
                group by  location_id\
                order by count desc\
                limit 10;")
        rows = cursor.fetchall()

        return json.dumps(rows)
    except MySQLdb.Error as e:
        cursor.close()
        db.close
        return "<tr><td>error {}</td><td>where clause {}</tr>".format(e.args[1], buildWhereClause())
    finally:
        cursor.close()
        db.close()

def getInstructors():
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="root", # your username
                         passwd="1234", # your password
                         db="ClassSchedule") # name of the data base
    try:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select * from Instructors;")
        rows = cursor.fetchall()

        retval = []
        for row in rows:
            retval.append("<option value=\"%(instructor)s\">%(instructor)s</option>" % {'instructor' : row['instructor']})

        return json.dumps(retval)

    except MySQLdb.Error as e:
        cursor.close()
        db.close
    finally:
        cursor.close()
        db.close()

def getCourses():
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="root", # your username
                         passwd="1234", # your password
                         db="ClassSchedule") # name of the data base
    try:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select * from Courses;")
        rows = cursor.fetchall()

        retval = []
        for row in rows:
            retval.append("<option value=\"%(course)s\">%(course)s</option>" % {'course' : row['course_id']})

        return json.dumps(retval)

    except MySQLdb.Error as e:
        cursor.close()
        db.close
    finally:
        cursor.close()
        db.close()

