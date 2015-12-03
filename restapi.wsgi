import sys, os, GetData, bottle, MySQLdb
from bottle import route, request, template, static_file

os.chdir(os.path.dirname(__file__))

sys.path = ['/var/www/DatabaseProject/'] + sys.path

@route('/')
def home():
    return static_file('index.html', root='/var/www/DatabaseProject/public_html/')

@route('/myjavascript')
def javascript():
    return static_file('index.js', root='/var/www/DatabaseProject/public_html/')

@route('/mycss')
def css():
    return static_file('index.css', root='/var/www/DatabaseProject/public_html/')

@route('/jquery')
def jquery():
    return static_file('jquery.js', root='/var/www/DatabaseProject/public_html/')

@route('/query', method='POST')
def query():
    year = request.forms.get('Year')
    term = request.forms.get('Term')
    course_title = request.forms.get('CourseTitle')
    hours_from = request.forms.get('From')
    hours_to = request.forms.get('To')
    course_num = request.forms.get('CourseNumber')
    instructor = request.forms.get('Instructor')
    days_list = request.forms.getlist('Days')

    GetData.criteria['year'] = year
    GetData.criteria['semester'] = term
    GetData.criteria['instructor'] = instructor
    GetData.criteria['course_name'] = course_title
    GetData.criteria['days'] = buildDaysString(days_list)
    GetData.criteria['from'] = hours_from
    GetData.criteria['to'] = hours_to
    GetData.criteria['course_id'] = course_num

    return GetData.executeQuery()

    #return "<tr><td>" + GetData.criteria['days'] + "</tr></td>"

@route('/aggregation')
def aggregation():
    return GetData.executeAggregation()

def buildDaysString(days):
  retString = ""
  for day in days:
      if(day == "Thursday"):
          retString = retString + "R"
      else:
          retString = retString + day[0]

  return retString

bottle.debug(True)
application = bottle.default_app()
