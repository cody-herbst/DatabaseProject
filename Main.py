"""Script to gather course and section data from temple cs program."""

import sys
import urllib
import Parser
from ClassForm import ClassForm
import CourseManager

# 03 is spring 36 is fall
def Controller():
  schedules = [ClassForm('201303', 'CIS'), ClassForm('201436', 'CIS'), ClassForm('201403', 'CIS'), ClassForm('201536', 'CIS'), ClassForm('201503', 'CIS')]
  for schedule in schedules:
    html = schedule.submit()
    Parser.Parse(html)

  CourseManager.StoreAllCourses()

# hello

Controller()
