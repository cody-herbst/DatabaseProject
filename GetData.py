import MySQLdb

criteria = {}

def buildWhereClause():
  conditionList = []
  for key, item in criteria:
    if item == None:
        criteria.pop(key)
    else:
        if key == 'name_list':
            for name in item:
                conditionList.append('instructor like "%' + name + '%"')
        elif key == 'from':
            conditionList.adend('credit_hours >= ' + item)
        elif key == 'to':
            conditionList.adend('credit_hours <= ' + item)
        else:
            condition = key + ' = ' + item
            conditonList.append(condition)

  if not conditionList:
      return ";"
  else:
    return ' Where ' +  ' and '.join(conditionList) + ';'

def executeQuery():
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="root", # your username
                         passwd="1234", # your password
                         db="ClassSchedule") # name of the data base
    try:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT associate_term, course_name, credit_hours, instructor, course_id, days " +
                        "FROM (Courses Natural Join Sections) Natural Join MeetTimes" + buildWhereClause())
        rows = cursor.fetchall()

        retval = ''
        for row in rows:
           retval = retval + buildHtml(row)

        return retval
    except MySQLdb.Error as e:
        print buildWhereClause()
        cursor.close()
        db.close
        return "<tr><td>error {0}</tr></td>".format(e.args[1])
    finally:
        cursor.close()
        db.close()

def buildHtml(row):
   return '<tr class="returnRow">' \
   '<td>' + row['associate_term'] + '</td>' \
   '<td>' + row['course_name'] + '</td>' \
   '<td>' + row['credit_hours'] + '</td>' \
   '<td>' + row['instructor'] + '</td>' \
   '<td>' + row['course_id'] + '</td>' \
   '<td>' + row['days'] + '</td>' \
   '<tr>'
