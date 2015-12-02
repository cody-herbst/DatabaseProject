import MySQLdb

criteria = {}

def buildWhereClause():
  conditionList = []
  for key, item in criteria.iteritems():
    if item != None and item != "":
        if key == 'instructor':
            conditionList.append('instructor Like %(instructor)s')
        elif key == 'from':
            conditionList.append('credit_hours >= %(from)s')
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
