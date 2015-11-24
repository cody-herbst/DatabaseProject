class Instructor:

   instructors = []

   current_id = 0

   def __init__(self, name):
        Instructor.current_id += 1
        self.InstructorInfo = {}
        self.InstructorInfo['instructor_id'] = Instructor.current_id
        self.InstructorInfo['instructor'] = name

''' def StoreAll(cursor):
        for instructor in instructors:
            placeholders = ', '.join(['%s'] * len(instructor.InstructorInfo))
            columns = ', '.join(instructor.InstructorInfo.keys())
            qry = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('Instructors', columns, placeholders)
            cursor.execute(qry, instructor.InstructorInfo.values())


    def AddInstructors(instructor_name):
        for instructor in instructors:
            if instructor.InstructorInfo['instructor'] == instructor_name:
                return  instructor.InstructorInfo['instructor_id']
        newInstructor = Instructor(instructor_name)
        instructors.append(newInstructor)
        return newInstructor.InstructorInfo['instructor_id']'''

def StoreAllInstructors(cursor):
    for instructor in Instructor.instructors:
        placeholders = ', '.join(['%s'] * len(instructor.InstructorInfo))
        columns = ', '.join(instructor.InstructorInfo.keys())
        qry = "INSERT INTO %s ( %s ) VALUES ( %s )" % ('Instructors', columns, placeholders)
        cursor.execute(qry, instructor.InstructorInfo.values())
def AddInstructor(instructor_name):
    for instructor in Instructor.instructors:
        if instructor.InstructorInfo['instructor'] == instructor_name:
            return  instructor.InstructorInfo['instructor_id']
    newInstructor = Instructor(instructor_name)
    Instructor.instructors.append(newInstructor)
    return newInstructor.InstructorInfo['instructor_id']

